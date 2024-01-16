# A To-Do List application is a useful project that helps users manage
# and organize their tasks efficiently. This project aims to create a
# command-line or GUI-based application using Python, allowing
# users to create, update, and track their to-do lists


import pickle
import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime

LILAC = "#b1a4de"
PURPLE = '#780aff'
LIGHT_GRAY = '#8b84b8'
DARK_GRAY = '#292929'

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

root = ctk.CTk(fg_color=LILAC)
root.title("ToDo List")
root.geometry('540x570')

main_frame = ctk.CTkFrame(root, corner_radius=10, fg_color=PURPLE)
main_frame.pack(pady=10)
heading_label = ctk.CTkLabel(main_frame, text="ToDo List", font=('Georgia', 25, 'italic'), fg_color=PURPLE,
                             text_color='white')
heading_label.pack()

date_label = ctk.CTkLabel(main_frame, text="                 ", font=('Georgia', 16, 'bold'), text_color='white')
date_label.pack(pady=10, fill=BOTH)
task_list = Listbox(main_frame, font=('Georgia', 15),
                    width=38, height=11,
                    bg='SystemButtonFace',
                    bd=0, fg='#332f4d',

                    highlightthickness=0,
                    selectbackground=LIGHT_GRAY,

                    activestyle='none')

task_list.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
task_list.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)
entry = ctk.CTkEntry(root, width=460, height=35, border_width=1, placeholder_text="Enter a task", text_color=DARK_GRAY,
                     font=('Georgia', 17, 'italic'))
entry.pack(pady=20)

btn_frame = ctk.CTkFrame(root, corner_radius=10, fg_color=LILAC)
btn_frame.pack(pady=20)


def delete_task():
    if messagebox.askyesno("Delete Item", "Are you sure you want to delete this task?"):
        task_list.delete(ANCHOR)


def add_task():
    if entry.get().strip():
        task_list.insert(END, f'◦ {entry.get()}\n\n')
        entry.delete(0, END)


def cross_item():
    index = task_list.curselection()
    if index:
        task_list.itemconfig(index, fg='#878c94')
        task_list.selection_clear(0, END)


def uncross():
    index = task_list.curselection()
    if index:
        task_list.itemconfig(index, fg=DARK_GRAY)
        task_list.selection_clear(0, END)


def delete_cross():
    crossed_items = [index for index in range(task_list.size()) if task_list.itemcget(index, "fg") == '#878c94']
    for index in reversed(crossed_items):
        task_list.delete(index)


def save_list():
    file_name = filedialog.asksaveasfilename(

        initialdir="D:\python projects\CodSoft_Python_Internship\Task1_ToDoList", #change to local path
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        if not file_name.endswith(".dat"):
            file_name = f'{file_name}.dat'

        crossed_items = [index for index in range(task_list.size()) if task_list.itemcget(index, "fg") == LIGHT_GRAY]
        stuff = [task_list.get(index) for index in range(task_list.size()) if index not in crossed_items]

        with open(file_name, 'wb') as output_file:
            pickle.dump(stuff, output_file)


def clear_list():
    task_list.delete(0, END)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="D:\python projects\CodSoft_Python_Internship\Task1_ToDoList",  #change to ur local path
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        task_list.delete(0, END)
        with open(file_name, 'rb') as input_file:
            stuff = pickle.load(input_file)
            for item in stuff:
                task_list.insert(END, item)


menu_to = Menu(root)
root.configure(menu=menu_to)
menu_to.configure(bg="purple")

file_menu = Menu(menu_to, tearoff=False)
menu_to.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

edit_menu = Menu(menu_to, tearoff=False)
menu_to.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cross off", command=cross_item)
edit_menu.add_command(label="Uncross", command=uncross)
edit_menu.add_separator()
edit_menu.add_command(label="Delete Crossed items", command=delete_cross)

delete_button = ctk.CTkButton(btn_frame, text="ADD",
                              fg_color=PURPLE,
                              command=add_task,
                              width=70,
                              height=30,
                              corner_radius=10,
                              font=('Georgia', 18, 'bold'),

                              )
add_button = ctk.CTkButton(btn_frame, text="DELETE", fg_color=PURPLE,
                           command=delete_task,
                           width=40,
                           height=30,
                           corner_radius=10,
                           font=('Georgia', 18, 'bold'),

                           )

add_button.grid(row=0, column=1, padx=20)
delete_button.grid(row=0, column=0)


def update_date_label():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d ')
    date_label.configure(text=f"date: {current_date}")


update_date_label()

root.bind("<Enter>", lambda event: add_task())
root.bind("<Control-d>", lambda event: delete_task())
root.bind("<Control-c>", lambda event: cross_item())
root.bind("<Control-u>", lambda event: uncross())


def main_loop():
    root.after(1000, main_loop)
    update_date_label()


root.mainloop()
