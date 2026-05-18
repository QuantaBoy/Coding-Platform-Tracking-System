import requests

def get_user_info(username:str):

    url = f"https://codeforces.com/api/user.info?handles={username}"

    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        return {
            "message" : "User not found"
        }
    user = data['result'][0]
    
    return {
        "handle":user.get("handle"),
        "rank" : user.get("rank"),
        "rating" :user.get("rating"),
        "maxrank" : user.get("maxRank"),
        "maxrating" : user.get("maxRating")
    }
def get_rating_history(username:str):

    url = f"https://codeforces.com/api/user.rating?handle={username}"

    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        return {
            "message" :"Rating history not found"
        }
    
    rating_history = []

    for contest in data['result']:
        rating_history.append({
            "content_name" : contest.get("contestName"),
            "rank" : contest.get("rank"),
            "old_rating" : contest.get("oldRating"),
            "new_rating" : contest.get("newRating")
        })
    
    return rating_history

def get_submission(username:str):
    url = f"https://codeforces.com/api/user.status?handle={username}"

    response = requests.get(url)
    data = response.json()

    if data['status'] != 'OK':
        return {
            "message" : "Submissions not found"
        }
    submissions = []

    for submission in data['result'][:20]:
        problem = submission.get("problem",{})

        submissions.append({
            "problem_name" : submission.get("name"),
            "verdict" : submission.get("verdict"),
            "language" : submission.get("programmingLanguage")
        })
    return submissions