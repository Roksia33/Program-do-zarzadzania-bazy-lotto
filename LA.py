import tkinter as tk
from tkinter import ttk
import mysql.connector

# Funkcja do zliczania i wyświetlania powtarzających się liczb
def count_and_display():
    lotto_type = lotto_type_entry.get()
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lotto"
        )
        cursor = conn.cursor()

        # Zapytanie do bazy danych
        query = f"SELECT number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11, number12 FROM lotto_results WHERE lotto_type = '{lotto_type}'"
        cursor.execute(query)

        # Pobieranie wyników zapytania
        results = cursor.fetchall()
        
        # Inicjalizacja słownika do zliczania liczby wystąpień każdej liczby
        number_counts = {}
        for row in results:
            for number in row:
                if number in number_counts:
                    number_counts[number] += 1
                else:
                    number_counts[number] = 1
        
        # Sortowanie wyników oraz wybranie top 5 powtarzających się licb
        top_5 = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)[:5]

        # Czyszczenie tekstu na etykiecie wyników
        results_label.config(text="")

        # Wyświetlanie wyników
        for number, count in top_5:
            results_label.config(text=results_label.cget("text") + f"Liczba {number}: {count} razy\n", font=("Helvetica", 14))

        conn.close()
    except mysql.connector.Error as err:
        print(f"Błąd bazy danych: {err}")

# Tworzenie głównego okna
root = tk.Tk()
root.title("")
root.geometry("400x600")
root.resizable(False,False)

# Etykieta i pole tekstowe dla rodzaju lotto
lotto_type_label = tk.Label(root, text="Wpisz rodzaj Lotto:", font=("Helvetica", 20))
lotto_type_label.pack(pady=40)
lotto_type_entry = tk.Entry(root)
lotto_type_entry.pack(pady=20)

# Przycisk do analizy i wyświetlania wyników oraz przycisk wyjścia z programu
analyze_button = tk.Button(root, text="Analizuj",height = 2, width = 10, bg='#ffb92d', command=count_and_display, font=("Helvetica", 13))
analyze_button.pack(pady=15)

button_exit = tk.Button(root, text="Wyjście",height = 2, width = 10, bg='#ffb92d', command=root.quit, font=("Helvetica", 13))
button_exit.pack(pady=10)

# Etykieta wyników
results_label = tk.Label(root, text="", justify="left")
results_label.pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    root.mainloop()
