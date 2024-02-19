class Library():
    def __init__(self):
        self.file = open("books.txt", "a+")
        print("books.txt file opened")
        self.books = []

    def __del__(self):
        self.file.close()
        print("books.txt file closed")

    def add(self):
        book_name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        while True:
            release_date = input("Enter the release year of the book: ")
            if release_date.isdigit():  # girilen değer bir tamsayı mı kontrolü
                release_date = int(release_date)
                break
            else:
                print("Please enter a valid integer for release year.")

        
        while True:
            num_pages = input("Enter the number of pages of the book: ")
            if num_pages.isdigit():  # girilen değer bir tamsayı mı kontrolü
                num_pages = int(num_pages)
                break
            else:
                print("Please enter a valid integer for number of pages.")

        book_info = f"{book_name},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        self.file.flush()
        print("Book information added to books.txt")

        self.books.append({
            "book_name": book_name,
            "author": author,
            "release_date": release_date,
            "num_pages": num_pages
        })

    def list_books(self):
        self.file.seek(0)  # Dosyanın başına git
        lines = self.file.read().splitlines()
        if not lines:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for line in lines:
                book_info = line.split(',')
                book_name = book_info[0]
                author = book_info[1]
                print(f"Book Name: {book_name}, Author: {author}")

    def remove_book(self):
        book_title = input("Enter the title of the book to remove: ")

        self.file.seek(0)  # Dosyanın başına git
        lines = self.file.readlines()
        if not lines:
            print("No books available in the library.")
            return

        updated_books = []
        removed = False
        for line in lines:
            book_info = line.split(',')
            if book_info[0] == book_title:
                removed = True
            else:
                updated_books.append(line)

        if not removed:
            print("Book not found in the library.")
            return

        # Dosyayı sıfırla ve güncellenmiş kitapları yeniden yaz
        self.file.seek(0)
        self.file.truncate()  
        self.file.writelines(updated_books)
        
        print("Book removed from books.txt")
        self.file.flush()  # Bufferı boşaltarak hemen dosyaya yaz

# Örnek oluşturuluyor
library = Library()

while True:
    print("\nMenu:")
    print("1. List Book")
    print("2. Add Books")
    print("3. Remove Book")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.list_books()
    elif choice == '2':
        library.add()
    elif choice == '3':
        library.remove_book()
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please enter again.")

