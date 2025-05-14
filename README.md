# Telegram Bot API Basics with Python

## Objective
Learn and implement basic Telegram Bot API methods using Python's requests module or another HTTP client.

## Instructions
Create a Python script named `bot_homework.py` to interact with your Telegram bot using direct HTTP requests.

## Required Tasks

### 1. Bot Information (getMe)
- Implement `get_bot_info()` function using getMe method
- Display bot's name and username
- **Bonus**: Show bot verification status

Example output:
```
Bot Information:
Name: MyAwesomeBot
Username: @my_awesome_bot
Verified: False
```

### 2. Update Monitor (getUpdates)
- Implement `check_updates()` function
- Display last 5 bot updates/messages
- For each message show:
  - User's name
  - Message content
  - Readable timestamp (converted from Unix time)

Example output:
```
Last 5 Updates:
1. From: John Doe
   Message: "Hello bot!"
   Time: May 14, 2025 14:30:25

2. From: Jane Smith
   Message: "How are you?"
   Time: May 14, 2025 14:31:00

3. From: Alice Johnson
   Message: "Testing"
   Time: May 14, 2025 14:32:15
```

### 3. Auto-Reply System (sendMessage)
- Implement `reply_to_last_user()` function that:
  - Retrieves most recent update
  - Extracts chat_id
  - Sends response message ("Hello, I received your message!")

Example output:
```
Message received from: John Doe
Chat ID: 123456789
Response sent: "Hello, I received your message!"
Status: Message delivered successfully
```

## Optional Challenge
Create conditional responses:
- Input: "hi" → Output: "Hello!"
- Input: "bye" → Output: "Goodbye!"
- Input: anything else → Output: "I don't understand."

Example output:
```
User: "hi"
Bot: "Hello!"

User: "bye"
Bot: "Goodbye!"

User: "what's the weather?"
Bot: "I don't understand."
```



