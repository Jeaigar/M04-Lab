const express = require('express');
const app = express();
app.use(express.json());

let books = [];

// Create a new book
app.post('/books', (req, res) => {
    const book = {
        id: Math.floor(Math.random() * 10000), // random id
        book_name: req.body.book_name,
        author: req.body.author,
        publisher: req.body.publisher
    };
    books.push(book);
    res.status(201).send(book);
});

// Get all books
app.get('/books', (req, res) => {
    res.send(books);
});

// Get a book by id
app.get('/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).send('The book with the given ID was not found.');
    res.send(book);
});

// Update a book
app.put('/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).send('The book with the given ID was not found.');

    book.book_name = req.body.book_name;
    book.author = req.body.author;
    book.publisher = req.body.publisher;

    res.send(book);
});

// Delete a book
app.delete('/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).send('The book with the given ID was not found.');

    const index = books.indexOf(book);
    books.splice(index, 1);

    res.send(book);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}...`));
