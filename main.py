from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_home():
    return FileResponse("index.html")

@app.get("/style.css")
def get_css():
    return FileResponse("style.css", media_type="text/css")

@app.get("/script.js")
def get_js():
    return FileResponse("script.js", media_type="application/javascript")

@app.get("/books")
def get_books():
    return [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
        {"title": "1984", "author": "George Orwell", "year_published": 1949},
        {"title": "శ్రీశ్రీ కవితలు", "author": "Sri Sri", "year_published": 1960},
        {"title": "మహాభారతం", "author": "Vyasa", "year_published": -400},
    ]
