import httpx
import os

DID_API_KEY = os.getenv("AVATAR_API_KEY")  # or hardcode for now

async def send_to_did(message: str):
    url = "https://api.d-id.com/talks"

    headers = {
        "Authorization": f"Bearer {DID_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "script": {
            "type": "text",
            "input": message,
            "provider": {"type": "microsoft", "voice_id": "en-US-JennyNeural"},
            "ssml": False
        },
        "driver_url": "bank://lively"  # or use your preferred driver
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        result = response.json()
        return result["id"]  # You’ll use this ID for polling GET from frontend
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

