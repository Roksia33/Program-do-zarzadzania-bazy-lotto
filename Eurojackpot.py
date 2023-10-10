import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

####### Funkcja odświeżania pól do wpisania liczb #######
def refresh_data():
    for entry_num in number_entries:
        entry_num.delete(0, tk.END)

    for entry_e_num in e_number_entry:
        entry_e_num.delete(0, tk.END)

    entry_date.delete(0, tk.END)
    option_time.delete(0, tk.END)

####### Funkcja, która zapyta o wyjście z programu #######
def exit_program():
    result = messagebox.askquestion("Wyjście", "Czy na pewno chcesz wyjść z programu?")
    if result == "yes":
        root.quit()

####### Funkcja obsługująca zapis danych do bazy MySQL #######
def save_to_database():
    try:
        # Pobieranie danych z pól tekstowych
        lotto_type = lotto_type_entry.get()
        numbers = [number_entries[i].get() for i in range(5)]
        e_numbers = [e_number_entry[i].get() for i in range(2)]
        date = entry_date.get()
        time = option_time.get()

        # Łączenie się z bazą danych MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lotto"
        )
        cursor = conn.cursor()

        # Wstawianie danych do tabeli
        cursor.execute("INSERT INTO lotto_results (lotto_type, number1, number2, number3, number4, number5, e_number1, e_number2, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (lotto_type, *numbers, *e_numbers, date, time))
        
        # Zatwierdzanie zmian i zamykanie połączenia
        conn.commit()
        conn.close()

        messagebox.showinfo("Sukces", "Dane zostały zapisane do bazy danych!")

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")

# Tworzenie okna
root = tk.Tk()
root.title("Eurojackpot")
root.geometry("900x280")
root.resizable(False,False)

# Tworzenie etykiet i pól tekstowych dla danych
label = tk.Label(root, text="", font=("Helvetica", 19)).grid(row=0, column=3)
tk.Label(root, text="Typ lotto:", font=("Helvetica", 14)).grid(row=1, column=0)
lotto_type_var = tk.StringVar()
lotto_type_var.set("Eurojackpot")
lotto_type_entry = tk.Entry(root, textvariable=lotto_type_var)
lotto_type_entry.config(state='disabled')
lotto_type_entry.grid(row=1, column=1)

tk.Label(root, text="Liczby (1-50):", font=("Helvetica", 14)).grid(row=2, column=0)
number_entries = []
for i in range(5):
    entry = tk.Entry(root)
    entry.grid(row=2, column=i+1)
    number_entries.append(entry)

tk.Label(root, text="Liczby dodatkowe (1-12):", font=("Helvetica", 14)).grid(row=3, column=0)
e_number_entry = []
for i in range(2):
    e_number_entry1 = tk.Entry(root)
    e_number_entry1.grid(row=3, column=i+1)
    e_number_entry.append(e_number_entry1)
    
# Etykieta wybierania daty
data_label = tk.Label(root, text="Wpisz datę (RRRR-MM-DD):", font=("Helvetica", 14))
data_label.grid(row=4, column=0)
label = tk.Label(root, text="", font=("Helvetica", 19)).grid(row=6, column=3)

# Pole do wprowadzania daty
entry_date = tk.Entry(root)
entry_date.grid(row=4, column=1)

# Etykieta wybierania godziny
godzina_label = tk.Label(root, text="Wybierz godzinę:", font=("Helvetica", 14))
godzina_label.grid(row=5, column=0)

# Lista opcji dla godziny
godziny = ["20:00"]
option_time = ttk.Combobox(root, values=godziny)
option_time.grid(row=5, column=1)

# Przyciski do zapisu danych, wyjścia z programu oraz resetowania pól do wpisania liczb.
label1 = tk.Label(root, text="", font=("Helvetica", 10)).grid(row=6, column=3)
button_refresh = tk.Button(root, text="Resetuj", height = 2, width = 10, bg='#e0c05f', command=refresh_data, font=("Helvetica", 10))
button_refresh.grid(row=7, column=1)
save_button = tk.Button(root, text="Zapisz",height = 2, width = 10, bg='#e0c05f', command=save_to_database, font=("Helvetica", 10))
save_button.grid(row=7, column=2)
button_exit = tk.Button(root, text="Wyjście",height = 2, width = 10, bg='#e0c05f', command=exit_program, font=("Helvetica", 10))
button_exit.grid(row=7, column=3)

root.protocol("WM_DELETE_WINDOW", exit_program)

if __name__ == '__main__':
    root.mainloop()
