import asyncio
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
import requests
import openai

app = FastAPI()
templates = Jinja2Templates(directory="templates")
openai.api_key = "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"


@app.get("/", response_class=HTMLResponse)
async def input_url(request: Request):
    return templates.TemplateResponse("input.html", {"request": request})


@app.post("/result", response_class=HTMLResponse)
async def show_result(request: Request, url: str = Form(...)):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    # Replace with your actual API key and endpoint
    prompt = f"{text}\n이 문제를 c++로 풀어줘. 주석을 추가하고, 핵심 아이디어들도 함께 나열해줘."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response['choices'][0]['message']['content']

    return templates.TemplateResponse("result.html", {"request": request, "text": text, "answer": answer})


def run_asyncio(app, host='127.0.0.1', port=8000):
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(uvicorn.create_server(
        app, host=host, port=port, log_level='info'))
    loop.run_forever()


if __name__ == "__main__":
    run_asyncio(app)
