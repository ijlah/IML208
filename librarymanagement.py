import tkinter as tk
from tkinter import messagebox

class RegisterLoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RIIZE Library Management System")
        self.geometry("700x400")
        self.config(bg='#504070')
        
        self.staff= []

        # Login labels 
        self.login_label = tk.Label(self.master, text="RIIZE Library Management System", font=( "Playfair Dispair", 16), bg='#504070', fg='white')
        self.login_label.pack()
        self.staff_ID_label = tk.Label(self.master, text="Staff ID", font=("Playfair Dispair", 16), bg='#504070', fg='white')
        self.staff_ID_label.pack()
        self.staff_ID_entry = tk.Entry(self.master, font=("Playfair Dispair", 12))
        self.staff_ID_entry.pack()
        self.password_label = tk.Label(self.master, text="Password", font=("Playfair Dispair", 16), bg='#504070', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Playfair Dispair", 12))
        self.password_entry.pack()
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Playfair Dispair", 12))
        self.login_button.pack()     

    def login(self):
        staff_ID = self.staff_ID_entry.get()
        password = self.password_entry.get()
    
        # Get staff ID and password from the user
        if staff_ID == "2022491592" and password == "icecramellatte1308":
            messagebox.showinfo("Login successful", "Welcome, jeeha!".format(staff_ID))
            self.setup__add_book_page ()
        
        else:
            messagebox.showerror("Login failed", "Incorrect staff ID or password. Please try again.")
            self.staff_ID_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
 
    def setup__add_book_page(self):
        self.login_label.pack_forget()
        self.staff_ID_label.pack_forget()
        self.staff_ID_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()

        staff_ID = self.staff_ID_entry.get()
        self.library_management = LibraryManagement(self, staff_ID)
        

class LibraryManagement:
    def __init__(self, master, staff_id):
        self.master = master
        self.master.title("RIIZE Library Management System")
        self.master.geometry("700x600")
        self.master.config(bg='#504070')
        self.staff_id = staff_id
        
        self.books = []
        self.lend_list = []

        # Labels
        self.login_label = tk.Label(self.master, text="RIIZE Library Management System", font=( "Playfair Dispair", 16), bg='#504070', fg='white')
        self.login_label.pack()
        self.add_book_label = tk.Label(self.master, text="Add Book", font=("Playfair Dispair", 16), bg='#504070', fg='white')
        self.add_book_label.pack()
        self.add_book_entry = tk.Entry(self.master, font=("Playfair Dispair", 12))
        self.add_book_entry.pack()
        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Playfair Dispair", 12))
        self.add_book_button.pack()
        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Playfair Dispair", 16), bg='#504070', fg='white')
        self.remove_book_label.pack()
        self.remove_book_entry = tk.Entry(self.master, font=("Playfair Dispair", 12))
        self.remove_book_entry.pack()
        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book, font=("Playfair Dispair", 12))
        self.remove_book_button.pack()
        self.issue_book_label = tk.Label(self.master, text="Issue Book", font=("Playfair Dispair", 16), bg='#504070', fg='white')
        self.issue_book_label.pack()
        self.issue_book_entry = tk.Entry(self.master, font=("Playfair Dispair", 12))
        self.issue_book_entry.pack()
        self.issue_book_button = tk.Button(self.master, text="Issue Book", command=self.issue_book, font=("Playfair Dispair", 12))
        self.issue_book_button.pack()
        self.view_books_button = tk.Button(self.master, text="View Books", command=self.view_books, font=("Playfair Dispair", 12))
        self.view_books_button.pack()

    def add_book(self):
            book = self.add_book_entry.get()
            self.books.append(book)
            messagebox.showinfo("Success", "Book added successfully")
            self.add_book_entry.delete(0, tk.END)

    def remove_book(self):
            book = self.remove_book_entry.get()
            if book in self.books:
                self.books.remove(book)
                messagebox.showinfo("Success", "Book removed successfully")
            else:
                messagebox.showerror("Error", "Book not found")
            self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
            book = self.issue_book_entry.get()
            if book in self.books:
                self.lend_list.append(book)
                self.books.remove(book)
                messagebox.showinfo("Success", "Book issued successfully")
            else:
                messagebox.showerror("Error", "Book not found")
            self.issue_book_entry.delete(0, tk.END)

    def view_books(self):
            message = "\n".join(self.books)
            messagebox.showinfo("Books", message)

if __name__ == "__main__":
    app = RegisterLoginApp()
    app.mainloop() 
