import httpx
import os
from dotenv import load_dotenv
from typing import List, Tuple

load_dotenv()

def get_did_api_credentials() -> List[Tuple[str, str]]:
    """
    Parses AVATAR_KEYS env variable into list of (username, password) tuples.
    Format: "user1:pass1,user2:pass2"
    """
    raw_keys = os.getenv("AVATAR_KEYS", "")
    return [tuple(pair.split(":")) for pair in raw_keys.split(",") if ":" in pair]

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
        "driver_url": "bank://lively"
    }

    async with httpx.AsyncClient() as client:
        api_credentials = get_did_api_credentials()
        for username, password in api_credentials:
            try:
                response = await client.post(
                    url,
                    json=payload,
                    headers=headers,
                    auth=(username, password)
                )

                if response.status_code in [200, 201]:
                    result = response.json()
                    return result["id"]

                print(f"Failed with {username}: {response.status_code} - {response.text}")

            except Exception as e:
                print(f"Exception with {username}: {e}")

    print("All credentials failed.")
    return None

