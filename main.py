import tkinter as tk
from tkinter import NO, W, ttk
import datetime
import mysql.connector
import subprocess

####### funkcja do wyśrodkowania głównego okna #######
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

####### tworzenie głównego okna #######
root = tk.Tk()
root.title("Aplikacja do zarządzania bazą Lotto")
window_width = 800
window_height = 940
center_window(root, window_width, window_height)
root.resizable(False,False)

# Funkcja do sprawdzania statusu bazy danych MySQL
def sprawdz_status_bazy():
    try:
        # Nawiązujemy połączenie z bazą danych
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )

        # Tworzymy kursor
        cursor = conn.cursor()

        # Wykonujemy polecenie SQL, aby sprawdzić status bazy
        cursor.execute("SELECT 1")

        # Jeśli wykonanie powyższego polecenia nie wygenerowało błędu,
        # to baza danych jest włączona
        status_label.config(text="włączona", fg="green")
    except mysql.connector.Error as err:
        # Jeśli pojawił się błąd, baza danych jest wyłączona
        status_label.config(text="wyłączona!", fg="red")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

####### Lotto #######
def Lotto():
    subprocess.Popen(["python", "Lotto.py"])

####### Eurojackpot #######
def Eurojackpot():
    subprocess.Popen(["python", "Eurojackpot.py"])

####### Keno #######
def Keno():
    subprocess.Popen(["python", "Keno.py"])

####### Szybkie 600 #######
def Szybkie_600():
    subprocess.Popen(["python", "Szybkie_600.py"])

####### Multi Multi #######
def Multi_Multi():
    subprocess.Popen(["python", "Multi_multi.py"])

####### Ekstra Pensja #######
def Ekstra_Pensja():
    subprocess.Popen(["python", "Ekstra_pensja.py"])

####### Mini Lotto #######
def Mini_Lotto():
    subprocess.Popen(["python", "Mini_lotto.py"])

####### Funkcja do wyświetlania aktualnej godziny i daty na pierwszej zakładce #######
def display_time_date():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d-%m-%Y")
    label_time_date.config(text=f"Aktualna godzina: {current_time}\nAktualna data: {current_date}")
    root.after(1000, display_time_date)

####### Funkcja do wyświetlania powtarzających się liczb #######
def check_duplicates():
    subprocess.Popen(["python", "LA.py"])

####### Funkcja do modyfikacji tabeli w bazie danych #######
def update_database():
    subprocess.Popen(["python", "zmiana_danych.py"])

####### Funkcja do wyświetlania tabeli w bazie danych #######
def show_database_window():
     # Połączenie z bazą danych MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lotto"
    )

    mycursor = mydb.cursor()

    # Pobieranie danych z bazy
    mycursor.execute("SELECT * FROM lotto_results")

    # Tworzenie nowego okna
    database_window = tk.Toplevel(root)
    database_window.title("")
    database_window.geometry("1300x600")
    database_window.resizable(False,False)

    # Tworzenie tabelki do wyświetlenia danych z bazy
    tree = ttk.Treeview(database_window, columns=list(range(len(mycursor.column_names))), show="headings")
    
    # Ustalanie nagłówków kolumn
    for i, col_name in enumerate(mycursor.column_names):
        tree.column(i,anchor=tk.CENTER,width=80)
        tree.heading(i, text=col_name)
    
    # Wyświetlanie danych
    for row in mycursor.fetchall():
        tree.insert("", "end", values=row)

    tree.pack(fill="both", expand=True)

####### Funkcja do sprawdzania ilości rekordów w bazie danych #######
def check_records():
    subprocess.Popen(["python", "Slr.py"])

####### Funkcja do wyświetlania ostatnich powtarzających się liczb w bazie danych #######
def check_l():
    subprocess.Popen(["python", "spl.py"])

####### Zakładki #######
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

####### Zakładka 1: Ekran startowy #######
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Strona główna")

label_text= tk.Label(tab1, text="˃Statusu bazy danych MySQL: ", font=("Helvetica", 15))
label_text.place(x=7,y=10)
status_label = tk.Label(tab1, text="Sprawdzanie statusu...", fg="blue", font=("Helvetica", 15))
status_label.place(x=285,y=10)
sprawdz_status_bazy()

label = tk.Label(tab1, text="Witaj w bazie Lotto!", font=("Helvetica", 25))
label.pack(pady=80)
label_time_date = tk.Label(tab1, text="", font=("Helvetica", 16))
label_time_date.pack(pady=20)

display_time_date()

image = tk.PhotoImage(file=r"lotto.png")
image_label = tk.Label(tab1, image=image)
image_label.image = image
image_label.pack(pady=20)

V_label = tk.Label(tab1, text="Ver. 1.0.0", font=("Helvetica", 15))
V_label.pack(pady=50)

####### Zakładka 2: Wprowadzanie danych #######
tab2 = tk.Frame(notebook)
label = tk.Label(tab2, text="Wybierz typ Lotto", font=("Helvetica", 25))
label.pack(pady=20)

notebook.add(tab2, text="Dodaj dane")


button_lotto = tk.Button(tab2, text="Lotto", height = 7, width = 20, bg='#3cc6e0', command=Lotto, font=("Helvetica", 16))
button_lotto.place(x=15,y=90)

button_eurojackpot = tk.Button(tab2, text="Eurojackpot", height = 7, width = 20, bg='#e0c05f', command=Eurojackpot, font=("Helvetica", 16))
button_eurojackpot.place(x=275,y=90)

button_keno = tk.Button(tab2, text="Keno", height = 7, width = 20, bg='#fc851a', command=Keno, font=("Helvetica", 16))
button_keno.place(x=535,y=90)

button_szybkie_600 = tk.Button(tab2, text="Szybkie 600", height = 7, width = 20, bg='#f49504', command=Szybkie_600, font=("Helvetica", 16))
button_szybkie_600.place(x=15,y=290)

button_multi_multi = tk.Button(tab2, text="Multi Multi", height = 7, width = 20, bg='#bf22af', command=Multi_Multi, font=("Helvetica", 16))
button_multi_multi.place(x=275,y=290)

button_ekstra_pensja = tk.Button(tab2, text="Ekstra Pensja", height = 7, width = 20, bg='#6aad32', command=Ekstra_Pensja, font=("Helvetica", 16))
button_ekstra_pensja.place(x=535,y=290)

button_mini_lotto = tk.Button(tab2, text="Mini Lotto", height = 7, width = 20, bg='#fdca51', command=Mini_Lotto, font=("Helvetica", 16))
button_mini_lotto.place(x=275,y=490)


####### Zakładka 3: Zarządzanie bazą #######
tab3 = tk.Frame(notebook)
notebook.add(tab3, text="Zarządzanie bazą")
label = tk.Label(tab3, text="Zarządzaj bazą", font=("Helvetica", 25))
label.pack(pady=20)

button_check_duplicates = tk.Button(tab3, text="Sprawdź powtórzenia", height = 3, width = 25, bg='#ffb92d', command=check_duplicates, font=("Helvetica", 16))
button_check_duplicates.pack(pady=10)

button_check_l = tk.Button(tab3, text="Sprawdź ostatnie powtórzenia", height = 3, width = 25, bg='#ffb92d', command=check_l, font=("Helvetica", 16))
button_check_l.pack(pady=10)

button_check_records = tk.Button(tab3, text="Sprawdź liczbę rekordów", height = 3, width = 25, bg='#ffb92d', command=check_records, font=("Helvetica", 16))
button_check_records.pack(pady=10)


button_update = tk.Button(tab3, text="Zmień dane", height = 3, width = 25, bg='#ffb92d', command=update_database, font=("Helvetica", 16))
button_update.pack(pady=10)

open_database_button = tk.Button(tab3, text="Otwórz bazę danych", height = 3, width = 25, bg='#ffb92d', command=show_database_window, font=("Helvetica", 16))
open_database_button.pack(pady=10)


####### Zakładka 4: Menu #######
tab4 = tk.Frame(notebook)
notebook.add(tab4, text="Menu")

label = tk.Label(tab4, text="Menu", font=("Helvetica", 25))
label.pack(pady=20)

button_exit = tk.Button(tab4, text="Wyjście",height = 3, width = 25, bg='#ffb92d', command=root.quit, font=("Helvetica", 16))
button_exit.pack(pady=10)

####### Uruchomienie aplikacji #######
if __name__ == '__main__':
    root.mainloop()