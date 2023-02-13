import os
import random
import time
from tkinter import *
from tkinter import messagebox
import keyboard
from data import *
def main():
    root = Tk()

    def place_forget():
        user_name.place_forget()
        user_year.place_forget()
        user_base.place_forget()
        user_join.place_forget()
        user_doin.place_forget()
        text.place_forget()
        data.place_forget()
        continue_.place_forget()
        name_text.place_forget()
        enter.place_forget()
        years_text.place_forget()
        base_text.place_forget()
        join_text.place_forget()
        doing_text.place_forget()

    def data():

        def back():
            root.destroy()
            main()

        place_forget()

        SIZE = 20

        back = Button(text="⬅", font=("Arial", 20, "bold"), command=back,
                      fg="white",
                      bg=b,
                      bd=0,
                      activebackground=b,
                      activeforeground="green")
        back.place(relx=0.9)

        result = Label(text="Результат", font=("Arial", 20, "bold"),
                     fg="white",
                     bg=b)
        result.place(relx=0.2)

        result_data_user_name = Label(text="Ваше имя | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_name.place(rely=0.1)
        result_data_user_years = Label(text="Ваш возраст | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_years.place(rely=0.2)
        result_data_user_base = Label(text="Ваша весовая категория | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_base.place(rely=0.3)
        result_data_user_join = Label(text="Ваша работа | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_join.place(rely=0.4)
        result_data_user_doing = Label(text="Ваша должность | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_doing.place(rely=0.5)

        FOREGROUND = "lime"

        result_data_user_name = Label(text=name, font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,
                                     bg=b)
        result_data_user_name.place(relx=0.35, rely=0.11)
        result_data_user_years = Label(text=years, font=("Arial", SIZE, "bold"),
                                      fg=FOREGROUND,
                                      bg=b)
        result_data_user_years.place(relx=0.43, rely=0.21)
        result_data_user_base = Label(text=base, font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,
                                     bg=b)
        result_data_user_base.place(relx=0.8, rely=0.31)
        result_data_user_join = Label(text=join, font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,
                                     bg=b)
        result_data_user_join.place(relx=0.43, rely=0.41)
        result_data_user_doing = Label(text=doing, font=("Arial", SIZE, "bold"),
                                      fg=FOREGROUND,
                                      bg=b)
        result_data_user_doing.place(relx=0.55, rely=0.51)

    def con():
        def back():
            root.destroy()
            main()

        place_forget()
        SIZE = 20

        back = Button(text="⬅", font=("Arial", SIZE, "bold"), command=back,
                      fg="white",
                      bg=b,
                      bd=0,
                      activebackground=b,
                      activeforeground="green")
        back.place(relx=0.9)

        result = Label(text="Результат", font=("Arial", SIZE, "bold"),
                     fg="white",
                     bg=b)
        result.place(relx=0.2)

        result_data_user_name = Label(text="Ваше имя | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_name.place(rely=0.1)
        result_data_user_years = Label(text="Ваш возраст | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_years.place(rely=0.2)
        result_data_user_base = Label(text="Ваша весовая категория | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_base.place(rely=0.3)
        result_data_user_join = Label(text="Ваша работа | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_join.place(rely=0.4)
        result_data_user_doing = Label(text="Ваша должность | ", font=("Arial", SIZE, "bold"),
                                     fg="#e0a716",
                                     bg=b)
        result_data_user_doing.place(rely=0.5)

        FOREGROUND = "lime"

        result_data_user_name = Label(text=name_SV.get(), font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,
                                     bg=b)
        result_data_user_name.place(relx=0.35, rely=0.11)
        result_data_user_years = Label(text=years_SV.get(), font=("Arial", SIZE, "bold"),
                                      fg=FOREGROUND,
                                      bg=b)
        result_data_user_years.place(relx=0.43, rely=0.21)
        result_data_user_base = Label(text=base_SV.get(), font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,
                                     bg=b)
        result_data_user_base.place(relx=0.8, rely=0.31)
        result_data_user_join = Label(text=join_SV.get(), font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,
                                     bg=b)
        result_data_user_join.place(relx=0.43, rely=0.41)
        result_data_user_doing = Label(text=doing_SV.get(), font=("Arial", SIZE, "bold"),
                                      fg=FOREGROUND,
                                      bg=b)
        result_data_user_doing.place(relx=0.55, rely=0.51)

    def save():
        with open('data.py', 'w', encoding='utf-8') as f:
            f.write('name = "' + name_SV.get() + '"\n' +
                    'years = "' + years_SV.get() + '"\n' +
                    'base = "' + base_SV.get() + '"\n' +
                    'join = "' + join_SV.get() + '"\n' +
                    'doing = "' + doing_SV.get() + '"')

    b = "#121212"
    root["bg"] = "#121212"
    root.geometry("450x400+140+230")
    root.title("                АНКЕТА")
    root.resizable(width=False, height=False)

    data = Button(text="🔙", font=("Arial", 30, "bold"), command=data,
                   fg="white",
                   bg=b,
                   bd=0,
                   activeforeground="lime",
                   activebackground=b)
    data.place(relx=0.7, rely=0.6)

    text = Label(text="Анкета", font=("Arial", 20, "bold"),
                 fg="white",
                 bg=b)
    text.place(relx=0.2)

    name_SV = StringVar()
    years_SV = StringVar()
    base_SV = StringVar()
    join_SV = StringVar()
    doing_SV = StringVar()
    user_name = Entry(textvariable=name_SV, font=("Arial", 10, "bold"), width=40)
    user_year = Entry(textvariable=years_SV, font=("Arial", 10, "bold"), width=40)
    user_base = Entry(textvariable=base_SV, font=("Arial", 10, "bold"), width=40)
    user_join = Entry(textvariable=join_SV, font=("Arial", 10, "bold"), width=40)
    user_doin = Entry(textvariable=doing_SV, font=("Arial", 10, "bold"), width=40)
    user_name.place(rely=0.1, height=30)
    user_year.place(rely=0.2, height=30)
    user_base.place(rely=0.3, height=30)
    user_join.place(rely=0.4, height=30)
    user_doin.place(rely=0.5, height=30)

    name_text = Label(text="имя", font=("Arial", 15, "bold"),
                 fg="white",
                 bg=b)
    name_text.place(relx=0.67, rely=0.1)
    years_text =Label(text="возраст", font=("Arial", 15, "bold"),
                 fg="white",
                 bg=b)
    years_text.place(relx=0.67, rely=0.2)
    base_text = Label(text="вес", font=("Arial", 15, "bold"),
                 fg="white",
                 bg=b)
    base_text.place(relx=0.67, rely=0.3)
    join_text = Label(text="работа", font=("Arial", 15, "bold"),
                 fg="white",
                 bg=b)
    join_text.place(relx=0.67, rely=0.4)
    doing_text =Label(text="должность", font=("Arial", 15, "bold"),
                 fg="white",
                 bg=b)
    doing_text.place(relx=0.67, rely=0.5)

    enter = Button(text="Сохранить", font=("Arial", 30, "bold"), command=save,
                   fg="#09a7b3",
                   bg=b,
                   bd=0,
                   activeforeground="#05949e",
                   activebackground=b)
    enter.place(relx=0.1, rely=0.6)

    continue_ = Button(text="Продолжить", font=("Arial", 15, "bold"), width=37, command=con,
                       fg="white",
                       bg="#d1891d",
                       activeforeground="gray",
                       activebackground="orange",
                       bd=0)
    continue_.place(relx=0.0, rely=0.85, height=70)
    root.mainloop()

if __name__ == '__main__':
    main()