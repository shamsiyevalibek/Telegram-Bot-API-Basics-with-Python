import requests
from config import TOKEN, BASE_URL


def reply_to_last_user():
    """
    Task 3: Auto-Reply System
    - Get most recent update
    - Extract chat_id
    - Send response message
    """
    url=f"{BASE_URL}/getUpdates"
    send=f"{BASE_URL}/sendMessage"
    response=requests.get(url)
    data=response.json()
    updates=data['result'][-1]
    chat_id=updates['message']['chat']['id']
    requests.post(send,params={
        'chat_id': chat_id,
        'text': "alibrk"
    })
    return chat_id
print(reply_to_last_user())