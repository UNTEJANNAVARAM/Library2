fetch("/books")
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById("books-list");
    data.forEach(book => {
      const item = document.createElement("li");
      item.textContent = `${book.title} by ${book.author} (${book.year_published})`;
      list.appendChild(item);
    });
  })
  .catch(error => {
    console.error("Error fetching books:", error);
  });
