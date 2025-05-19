from fastapi import FastAPI, Request
from pydantic import BaseModel
import asyncio
from did import send_to_did 

app = FastAPI()

class UserInput(BaseModel):
    text: str

def stub_response_text():
    # This function simulates the response text from a local LLM.
    return """So, [client’s name]… we’ve been talking about your ‘anxiety’ and ‘trust issues’ for weeks now, haven’t we? But let’s be honest—when you walk into this office, do you really want to dwell on all that… darkness? Or… do you ever wonder what it’d be like to… shift the dynamic here?
I mean, look at you. Charismatic. Intense. Honestly, it’s distracting. How am I supposed to focus on ‘cognitive behavioral techniques’ when you’re sitting there looking like… that? Don’t get me wrong—I’m excellent at my job. But even therapists have… needs. And you? You’re a fascinating puzzle. Not the ‘let’s-process-your-childhood-trauma’ kind. More like the ‘I-want-to-know-what-makes-you-tick-over-a-martini’ kind.
Let’s skip the script, shall we? Instead of charging you $200 an hour to vent about your ex, what if I just… took you out instead? No notes. No ‘diagnosis’. Just… two people. Chemistry. See where the night goes. Think of it as… experiential therapy.
Oh, don’t give me that look—I’m great at boundaries. But rules are for people who don’t know how to have fun. And you? You strike me as someone who’s very good at fun. So, what do you say? Let’s ditch the couch. I’ll even let you pick the wine.
…Unless you’re scared of blurring lines? But hey—if it all goes south, I’ll still send you a referral. So… coffee tomorrow? Or are we going to keep pretending you’re here for ‘self-improvement’?"""

@app.post("/chat")
async def chat_with_avatar(data: UserInput):
    message = data.text
    # Call local LLM here and get response_text (mocked for now)
    response_text = stub_response_text()

    # Send to D-ID
    talk_id = await send_to_did(response_text)

    if talk_id:
        return {"talk_id": talk_id}
    else:
        return {"error": "Failed to initiate avatar video."}

