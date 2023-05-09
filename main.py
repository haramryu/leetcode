from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
import requests
import openai

app = FastAPI()
templates = Jinja2Templates(directory="templates")
openai.api_key = ""


@app.get("/", response_class=HTMLResponse)
async def input_url(request: Request):
    return templates.TemplateResponse("input.html", {"request": request})


@app.post("/result", response_class=HTMLResponse)
async def show_result(request: Request, url: str = Form(...)):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    # GPT-4로 질의하기
    prompt = f"{text}\n이 문제를 c++로 풀어줘. 주석을 추가하고, 핵심 아이디어들도 함께 나열해줘."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response['choices'][0]['message']['content']

    return templates.TemplateResponse("result.html", {"request": request, "text": text, "answer": answer})
