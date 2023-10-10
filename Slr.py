import tkinter as tk
import mysql.connector

# Funkcja do pobierania informacji z bazy danych MySQL
def get_database_stats():
    # Nawiązanie połączenia z bazą danych
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lotto"
    )

    # Utworzenie kursora
    cursor = connection.cursor()

    # Przykładowe zapytanie SQL do pobrania informacji
    query = "SELECT COUNT(*) FROM lotto_results"

    # Wykonanie zapytania
    cursor.execute(query)

    # Pobranie wyników zapytania
    result = cursor.fetchone()

    # Zamknięcie kursora i połączenia
    cursor.close()
    connection.close()

    # Wyświetlenie informacji w oknie
    stat_label.config(text=f"Liczba rekordów w bazie danych: {result[0]}")

# Tworzenie okna
root = tk.Tk()
root.title("")
root.geometry("500x190")
root.resizable(False,False)

# Tworzenie etykiety do wyświetlenia informacji
stat_label = tk.Label(root, text="", font=("Helvetica", 16))
stat_label.pack(pady=20)

# Przycisk do pobierania informacji oraz wyjścia
get_stats_button = tk.Button(root, text="Uruchom", height = 2, width = 10, bg='#ffb92d', command=get_database_stats, font=("Helvetica", 10))
get_stats_button.pack(pady=5)
button_exit = tk.Button(root, text="Wyjście",height = 2, width = 10, bg='#ffb92d', command=root.quit, font=("Helvetica", 10))
button_exit.pack(pady=5)

if __name__ == '__main__':
    root.mainloop()
