from dotenv import load_dotenv
import requests
import os 

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization" : 
    f"Bearer {GITHUB_TOKEN}" 
}

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        return {"message":"Github user not found"}
    data = response.json()
    return {
        "username" : data.get("login"),
        "name" : data.get("name"),
        "bio" : data.get("bio"),
        "public_repos" : data.get("public_repos")
     }

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        return {"message" : "Repositories Not Found"}
    
    data = response.json()

    repo = []

    for item in data:
        repo.append({
            "repo_name" : item.get("name"),
            "main_language" : item.get("language"),
            "stars" : item.get("stargazers_count"),
        })

    return repo

def get_language_stats(username):
    repo = 