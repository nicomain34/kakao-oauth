# kakao-oauth
This repository contains an example implementation of OAuth 2.0 authentication for Kakao API. It demonstrates how to obtain an access token using the authorization code grant type, allowing you to integrate Kakao services into your application.

# Kakao OAuth Token Request

This Python script is used to obtain an **access token** via **OAuth 2.0** from Kakao API. The script takes an authorization code from the user, which is then exchanged for an access token to interact with the Kakao API.

## Setup Steps:

1. **Obtain REST API Key**:
   - First, you need to create an application on the [Kakao Developers](https://developers.kakao.com/) platform to get your unique **REST API Key**.
   - Use this key to authorize your app.

2. **Obtain Authorization Code**:
   - To get the **Authorization Code**, you need to perform the **OAuth 2.0** authorization flow. The user must grant access to their data via your app.

3. **Setup**:
   - Insert the obtained **REST API Key** into the `REST_API_KEY` variable.
   - Replace `YOUR_REDIRECT_URI` with your **redirect URI** (make sure it's the same URI you specified in your Kakao Developers app settings).
   - Replace `AUTHORIZATION_CODE_FROM_USER` with the authorization code you get after successful user authorization.

4. **Exchange Code for Token**:
   - Afterward, you can send a request to exchange the obtained authorization code for an **access token**.

## Code Description:

1. First, we define the main parameters:
   - **REST_API_KEY**: Your API key from Kakao Developers.
   - **REDIRECT_URI**: The URI to which the user will be redirected after authorization.
   - **AUTH_CODE**: The authorization code you receive after the user grants access.

2. We then send a **POST request** to the URL `https://kauth.kakao.com/oauth/token` to exchange the authorization code for the access token.

3. On success, the script will print the received **access token**, which can be used to make requests to the Kakao API.

## Example Response:

```json
{
  "access_token": "your_access_token_here",
  "token_type": "bearer",
  "expires_in": 21599,
  "scope": "account_email"
}
