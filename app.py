from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from did import send_to_did 

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserInput(BaseModel):
    text: str

def stub_response_text():
    # This function simulates the response text from a local LLM.
    return """So, Saad Ashraf… we’ve been talking about your ‘anxiety’ and ‘trust issues’ for weeks now, haven’t we? But let’s be honest—when you walk into this office, do you really want to dwell on all that… darkness? Or… do you ever wonder what it’d be like to… shift the dynamic here?"""

@app.post("/chat")
async def chat_with_avatar(data: UserInput):
    message = data.text
    # Call local LLM here and get response_text (mocked for now)
    response_text = stub_response_text()

    # Send to D-ID
    talk_id = await send_to_did(response_text)

    # Always return response_text, add talk_id if successful
    if talk_id:
        return {
            "talk_id": talk_id,
            "response_message": response_text
        }
    else:
        return {
            "error": "Failed to initiate avatar video.",
            "response_message": response_text
        }


