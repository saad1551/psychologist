import httpx

def send_message(message: str) -> str:
    url = "http://localhost:3001/llm"
    params = {"message": message}

    try:
        response = httpx.post(url, params=params)
        response.raise_for_status()
        return response.json().get("message", "")
    except httpx.HTTPError as e:
        print(f"Request failed: {e}")
        return ""

