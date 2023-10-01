import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Funkcja do zmiany liczby w bazie danych
def change_number():
    try:
        # Pobieranie danych z pól
        id = int(id_entry.get())
        lotto_type = lotto_type_entry.get()
        new_number = int(new_number_entry.get())

        # Połączenie się z bazą danych
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lotto"
        )

        cursor = connection.cursor()

        # Zmiana liczb w bazie danych
        update_query = f"UPDATE lotto_results SET {lotto_type} = %s WHERE id = %s"
        cursor.execute(update_query, (new_number, id))
        connection.commit()

        # Powiadomienie o udanej zmiany liczby
        messagebox.showinfo("Sukces", "Liczba została zaktualizowana.")
        
        # Zamykanie połączenia z bazą
        cursor.close()
        connection.close()
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")

# główne okno
root = tk.Tk()
root.title("")
root.geometry("400x550")
root.resizable(False,False)

# Etykiety i pola tekstowe
lotto_title_label = tk.Label(root, text="Zmiana danych", font=("Helvetica", 20))
lotto_title_label.pack(pady=40)

id_label = tk.Label(root, text="ID:", font=("Helvetica", 14))
id_label.pack(pady=10)
id_entry = tk.Entry(root)
id_entry.pack(pady=10)

lotto_type_label = tk.Label(root, text="Podaj kolumne (np. number1):", font=("Helvetica", 14))
lotto_type_label.pack(pady=10)
lotto_type_entry = tk.Entry(root)
lotto_type_entry.pack(pady=10)

new_number_label = tk.Label(root, text="Podaj nową liczbę:", font=("Helvetica", 14))
new_number_label.pack(pady=10)
new_number_entry = tk.Entry(root)
new_number_entry.pack(pady=10)

# Przycisk do zmiany liczby oraz wyjście z programu
change_button = tk.Button(root, text="Zmień Liczbę",height = 2, width = 12, bg='#ffb92d', command=change_number, font=("Helvetica", 13))
change_button.pack(pady=15)

button_exit = tk.Button(root, text="Wyjście",height = 2, width = 12, bg='#ffb92d', command=root.quit, font=("Helvetica", 13))
button_exit.pack(pady=10)

# Uruchomienie aplikacji
if __name__ == '__main__':
    root.mainloop()
