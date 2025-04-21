###用于Nuitka打包,并未在该文件内使用
from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# release: nuitka server.py --onefile
###

import uvicorn


def main():
    uvicorn.run(
        app="main:app",
        host='127.0.0.1',
        port=8000,
        reload=False
    )


if __name__ == "__main__":
    main()
