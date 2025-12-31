from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates directory
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "greeting": None}
    )


@app.post("/greet", response_class=HTMLResponse)
def greet(request: Request, name: str = Form(...)):
    greeting = f"Hello, {name}! 👋 Welcome to FastAPI."
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "greeting": greeting}
    )
