import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

# Ensure OAuth variables are set
github_client_id = os.getenv("GITHUB_CLIENT_ID")
github_client_secret = os.getenv("GITHUB_CLIENT_SECRET")

if not github_client_id or not github_client_secret:
    raise ValueError("❌ Missing GITHUB_CLIENT_ID or GITHUB_CLIENT_SECRET in environment variables!")

# Load Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("❌ Missing GEMINI_API_KEY!")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    """Handle the OAuth callback from the provider."""
    print(f"✅ Provider ID: {provider_id}")
    print(f"✅ Token Received: {token}")
    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user.session.set("history", [])
    await cl.Message(content="Hello! I am a chatbot").send()
