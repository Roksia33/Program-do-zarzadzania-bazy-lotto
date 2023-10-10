import tkinter as tk
from tkinter import ttk
import mysql.connector

# Funkcja do pobierania ostatnich 20 rekordów w danym typie lotto
def get_last_20_lotto_results():
    lotto_type = lotto_type_var.get()
    query = f"SELECT * FROM lotto_results WHERE lotto_type = '{lotto_type}' ORDER BY id DESC LIMIT 20"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# Funkcja do wyświetlania wyników w oknie
def display_results():
    results_tree.delete(*results_tree.get_children())
    results = get_last_20_lotto_results()
    for row in results:
        results_tree.insert("", "end", values=row[1:])

# Połączenie z bazą danych MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lotto"
)

cursor = db.cursor()

# Tworzenie głównego okna
root = tk.Tk()
root.title("Ostatnie 20 wyników lotto")

# Wybór lotto
label = tk.Label(root, text="Wybierz typ lotto:")
label.pack(pady=10)
lotto_types = ["Ekstra Pensja","Eurojackpot","Keno","Lotto","Mini Lotto","Multi Multi","Szybkie 600"]
lotto_type_var = tk.StringVar()
lotto_type_var.set(lotto_types[0])
lotto_type_menu = ttk.Combobox(root, textvariable=lotto_type_var, values=lotto_types)
lotto_type_menu.pack()

# Przycisk do wyświetlenia wyników
show_results_button = tk.Button(root, text="Pokaż wyniki", command=display_results)
show_results_button.pack(pady=10)

# Tabela wyników
columns = (
    "Lotto Type", "Number 1", "Number 2", "Number 3", "Number 4", "Number 5",
    "Number 6", "Number 7", "Number 8", "Number 9", "Number 10", "e_number 1", "e_number 2"
)
results_tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    results_tree.heading(col,anchor=tk.CENTER, text=col)
    results_tree.column(col,anchor=tk.CENTER, width=80)

results_tree.pack(padx=10, pady=10)

if __name__ == '__main__':
    root.mainloop()

# Zamykanie połączenia z bazą danych
db.close()
