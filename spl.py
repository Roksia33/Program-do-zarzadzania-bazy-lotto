import tkinter as tk
import mysql.connector

def check_lotto_results():
    # Pobieranie wartości wprowadzone przez użytkownika
    num_records = int(records_entry.get())
    lotto_type = lotto_type_entry.get()

    # Połącznie się z bazą danych MySQL
    connection = mysql.connector.connect(
        host="localhost",  # Zmienić na adres hosta bazy danych
        user="root",       # Zmienić na nazwę użytkownika bazy danych
        password="",  # Zmienić na hasło użytkownika bazy danych
        database="lotto"  # Zmienić na nazwę bazy danych
    )

    # Tworzenie kursoru do wykonywania zapytań SQL
    cursor = connection.cursor()

    # Zapytanie SQL do pobrania ostatnich rekordów dla danego typu lotto
    query = f"SELECT * FROM lotto_results WHERE lotto_type = '{lotto_type}' ORDER BY id DESC LIMIT {num_records}"
    cursor.execute(query)

    # Pobieranie wyników zapytania
    results = cursor.fetchall()

    # Liczenie ilości powtarzających się liczb
    number_counts = {}
    for row in results:
        for i in range(1, 13):
            number = row[i]
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1

    # Wyświetlanie wyników w oknie
    result_text.delete(1.0, tk.END)
    for number, count in number_counts.items():
        result_text.insert(tk.END, f"Liczba {number}: {count} razy\n")

    # Zamknie połączenia z bazą danych
    connection.close()

# tworzenie głównego okna
window = tk.Tk()
window.title("")
window.geometry("400x700")
window.resizable(False,False)

# Etykieta i pola tekstowe

records_label = tk.Label(window, text="Ilość rekordów:", font=("Helvetica", 14))
records_label.pack(pady=20)
records_entry = tk.Entry(window)
records_entry.pack()

lotto_type_label = tk.Label(window, text="Typ Lotto:", font=("Helvetica", 14))
lotto_type_label.pack(pady=20)
lotto_type_entry = tk.Entry(window)
lotto_type_entry.pack()

# Przycisk do sprawdzenia wyników oraz wyjścia z programu
check_button = tk.Button(window, text="Sprawdź wyniki",height = 2, width = 13, bg='#ffb92d', command=check_lotto_results, font=("Helvetica", 10))
check_button.pack(pady=20)

button_exit = tk.Button(window, text="Wyjście",height = 2, width = 13, bg='#ffb92d', command=window.quit, font=("Helvetica", 10))
button_exit.pack(pady=5)

# Pole tekstowe do wyświetlania wyników
result_text = tk.Text(window, height=20, width=40)
result_text.pack(pady=10)

if __name__ == '__main__':
    window.mainloop()
