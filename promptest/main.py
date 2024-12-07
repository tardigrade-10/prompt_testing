import os, sys
sys.path.append(os.getcwd())

from fastapi import FastAPI
from .api import prompt, manualtests

app = FastAPI()


app.include_router(prompt.router)
app.include_router(manualtests.router)


@app.get("/")
async def root():
    return {"message": "Hello OPENAGENT"}