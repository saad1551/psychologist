import httpx
import os
from dotenv import load_dotenv

load_dotenv()

DID_API_USERNAME = os.getenv("AVATAR_API_USERNAME")  # or hardcode for now
DID_API_PASSWORD = os.getenv("AVATAR_API_PASSWORD")  # or hardcode for now

async def send_to_did(message: str):
    url = "https://api.d-id.com/talks"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    payload = {
        "source_url": "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg",
        "script": {
            "type": "text",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "Sara"
            },
            "input": message,
            "ssml": "false"
        },
        "driver_url": "bank://lively"  # or use your preferred driver
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers, auth=(DID_API_USERNAME, DID_API_PASSWORD))

    if response.status_code == 200 or response.status_code == 201:
        result = response.json()
        return result["id"]  # You’ll use this ID for polling GET from frontend
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

