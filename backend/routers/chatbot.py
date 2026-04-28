from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import google.generativeai as genai

# Configure Gemini with the provided API Key
genai.configure(api_key="AIzaSyAXF290fn0HCoFdoTOkQVSGFQt8wdUnKCE")
model = genai.GenerativeModel('gemini-1.5-flash')

router = APIRouter(
    prefix="/api/chatbot",
    tags=["Chatbot"]
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/ask", response_model=ChatResponse)
async def ask_chatbot(request: ChatRequest):
    user_message = request.message.strip()
    
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
        
    try:
        # Prompt the Gemini AI model
        prompt = f"You are a helpful customer support agent for an E-Commerce store called E-Shop. Keep your answer concise and helpful. The user says: {user_message}"
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        reply = "I'm having trouble connecting to my AI brain at the moment. Please try again later."
        
    return ChatResponse(reply=reply)
