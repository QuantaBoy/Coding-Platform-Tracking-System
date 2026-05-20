import requests

headers = {
    "User-Agent" : "Mozilla/5.0"
}

def get(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 404:
            return {"error": "User Not Found"}
        elif response.status_code == 403:
            return {"error" : "Codeforce Request Blocked"}
        elif response.status_code == 429:
            return {"error": " Too Many Requests"}
        elif response.status_code != 200:
            return {"error" : f"Api Error:{response.status_code}"}
        data = response.json()

        if data.get("status") != "OK":
            return {"error" : data.get("comment", "Unknown API Error")}
        return data
    except requests.exceptions.Timeout:
        return {"error":"Request Timed Out"}
    except Exception as e:
        return {"error" : str(e)}

def sanitize_username(username):
    username = username.strip()

    if "/" in username:
        username = username.split('/')[-1]
    return username

def get_user_info(username):
    username = sanitize_username(username)

    url = f"https://codeforces.com/api/user.info?handles={username}"
    data = get(url)

    if "error" in data:
        return data
    
    user = data["result"][0]

    return {
        "handle":user.get("handle"),
        "rank":user.get("rank"),
        "rating" : user.get("rating"),
        "max_rank":user.get("maxRank"),
        "max_rating" : user.get("maxRating")
    }

def get_rating_history(username):
    username = sanitize_username(username)

    url = f"https://codeforces.com/api/user.rating?handle={username}"
    data = get(url)

    if "error" in data:
        return data
    
    rating_history = []

    for contest in data['result'][:-20]:
        rating_history.append({
            "contest_name" : contest.get("contestName"),
            "rank" : contest.get("rank"),
            "old_rating" : contest.get("oldRating"),
            "new_rating" : contest.get("newRating")
        })
    return rating_history

def get_language_statistics(username):
    username = sanitize_username(username)

    url = f"https://codeforces.com/api/user.status?handle={username}"
    data = get(url)

    if "error" in data:
        return data
    language_stats = {}

    for submission in data['result'][:100]:
        language = submission.get("programmingLanguage")
    
        if not language:
            continue

        if language in language_stats:
            language_stats[language] +=1
        else:
            language_stats[language] = 1

    return language_stats

def build_full_codeforces_profile(username):

    user_info = get_user_info(username)
    if "error" in user_info:
        return user_info
    language_stats = get_language_statistics(username)
    rating_history = get_rating_history(username)

    return {
        "user_info" : user_info,
        "language_stats" : language_stats,
        "rating_history" : rating_history
    }

print(build_full_codeforces_profile("Benq"))