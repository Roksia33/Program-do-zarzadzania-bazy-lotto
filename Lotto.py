import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Funkcja do ukrywania/możliwości wprowadzania liczb
def toggle_entry_state():
    entry_count = int(entry_num_var.get())
    for i, entry in enumerate(number_entries):
        if i < entry_count:
            entry.config(state=tk.NORMAL)
        else:
            entry.delete(0, tk.END)
            entry.config(state=tk.DISABLED)

####### Funkcja odświeżania pól do wpisania liczb #######
def refresh_data():
    for entry_num in number_entries:
        entry_num.delete(0, tk.END)

####### Funkcja obsługująca zapis danych do bazy MySQL #######
def save_to_database():
    try:
        # Pobieranie danych z pól tekstowych
        lotto_type = lotto_type_entry.get()
        numbers = [number_entries[i].get() for i in range(12)]


        # Łączenie się z bazą danych MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lotto"
        )
        cursor = conn.cursor()

        # Wstawianie danych do tabeli
        cursor.execute("INSERT INTO lotto_results (lotto_type, number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11, number12) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (lotto_type, *numbers))
        
        # Zatwierdzanie zmian i zamykanie połączenia
        conn.commit()
        conn.close()

        messagebox.showinfo("Sukces", "Dane zostały zapisane do bazy danych!")

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")

# Tworzenie okna
root = tk.Tk()
root.title("Lotto")
root.geometry("1750x220")
root.resizable(False,False)

# Tworzenie etykiet i pól tekstowych dla danych
label = tk.Label(root, text="", font=("Helvetica", 19)).grid(row=0, column=3)
entry_num_var = tk.StringVar()
num_label = tk.Label(root, text="Podaj ilość typowanych liczb:", font=("Helvetica", 14)).grid(row=2, column=0)
num_entry = tk.Entry(root, textvariable=entry_num_var).grid(row=2, column=1)
apply_button = tk.Button(root, text="Zastosuj", height = 2, width = 10, bg='#3cc6e0', command=toggle_entry_state).grid(row=2, column=2)

label = tk.Label(root, text="", font=("Helvetica", 19)).grid(row=3, column=3)
tk.Label(root, text="Typ lotto:", font=("Helvetica", 14)).grid(row=3, column=0)
lotto_type_var = tk.StringVar()
lotto_type_var.set("Lotto")
lotto_type_entry = tk.Entry(root, textvariable=lotto_type_var)
lotto_type_entry.config(state='disabled')
lotto_type_entry.grid(row=3, column=1)


tk.Label(root, text="Liczby (1-42):", font=("Helvetica", 14)).grid(row=4, column=0)
number_entries = []
for i in range(12):
    entry = tk.Entry(root, state='disabled')
    entry.grid(row=4, column=i+1)
    number_entries.append(entry)

# Przyciski do zapisu danych, wyjścia z programu oraz resetowania pól do wpisania liczb.
label1 = tk.Label(root, text="", font=("Helvetica", 10)).grid(row=6, column=3)
button_refresh = tk.Button(root, text="Resetuj", height = 2, width = 10, bg='#3cc6e0', command=refresh_data, font=("Helvetica", 10))
button_refresh.grid(row=8, column=2)
save_button = tk.Button(root, text="Zapisz",height = 2, width = 10, bg='#3cc6e0', command=save_to_database, font=("Helvetica", 10))
save_button.grid(row=8, column=3)
button_exit = tk.Button(root, text="Wyjście",height = 2, width = 10, bg='#3cc6e0', command=root.quit, font=("Helvetica", 10))
button_exit.grid(row=8, column=4)



root.mainloop()
