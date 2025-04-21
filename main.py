from typing import Union
from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets", StaticFiles(directory="./web/assets"), name="assets")
app.mount("/static", StaticFiles(directory="./web/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("./web/index.html", "r") as f:
        html_content = f.read()
    return html_content


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
