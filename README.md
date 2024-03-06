## Library Management System

This is a simple library management system implemented in Python. It allows users to add books, list available books, and remove books from the library inventory.

### Features
- **Add Books**: Add new books to the library inventory by providing book name, author, release year, and number of pages.
- **List Books**: View the list of available books in the library.
- **Remove Book**: Remove a book from the library inventory by providing the title of the book.

### Usage
1. **Clone Repository**: Clone this repository to your local machine using the following command:
    ```bash
    git clone <repository_url>
    ```

2. **Navigate to Directory**: Change your current directory to the cloned repository folder:
    ```bash
    cd library-management-system
    ```

3. **Run the Application**: Execute the Python script to run the library management system:
    ```bash
    python library_management_system.py
    ```

4. **Follow the Menu**: Once the application is running, you'll be presented with a menu where you can choose various options:
    - Enter `1` to list available books.
    - Enter `2` to add a new book.
    - Enter `3` to remove a book.
    - Enter `q` to quit the application.

### File Structure
- `books.txt`: This file stores the information of books added to the library. Each line represents a book's details in the format: `book_name,author,release_date,num_pages`.

### Sample Usage
Below is an example of how you can interact with the library management system:

