import requests
from config import TOKEN, BASE_URL


def get_bot_info():
    """
    Task 1: Get Bot Information
    - Use getMe method
    - Return bot's name and username
    - Show verification status
    """
    url=f"{BASE_URL}/getMe"
    response=requests.get(url)
    data=response.json()
    user=data["result"]
    a=user["first_name"]
    s=user["username"]
    return a,s
print(get_bot_info())

