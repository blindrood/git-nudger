from fastapi import FastAPI, Request
from slack_events import app_handler

app = FastAPI()


@app.post("/slack/events")
async def slack_events(req: Request):
    return await app_handler.handle(req)


@app.get("/")
async def root():
    return {"message": "Hello World, the app is running."}
