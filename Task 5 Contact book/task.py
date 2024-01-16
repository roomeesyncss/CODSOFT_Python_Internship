import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk


class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.contacts = []

        self.pages = {
            "Add": self.create_add_page,
            "View": self.create_view_page,
            "Search": self.create_search_page
        }

        self.create_navigation_bar()

        self.current_page = None
        self.show_page("Add")

    def create_navigation_bar(self):
        navigation_frame = ttk.Frame(self.master)
        navigation_frame.pack(side="left", fill="y")

        ttk.Label(navigation_frame, text="Navigation", font=("Helvetica", 12)).pack(pady=10)

        for page_name in self.pages.keys():
            ttk.Button(navigation_frame, text=page_name, command=lambda p=page_name: self.show_page(p)).pack(pady=5)

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()

        self.current_page = self.pages[page_name]()
        self.current_page.pack(side="right", fill="both", expand=True)

    def create_add_page(self):
        add_frame = ttk.Frame(self.master)

        ttk.Label(add_frame, text="Add Contact", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(add_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        name_entry = ttk.Entry(add_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(add_frame, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        phone_entry = ttk.Entry(add_frame)
        phone_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(add_frame, text="Email:").grid(row=3, column=0, padx=10, pady=5)
        email_entry = ttk.Entry(add_frame)
        email_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(add_frame, text="Address:").grid(row=4, column=0, padx=10, pady=5)
        address_entry = ttk.Entry(add_frame)
        address_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Button(add_frame, text="Add Contact", command=lambda: self.add_contact(name_entry.get(), phone_entry.get(),
                                                                                   email_entry.get(),
                                                                                   address_entry.get())).grid(row=5,
                                                                                                              column=0,
                                                                                                              columnspan=2,
                                                                                                              pady=10)

        return add_frame

    def create_view_page(self):
        view_frame = ttk.Frame(self.master)

        ttk.Label(view_frame, text="View Contacts", font=("Helvetica", 14)).pack(pady=10)

        if self.contacts:
            result = "\n".join([f"{contact.name}: {contact.phone_number}" for contact in self.contacts])
        else:
            result = "No contacts available."

        ttk.Label(view_frame, text=result).pack()

        return view_frame

    def create_search_page(self):
        search_frame = ttk.Frame(self.master)

        ttk.Label(search_frame, text="Search Contacts", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2,
                                                                                     pady=10)

        ttk.Label(search_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        name_entry = ttk.Entry(search_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(search_frame, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        phone_entry = ttk.Entry(search_frame)
        phone_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(search_frame, text="Search",
                   command=lambda: self.search_contact(name_entry.get(), phone_entry.get())).grid(row=3, column=0,
                                                                                                  columnspan=2, pady=10)

        return search_frame

    def add_contact(self, name, phone_number, email, address):
        if name and phone_number:
            contact = Contact(name, phone_number, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.show_page("View")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required!")

    def search_contact(self, search_name, search_phone):
        results = [contact for contact in self.contacts
                   if
                   search_name.lower() in contact.name.lower() or search_phone.lower() in contact.phone_number.lower()]

        if results:
            result = "\n".join([f"{contact.name}: {contact.phone_number}" for contact in results])
        else:
            result = "No matching contacts found."

        messagebox.showinfo("Search Results", result)


if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = ContactManagerApp(root)
    root.mainloop()
