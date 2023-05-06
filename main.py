from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
from bs4 import BeautifulSoup
import openai
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"), name="static")
templates = Jinja2Templates(directory="templates")
openai.api_key = ""


@app.get("/", response_class=HTMLResponse)
async def get_input(request: Request):
    return templates.TemplateResponse("input.html", {"request": request})


@app.post("/result", response_class=HTMLResponse)
async def show_result(request: Request, url: str = Form(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()

        # GPT-4로 질의하기
        prompt = f"{text}\n이 문제를 c++로 풀어줘. 주석을 추가하고, 핵심 아이디어들도 함께 나열해줘."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # response = await client.post("https://api.openai.com/v1/engines/davinci-codex/completions", json={
        #     "model": "gpt-4",
        #     "prompt": prompt,
        #     "max_tokens": 100,
        #     "n": 1,
        #     "stop": None,
        #     "temperature": 0.8,
        # })
        answer = response['choices'][0]['message']['content']

    return templates.TemplateResponse("result.html", {"request": request, "text": text, "answer": answer})
