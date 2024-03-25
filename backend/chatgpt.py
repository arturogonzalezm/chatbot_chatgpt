import asyncio
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Streamlit Chat")


async def get_response(prompt: str) -> str:
    chat_completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4-turbo-preview",
    )
    return chat_completion.choices[0].message.content


# def get_gpt_response(prompt: str) -> str:
#     return asyncio.run(get_response(prompt))

def get_gpt_response(prompt: str) -> str:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(get_response(prompt))
    loop.close()
    return response
