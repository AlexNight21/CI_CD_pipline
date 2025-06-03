from fastapi import FastAPI
import uvicorn

from config import HOST, PORT

app = FastAPI()


@app.get("/")
def check_handler():
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
