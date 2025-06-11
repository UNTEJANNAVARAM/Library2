from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS to allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Book list
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
    {"title": "1984", "author": "George Orwell", "year_published": 1949},
    {"title": "శ్రీశ్రీ కవితలు", "author": "Sri Sri", "year_published": 1960},
    {"title": "మహాభారతం", "author": "Vyasa", "year_published": -400},
]

# Serve frontend files
@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/style.css")
def style():
    return FileResponse("style.css", media_type="text/css")

@app.get("/script.js")
def script():
    return FileResponse("script.js", media_type="application/javascript")

# API route for books
@app.get("/books")
def get_books():
    return books

# Pydantic model for borrow form
class BorrowRequest(BaseModel):
    member_id: str
    book_id: str

@app.post("/borrow")
def borrow_book(request: BorrowRequest):
    return {"message": f"Member {request.member_id} borrowed Book {request.book_id} successfully!"}
