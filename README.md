# Library Management System API

This is a simple project for managing books in a library using Python and Flask. It allows you to add, update, delete, and search for books.

---

## (a) How to Run the Project

### **What You Need**
1. Install Python 3.8 or later on your computer.
2. Use Postman or any tool to test the API (optional, but recommended).

### **Steps to Run the Project**
1. **Download the Project:**
   - Download or clone the project files to your computer.
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Flask:**
   - Open your terminal and run:
   ```bash
   pip install flask
   ```

3. **Start the Server:**
   - Run the app with:
   ```bash
   python app.py
   ```
   - The server will start running on `http://127.0.0.1:5000/`.

4. **Test the API Endpoints:**
   - Use Postman or your browser to test the different features.

   | Method | URL                       | What It Does           |
   |--------|---------------------------|------------------------|
   | GET    | `/books`                 | Shows all books        |
   | POST   | `/books`                 | Adds a new book        |
   | PUT    | `/books/<book_id>`       | Updates a book         |
   | DELETE | `/books/<book_id>`       | Deletes a book         |
   | GET    | `/books/search`          | Searches for books     |

5. **Example Request:**
   - To add a book, send this JSON in Postman:
   ```json
   {
       "title": "The Great Gatsby",
       "author": "F. Scott Fitzgerald"
   }
   ```

---

## (b) Why It Is Designed This Way

1. **Simple Design:**
   - The project is small and easy to understand.
   - It uses a Python dictionary to store book data.

2. **RESTful API:**
   - Each feature (like adding or deleting books) has its own URL.
   - It uses standard HTTP methods like GET, POST, PUT, and DELETE.

3. **Search Feature:**
   - You can search for books by title or author.
   - This is done using query parameters (e.g., `?title=great`).

---

## (c) Assumptions and Limitations

### **Assumptions**
1. **Unique Titles:**
   - Each book title should be unique to avoid confusion.

2. **Correct Data Format:**
   - When adding or updating a book, it’s expected that the data is sent in the correct JSON format.

### **Limitations**
1. **No Database:**
   - The project uses an in-memory dictionary, so data will be lost when the server stops.
   - To keep data permanently, a database like SQLite or MySQL is needed.

2. **Small Scale:**
   - This is just a basic project for learning purposes and not suitable for large libraries.

3. **Manual Testing:**
   - You need to use Postman or similar tools to manually test the API.

---

