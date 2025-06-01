from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pathlib

app = FastAPI()

# Mount the 'static' directory to serve CSS and HTML
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Read the index.html content and return it
    index_path = pathlib.Path("static/index.html")
    return index_path.read_text(encoding="utf-8")

@app.get("/books")
async def get_books():
    return [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
        {"title": "1984", "author": "George Orwell", "year_published": 1949},
        {"title": "శ్రీశ్రీ కవితలు", "author": "Sri Sri", "year_published": 1960},
        {"title": "మహాభారతం", "author": "Vyasa", "year_published": -400}
    ]
