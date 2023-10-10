import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkcalendar import DateEntry

# Funkcja do obsługi przycisku "Sprawdź"
def check_numbers():
    # Pobierz dane od użytkownika
    lotto_type = lotto_type_box.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    # Utwórz połączenie z bazą danych MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lotto"
    )
    
    # Utwórz kursor do wykonywania zapytań SQL
    cursor = connection.cursor()
    
    # Zapytanie SQL do pobrania najczęściej losowanych liczb w podanym przedziale dat
    query = f"""
        SELECT number1, number2, number3, number4, number5, number6, number7, number8, number9, number10
        FROM lotto_results
        WHERE lotto_type = '{lotto_type}'
        AND date BETWEEN '{start_date}' AND '{end_date}'
    """
    
    # Wykonaj zapytanie SQL
    cursor.execute(query)
    
    # Pobierz wyniki zapytania
    rows = cursor.fetchall()
    
    # Oblicz, które liczby były najczęściej losowane
    number_counts = {}
    for row in rows:
        for number in row:
            if number is not None:
                if number in number_counts:
                    number_counts[number] += 1
                else:
                    number_counts[number] = 1
    
    # Posortuj liczby według liczby wystąpień
    sorted_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Wyświetl wyniki w oknie programu
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Najczęściej losowane liczby w okresie od {start_date} do {end_date} dla typu: {lotto_type}:\n")
    for number, count in sorted_numbers:
        result_text.insert(tk.END, f"Liczba {number}: {count} razy\n")
    
    # Zamknij połączenie z bazą danych
    cursor.close()
    connection.close()

# Tworzenie głównego okna
root = tk.Tk()
root.title("Sprawdź najczęściej losowane liczby Lotto")
root.geometry("500x700")
root.resizable(False,False)

# Etykiety i pola tekstowe
space_label = tk.Label(root, text="", font=("Helvetica", 15))
space_label.pack(pady=10)
lotto_type_label = tk.Label(root, text="Typ Lotto", font=("Helvetica", 15))
lotto_type_label.pack()
lotto_type_box = ["Ekstra Pensja","Eurojackpot","Keno","Lotto","Mini Lotto","Multi Multi","Szybkie 600"]
lotto_type_box = ttk.Combobox(root, values=lotto_type_box)
lotto_type_box.pack(pady=10)

start_date_label = tk.Label(root, text="Data początkowa", font=("Helvetica", 15))
start_date_label.pack()
start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date_entry.pack(pady=10)

end_date_label = tk.Label(root, text="Data końcowa", font=("Helvetica", 15))
end_date_label.pack()
end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date_entry.pack(pady=10)

# Przycisk "Sprawdź"
check_button = tk.Button(root, text="Sprawdź", height = 2, width = 10, bg='#ffb92d', command=check_numbers, font=("Helvetica", 15))
check_button.pack(pady=10)

# Wyniki
result_text = tk.Text(root, height=20, width=60)
result_text.pack()

if __name__ == '__main__':
    root.mainloop()
