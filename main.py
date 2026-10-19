from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI
app.mount("/view", StaticFiles(directory="view"))

@app.get("/")
def root():
    return RedirectResponse("/view/index.html")

@app.get("/one")
def step_one():
    return{"step":"one"}