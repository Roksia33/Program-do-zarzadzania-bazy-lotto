import tkinter as tk
from tkinter import NO, W, ttk
from tkinter import messagebox
import datetime
import mysql.connector


####### Inicjalizacja głównego okna #######
root = tk.Tk()
root.title("Aplikacja Lotto")
root.geometry("800x940")
root.resizable(False,False)

####### Funkcja do wyświetlania aktualnej godziny i daty na pierwszej zakładce #######
def display_time_date():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d-%m-%Y")
    label_time_date.config(text=f"Aktualna godzina: {current_time}\nAktualna data: {current_date}")
    root.after(1000, display_time_date)

####### Funkcja do obsługi zapisywania danych do bazy MySQL #######
def save_to_database():
    # Połączenie z bazą danych
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lotto"
    )
    
    # Sprawdzenie połączenia
    if conn.is_connected():
        cursor = conn.cursor()
        
        # Pobranie danych z pól wprowadzania
        lotto_type = entry_lotto_type.get()
        numbers = [entry_num.get() for entry_num in entry_numbers]
        
        # Zapisanie danych do bazy
        try:
            cursor.execute("INSERT INTO lotto_results (lotto_type, number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11, number12) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (lotto_type,) + tuple(numbers))
            conn.commit()
            messagebox.showinfo("Sukces", "Dane zostały zapisane do bazy danych.")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania danych: {e}")
        
        # Zamknięcie połączenia
        conn.close()

####### Funkcja do odświeżania wprowadzonych danych #######
def refresh_data():
    entry_lotto_type.delete(0, tk.END)
    for entry_num in entry_numbers:
        entry_num.delete(0, tk.END)

####### Funkcja do wyświetlania powtarzających się liczb #######
def check_duplicates():
    
    # Połącz z bazą danych MySQL
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lotto"
    )
    
    cursor = connection.cursor()
    
    # Inicjalizacja słownika do przechowywania wyników
    number_counts = {}
    
    # Pobierz nazwy kolumn w tabeli lotto_results
    cursor.execute("DESCRIBE lotto_results")
    column_names = [row[0] for row in cursor.fetchall()]
    
    # Iteruj przez kolumny z numerami (number1, number2, ..., number12)
    for column_name in column_names:
        if column_name.startswith("number"):
            # Zapytanie SQL do zliczenia wystąpień liczby w danej kolumnie
            query = f"SELECT {column_name}, COUNT(*) as count FROM lotto_results GROUP BY {column_name}"
            cursor.execute(query)
            
            # Pobierz wyniki i zaktualizuj słownik
            results = cursor.fetchall()
            for number, count in results:
                if number in number_counts:
                    number_counts[number] += count
                else:
                    number_counts[number] = count
    
    # Zamknij połączenie z bazą danych
    connection.close()
    
    return number_counts

# Tworzenie okna głównego
check = tk.Toplevel(root)
check.title("Tabela z bazy danych")
check.geometry("1000x600")

# Ustal rozmiar okna
check.geometry("600x700")

# Zlicz wystąpienia liczby
number_counts = check_duplicates()

# Tworzenie etykiety do wyświetlenia wyników
label = tk.Label(check, text="Liczba wystąpień w bazie:")
label.pack()

# Wyświetlenie wyników
for number, count in number_counts.items():
    result_label = tk.Label(check, text=f"Liczba {number}: {count} wystąpień")
    result_label.pack()


####### Funkcja do modyfikacji tabeli w bazie danych #######
def update_database():
    print()

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
    database_window.title("Tabela z bazy danych")
    database_window.geometry("1000x600")

    # Tworzenie tabelki do wyświetlenia danych z bazy
    tree = ttk.Treeview(database_window, columns=list(range(len(mycursor.column_names))), show="headings")
    
    # Ustalanie nagłówków kolumn
    for i, col_name in enumerate(mycursor.column_names):
        tree.column(i,anchor=W,width=70)
        tree.heading(i, text=col_name)
    
    # Wyświetlanie danych
    for row in mycursor.fetchall():
        tree.insert("", "end", values=row)

    tree.pack(fill="both", expand=True)

####### Zakładki #######
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

####### Zakładka 1: Ekran powitania #######
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Strona główna")

label = tk.Label(tab1, text="Witaj w bazie Lotto!", font=("Helvetica", 25))
label.pack(pady=80)
label_time_date = tk.Label(tab1, text="", font=("Helvetica", 16))
label_time_date.pack(pady=20)

display_time_date()

image = tk.PhotoImage(file="lotto.png")
image_label = tk.Label(tab1, image=image)
image_label.image = image
image_label.pack(pady=20)

####### Zakładka 2: Wprowadzanie danych #######
tab2 = tk.Frame(notebook)
label = tk.Label(tab2, text="Wprowadzanie danych Lotto", font=("Helvetica", 18))
label.pack(pady=20)

notebook.add(tab2, text="Wprowadź dane")

label_lotto_type = tk.Label(tab2, text="Typ Lotto:", font=("Helvetica", 14))
label_lotto_type.pack(pady=5)

entry_lotto_type = tk.Entry(tab2)
entry_lotto_type.pack(pady=10)

entry_numbers = []
for i in range(12):
    label = tk.Label(tab2, text=f"Numer {i+1}:", font=("Helvetica", 14))
    label.pack(pady=5)
    entry_num = tk.Entry(tab2)
    entry_num.pack(pady=2)
    entry_numbers.append(entry_num)

button_save = tk.Button(tab2, text="Zapisz do bazy", height = 3, width = 15, bg='#ffb92d', command=save_to_database)
button_refresh = tk.Button(tab2, text="Odśwież", height = 3, width = 15, bg='#ffb92d', command=refresh_data)
button_save.place(x=590, y=100)
button_refresh.place(x=590, y=170)


####### Zakładka 3: Zarządzanie bazą #######
tab3 = tk.Frame(notebook)
notebook.add(tab3, text="Zarządzanie bazą")
label = tk.Label(tab3, text="Zarządzaj bazą", font=("Helvetica", 25))
label.pack(pady=80)

button_check_duplicates = tk.Button(tab3, text="Sprawdź powtórzenia", height = 3, width = 20, bg='#ffb92d', command=check_duplicates, font=("Helvetica", 16))
button_check_duplicates.pack(pady=10)


button_update = tk.Button(tab3, text="Aktualizuj", height = 3, width = 20, bg='#ffb92d', command=update_database, font=("Helvetica", 16))
button_update.pack(pady=10)

open_database_button = tk.Button(tab3, text="Otwórz bazę danych", height = 3, width = 20, bg='#ffb92d', command=show_database_window, font=("Helvetica", 16))
open_database_button.pack(pady=10)


####### Zakładka 4: Wyjście #######
tab4 = tk.Frame(notebook)
notebook.add(tab4, text="Wyjście")

button_exit = tk.Button(tab4, text="Wyjście",height = 30, width = 30, bg='#ffb92d', command=root.quit, font=("Helvetica", 30))
button_exit.pack(pady=400)

####### Uruchomienie aplikacji #######
if __name__ == '__main__':
    root.mainloop()
