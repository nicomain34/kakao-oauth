import requests

# Your data (OAuth credentials)
REST_API_KEY = 'a228f7377d1b3c9e4ea12529fcc37b0a'  # Your REST API key
REDIRECT_URI = 'YOUR_REDIRECT_URI'  # Replace with your actual redirect URI
AUTH_CODE = 'AUTHORIZATION_CODE_FROM_USER'  # Authorization code obtained after user consent

# Step 1: Obtain access token
url = "https://kauth.kakao.com/oauth/token"

# Data for the token request
data = {
    "grant_type": "authorization_code",
    "client_id": REST_API_KEY,
    "redirect_uri": REDIRECT_URI,
    "code": AUTH_CODE
}

# Send POST request to get the token
response = requests.post(url, data=data)

# Check if the response was successful
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info["access_token"]
    print(f"Access Token: {access_token}")

    # Step 2: Send a message to the user via KakaoTalk

    # Kakao API URL for sending messages
    message_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # Headers for the message request
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Define the message data
    message_data = {
        "template_object": {
            "object_type": "text",
            "text": "Hello, this is a message sent from Kakao API!",
            "link": {
                "web_url": "https://your-website-url.com",
                "mobile_web_url": "https://your-website-url.com"
            },
            "button_title": "Visit Website"
        }
    }

    # Send POST request to send the message
    message_response = requests.post(message_url, headers=headers, json=message_data)

    # Check if the message was sent successfully
    if message_response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error sending message:", message_response.json())
else:
    print("Failed to obtain access token:", response.json())
