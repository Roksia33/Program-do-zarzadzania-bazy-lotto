import tkinter as tk

root = tk.Tk()
root.title("Kalendarz losowań Lotto")
root.resizable(False,False)

# Tworzenie ramki dla tabelki
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Nagłówki kolumn z nazwami dni tygodnia
dni_tygodnia = ["","Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Niedz"]

# Wyświetlanie nagłówków w tabelce
for i, dzien in enumerate(dni_tygodnia):
    label = tk.Label(frame, text=dzien, width=5, padx=10, pady=5, relief=tk.RIDGE, font=("Helvetica", 12, "bold"))
    label.grid(row=0, column=i)


dane = [
    ["Ekstra Pensja", "X", "X", "X", "X", "X", "X","X"],
    ["Eurojackpot", "", "X", "", "", "X", "",""],
    ["Keno", "X", "X", "X", "X", "X", "X","X"],
    ["Lotto", "", "X", "", "X", "", "X",""],
    ["Mini Lotto", "X", "X", "X", "X", "X", "X","X"],
    ["Multi Multi", "X", "X", "X", "X", "X", "X","X"],
    ["Szybkie 600", "X", "X", "X", "X", "X", "X","X"],
]

# Wyświetlanie danych w tabelce
for i, wiersz in enumerate(dane):
    for j, wartosc in enumerate(wiersz):
        label = tk.Label(frame, text=wartosc, width=15, padx=10, pady=5, relief=tk.RIDGE, font=("Helvetica", 12))
        label.grid(row=i + 1, column=j)

if __name__ == '__main__':
    root.mainloop()
