// Display books
fetch("/books")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("books-list");
    data.forEach((book, index) => {
      const li = document.createElement("li");
      li.textContent = `Book ID: ${index} - ${book.title} by ${book.author}`;
      list.appendChild(li);
    });
  });

// Borrow form logic
document.getElementById("borrowForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const memberId = document.getElementById("memberId").value;
  const bookId = document.getElementById("bookId").value;

  fetch("/borrow", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ member_id: memberId, book_id: bookId })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("borrowMessage").textContent = data.message;
    })
    .catch(err => {
      document.getElementById("borrowMessage").textContent = "Error borrowing book.";
      console.error("Error:", err);
    });
});
