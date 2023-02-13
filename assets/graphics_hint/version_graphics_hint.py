import os
import random
import time
from tkinter import *
from tkinter import messagebox
open("data.py", "a")
from data import *
def main():  # ГЛАВНЫЙ ЦИКЛ который запускает программу
    root = Tk()  #  СОЗДАНИЕ ГЛАВЫ ROOT

    def place_forget():
        user_name.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        user_year.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        user_base.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        user_join.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        user_doin.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        text.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        data.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        continue_.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        name_text.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        enter.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        years_text.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        base_text.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        join_text.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ
        doing_text.place_forget()  #  УДАЛЯЕТ ЭЛЕМЕНТ

    def data():

        def back():
            root.destroy()
            main()

        place_forget()  #  ВЫЗЫВАЕТ ДЕФ place_faorget

        SIZE = 20  # ПАЗМЕР ВСЕХ ШРИФТОВ

        back = Button(text="⬅", font=("Arial", 20, "bold"), command=back,  # СОЗДАЕТ КНОПКУ ПЕРЕКИДЫВАЮЩУЮ НА ГЛАВНУЮ СТРАНИЦУ!
                      fg="white",  # ВЫСТАВЛЯЕТ БЕЛЫЙ ЦВЕТ ТЕКСТА
                      bg=b,  # ДЕФОЛТНЫЙ ЦВЕТ ФОНА КНОПКИ
                      bd=0,  # УБИРАЕТ РАМКИ КНОПКИ
                      activebackground=b,  # НЕ МЕНЯЕТ ФОН КНОПКИ ПРИ АКТИВАЦИИ
                      activeforeground="green")  # МЕНЯЕТ ЦВЕТ ТЕКСТА КНОПКИ ПРИ АКТИВАИИ
        back.place(relx=0.9)  # ПОЗИЦИАНИРУЕТ КНОПКУ

        result = Label(text="Результат", font=("Arial", 20, "bold"),  # ОКНО С ТЕКСИРМ
                     fg="white",  # МННЯЕТ ЦВЕТ ТЕКСТА НА БЕЛЫЙ
                     bg=b)  # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result.place(relx=0.2)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО

        result_data_user_name = Label(text="Ваше имя | ", font=("Arial", SIZE, "bold"),  # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",  # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)  # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_name.place(rely=0.1)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_years = Label(text="Ваш возраст | ", font=("Arial", SIZE, "bold"),  # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",  # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)  # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_years.place(rely=0.2)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_base = Label(text="Ваша весовая категория | ", font=("Arial", SIZE, "bold"),  # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",  # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)  # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_base.place(rely=0.3)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_join = Label(text="Ваша работа | ", font=("Arial", SIZE, "bold"),  # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",  # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
                                     bg=b)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_join.place(rely=0.4)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_doing = Label(text="Ваша должность | ", font=("Arial", SIZE, "bold"),  # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",  # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)  # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_doing.place(rely=0.5)  # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        FOREGROUND = "lime"  # ЗАДАЕТ ОБЩИЙ ЦВЕТ ТЕКСТА

        result_data_user_name = Label(text=name, font=("Arial", SIZE, "bold"),
                                     fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_name.place(relx=0.35, rely=0.11)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_years = Label(text=years, font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                      fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                      bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_years.place(relx=0.43, rely=0.21)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_base = Label(text=base, font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_base.place(relx=0.8, rely=0.31)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_join = Label(text=join, font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_join.place(relx=0.43, rely=0.41)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_doing = Label(text=doing, font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                      fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                      bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_doing.place(relx=0.55, rely=0.51)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО

    def con():
        def back():  #  ПЕРЕНОСИТ НА ГЛАВНУЮ СТРАНИЦУ
            root.destroy()  #  ПЕРЕНОСИТ НА ГЛАВНУЮ СТРАНИЦУ
            main()  #  ПЕРЕНОСИТ НА ГЛАВНУЮ СТРАНИЦУ

        place_forget()  #  УМЕНЬШАЕТ МЕСТО ПУТЕМ ДЕФА
        SIZE = 20  # ЗАДАЕТ ОБЩИЙ РАЗМЕР ШРИФТА
        back = Button(text="⬅", font=("Arial", SIZE, "bold"), command=back,  # СОЗДАЕТ КНОПКУ КОТОРАЯ ПЕРЕКИДЫВАЕТ НА ГЛАВНЫЙ ЭКРАН
                      fg="white",  # МЕНЯЕТ ЦВЕТ ТЕКСТА НА БЕЛЫЙ
                      bg=b,  #  СТАВИТ ДЕФОЛТНЫЙ ФОН КНОПКИ
                      bd=0,  #  УБИРАЕТ РАМКИ КНОПКИ
                      activebackground=b,  #  НЕ МЕНЯЕТ ЦВЕТ ФОНА КНОПКИ ПРИ АКТИВАЦИИ
                      activeforeground="green")  #  МЕНЯЕТ ЦВЕТ ТЕКСТА КОНПКИ ПРИ АКТИВАЦИИ
        back.place(relx=0.9)  #  ПОЗИЦИАНИРУЕТ КНОПКУ

        result = Label(text="Результат", font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                     fg="white",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result.place(relx=0.2)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО

        result_data_user_name = Label(text="Ваше имя | ", font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_name.place(rely=0.1)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_years = Label(text="Ваш возраст | ", font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_years.place(rely=0.2)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_base = Label(text="Ваша весовая категория | ", font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_base.place(rely=0.3)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_join = Label(text="Ваша работа | ", font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_join.place(rely=0.4)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_doing = Label(text="Ваша должность | ", font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg="#e0a716",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_doing.place(rely=0.5)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО

        FOREGROUND = "lime"  #  ЗАДАЕТ ОЮЩИЙ ЦВЕТ ТЕКСТА

        result_data_user_name = Label(text=name_SV.get(), font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_name.place(relx=0.35, rely=0.11)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_years = Label(text=years_SV.get(), font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                      fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                      bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_years.place(relx=0.43, rely=0.21)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_base = Label(text=base_SV.get(), font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_base.place(relx=0.8, rely=0.31)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_join = Label(text=join_SV.get(), font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                     fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                     bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_join.place(relx=0.43, rely=0.41)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО
        result_data_user_doing = Label(text=doing_SV.get(), font=("Arial", SIZE, "bold"),    # ОКНО С ТЕКСИРМ
                                      fg=FOREGROUND,    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                                      bg=b)    # СТАВИТ ДЕФОЛТНЫЙ ЦВЕТ ФОНА ТЕКСТАОВОГО ОКНА
        result_data_user_doing.place(relx=0.55, rely=0.51)    # ПОЗИЦИАНИРУЕТ ТЕКСТОВОЕ ОКНО

    def save():
        with open('data.py', 'w', encoding='utf-8') as f:  #  СОЗДАЕТ ФАЙЛ data.py
            f.write('name = "' + name_SV.get() + '"\n' +  #  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                    'years = "' + years_SV.get() + '"\n' +  #  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                    'base = "' + base_SV.get() + '"\n' +    #  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                    'join = "' + join_SV.get() + '"\n' +    #  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                    'doing = "' + doing_SV.get() + '"') #  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ

    b = "#121212"  #  ГЛАЫНЙ ЦВЕТ ФОНА
    root["bg"] = "#121212"  # ЦВЕЬ ФОНА САМОГО ОКНА
    root.geometry("450x400+140+230")  #  ПОЗАЦИАНИРОВАНИЕ И РАЗМЕР ОКНА
    root.title("                АНКЕТА")  #  ЗАДАЕТ НАЗВАНИЕ В ВЕРХУ ПРОГРАММЫ
    root.resizable(width=False, height=False)  #  НЕ ДАЕТ ИЗМЕНЯТЬ ОКНО ПО ГАРИЗОНТАЛИ И ВЕРТИКАЛИ

    data = Button(text="🔙", font=("Arial", 30, "bold"), command=data,    # СОЗДАЕТ КНОПКУ КОТОРАЯ ДАЕТ ВВЕСТИ ПОСЛЕДНИЙ РЕЗУЛЬТАТ
                   fg="white",    # МЕНЯЕТ ЦВЕТ ТЕКСТА НА БЕЛЫЙ
                   bg=b,    #  СТАВИТ ДЕФОЛТНЫЙ ФОН КНОПКИ
                   bd=0,    #  УБИРАЕТ РАМКИ КНОПКИ
                   activeforeground="lime",    #  НЕ МЕНЯЕТ ЦВЕТ ФОНА КНОПКИ ПРИ АКТИВАЦИИ
                   activebackground=b)    #  МЕНЯЕТ ЦВЕТ ТЕКСТА КОНПКИ ПРИ АКТИВАЦИИ
    data.place(relx=0.7, rely=0.6)    #  ПОЗИЦИАНИРУЕТ КНОПКУ

    text = Label(text="Анкета", font=("Arial", 20, "bold"),#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 fg="white",#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 bg=b)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    text.place(relx=0.2)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ

    name_SV = StringVar()  #  ЗАДАЕТ ИМЯ ВЫВОДА
    years_SV = StringVar()  #  ЗАДАЕТ ИМЯ ВЫВОДА
    base_SV = StringVar()  #  ЗАДАЕТ ИМЯ ВЫВОДА
    join_SV = StringVar()  #  ЗАДАЕТ ИМЯ ВЫВОДА
    doing_SV = StringVar()  #  ЗАДАЕТ ИМЯ ВЫВОДА
    user_name = Entry(textvariable=name_SV, font=("Arial", 10, "bold"), width=40)  #  ТЕКСОВОЕ ПОЛЕ ВВОДА
    user_year = Entry(textvariable=years_SV, font=("Arial", 10, "bold"), width=40)  #  ТЕКСОВОЕ ПОЛЕ ВВОДА
    user_base = Entry(textvariable=base_SV, font=("Arial", 10, "bold"), width=40)  #  ТЕКСОВОЕ ПОЛЕ ВВОДА
    user_join = Entry(textvariable=join_SV, font=("Arial", 10, "bold"), width=40)  #  ТЕКСОВОЕ ПОЛЕ ВВОДА
    user_doin = Entry(textvariable=doing_SV, font=("Arial", 10, "bold"), width=40)  #  ТЕКСОВОЕ ПОЛЕ ВВОДА
    user_name.place(rely=0.1, height=30)  #  ПОЗИЦИАНИРУЕТ ПОЛЕ ВВОДА
    user_year.place(rely=0.2, height=30)  #  ПОЗИЦИАНИРУЕТ ПОЛЕ ВВОДА
    user_base.place(rely=0.3, height=30)  #  ПОЗИЦИАНИРУЕТ ПОЛЕ ВВОДА
    user_join.place(rely=0.4, height=30)  #  ПОЗИЦИАНИРУЕТ ПОЛЕ ВВОДА
    user_doin.place(rely=0.5, height=30)  #  ПОЗИЦИАНИРУЕТ ПОЛЕ ВВОДА

    name_text = Label(text="имя", font=("Arial", 15, "bold"),#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 fg="white",#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 bg=b)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    name_text.place(relx=0.67, rely=0.1)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    years_text =Label(text="возраст", font=("Arial", 15, "bold"),#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 fg="white",#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 bg=b)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    years_text.place(relx=0.67, rely=0.2)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    base_text = Label(text="вес", font=("Arial", 15, "bold"),#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 fg="white",#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 bg=b)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    base_text.place(relx=0.67, rely=0.3)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    join_text = Label(text="работа", font=("Arial", 15, "bold"),#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 fg="white",#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 bg=b)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    join_text.place(relx=0.67, rely=0.4)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    doing_text =Label(text="должность", font=("Arial", 15, "bold"),#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 fg="white",#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
                 bg=b)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ
    doing_text.place(relx=0.67, rely=0.5)#  ВПИСЫВАЕТ В НЕГО ЗАПИСАННЫЕ ДАННЫЕ

    enter = Button(text="Сохранить", font=("Arial", 30, "bold"), command=save,    # СОЗДАЕТ КНОПКУ КОТОРАЯ СОХРАНАЯЕТ РЕЗУЛЬТАТЫ ВВОДА
                   fg="#09a7b3",    # МЕНЯЕТ ЦВЕТ ТЕКСТА
                   bg=b,    #  СТАВИТ ДЕФОЛТНЫЙ ФОН КНОПКИ
                   bd=0,    #  УБИРАЕТ РАМКИ КНОПКИ
                   activeforeground="#05949e",    #  НЕ МЕНЯЕТ ЦВЕТ ФОНА КНОПКИ ПРИ АКТИВАЦИИ
                   activebackground=b)    #  МЕНЯЕТ ЦВЕТ ТЕКСТА КОНПКИ ПРИ АКТИВАЦИИ
    enter.place(relx=0.1, rely=0.6)    #  ПОЗИЦИАНИРУЕТ КНОПКУ

    continue_ = Button(text="Продолжить", font=("Arial", 15, "bold"), width=37, command=con,    # СОЗДАЕТ КНОПКУ КОТОРАЯ ДАЕТ РЕЗУЛЬТАТЫ ВВОДА
                       fg="white",    # МЕНЯЕТ ЦВЕТ ТЕКСТА НА БЕЛЫЙ
                       bg="#d1891d",    #  СТАВИТ ДЕФОЛТНЫЙ ФОН КНОПКИ
                       activeforeground="gray",    #  УБИРАЕТ РАМКИ КНОПКИ
                       activebackground="orange",    #  НЕ МЕНЯЕТ ЦВЕТ ФОНА КНОПКИ ПРИ АКТИВАЦИИ
                       bd=0)    #  МЕНЯЕТ ЦВЕТ ТЕКСТА КОНПКИ ПРИ АКТИВАЦИИ
    continue_.place(relx=0.0, rely=0.85, height=70)    #  ПОЗИЦИАНИРУЕТ КНОПКУ
    root.mainloop()

if __name__ == '__main__':  # ЗАПУСКАЕТ ПРОГРАММУ
    main()  #  ЗАПУСКАЕТ ДЕФ