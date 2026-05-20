import requests
import os
import math

from collections import defaultdict
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

base_url = "https://api.github.com"

headers = {
    "Accept": "application/vnd.github.v3+json"
}
if GITHUB_TOKEN:
    headers["Authorization"] = f"token {GITHUB_TOKEN}"


def get(url, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)

        if response.status_code == 404:
            return {"error": "User Not Found"}
        if response.status_code == 403:
            return {"error": "Github API Forbidden"}
        if response.status_code == 429:
            return {"error": "Too Many Requests"}
        if response.status_code != 200:
            return {"error": f"API Error: {response.status_code}"}
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request Timed Out"}
    except Exception as e:
        return {"error": str(e)}


def fetch_github_user(username):
    url = f"{base_url}/users/{username}"
    data = get(url)

    if isinstance(data, dict) and "error" in data:
        return data
    return {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "public_repos": data.get("public_repos"),
    }


def fetch_all_repositories(username):
    repositories = []
    page = 1
    while True:
        url = f"{base_url}/users/{username}/repos"
        data = get(url, params={"per_page": 100, "page": page})

        if isinstance(data, dict) and "error" in data:
            return data
        if not data:
            break
        repositories.extend(data)
        page += 1
    return repositories


def fetch_repository_languages(owner, repo_name):
    url = f"{base_url}/repos/{owner}/{repo_name}/languages"
    data = get(url)

    if isinstance(data, dict) and "error" in data:
        return []

    return list(data.keys())


def analyze_repository(owner, repo):
    try:
        created_at = datetime.strptime(repo.get("created_at"), "%Y-%m-%dT%H:%M:%SZ")
        pushed = datetime.strptime(repo.get("pushed_at"), "%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        created_at = pushed = datetime.utcnow()

    active_days = (pushed - created_at).days
    last_push_days_ago = (datetime.utcnow() - pushed).days

    if last_push_days_ago > 180:
        activity_status = "Inactive"
    elif last_push_days_ago <= 30:
        activity_status = "Active"
    elif active_days > 120:
        activity_status = "Serious Project"
    else:
        activity_status = "Maintained"

    languages = fetch_repository_languages(owner, repo.get("name"))
    stars = repo.get("stargazers_count", 0)

    return {
        "repository_name": repo.get("name"),
        "description": repo.get("description"),
        "languages": languages,
        "status": activity_status,
        "repository_url": repo.get("html_url"),
        "stars": stars,
    }


def build_language_statistics(repositories):
    language_stats = defaultdict(int)

    for repo in repositories:
        for language in repo.get("languages", []):
            language_stats[language] += 1
    return dict(language_stats)


def compute_developer_score(repository_analyses):
    if not repository_analyses:
        return 0

    total_stars = sum(repository.get("stars", 0) for repository in repository_analyses)
    active_projects = sum(1 for repository in repository_analyses if repository.get("status") == "Active")

    score = (
        0.6 * min(active_projects / 5, 1)
        + 0.4 * min(math.log(total_stars + 1, 10), 1)
    )

    return round(score * 100, 2)


def build_full_github_profile(username):
    profile = fetch_github_user(username)

    if isinstance(profile, dict) and "error" in profile:
        return profile

    repos = fetch_all_repositories(username)
    if isinstance(repos, dict) and "error" in repos:
        return repos

    analyzed_repos = []
    for repository in repos:
        if repository.get("fork"):
            continue
        analysis = analyze_repository(username, repository)
        analyzed_repos.append(analysis)

    language_stats = build_language_statistics(analyzed_repos)
    developer_score = compute_developer_score(analyzed_repos)

    return {
        "github_profile": profile,
        "language_stats": language_stats,
        "repositories": analyzed_repos,
        "developer_score": developer_score,
    }