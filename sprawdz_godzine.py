import tkinter as tk
from datetime import datetime, timedelta, time

def keno():
    current_time = datetime.now()
    start_time = current_time.replace(hour=6, minute=34, second=0, microsecond=0)
    end_time = current_time.replace(hour=23, minute=54, second=0, microsecond=0)
    
    if current_time < start_time:
        next_draw_time = start_time
    elif current_time >= end_time:
        next_draw_time = start_time + timedelta(days=1)
    else:
        time_difference = (current_time - start_time).total_seconds()
        draw_interval_seconds = 4 * 60
        draw_count = int(time_difference / draw_interval_seconds) + 1
        next_draw_time = start_time + timedelta(seconds=draw_count * draw_interval_seconds)
    
    time_difference = next_draw_time - current_time
    hours, remainder = divmod(time_difference.total_seconds(), 3600)
    minutes = remainder // 60
    seconds = remainder % 60

    next_draw_label1.config(text=f"Następne losowanie o {next_draw_time.strftime('%H:%M')}")
    time_left_label1.config(text=f"Pozostało: {int(hours)} godz. {int(minutes)} min. {int(seconds)} sek.")
    root.after(1000, keno)

def szybkie600():
    current_time2 = datetime.now()
    start_time2 = current_time2.replace(hour=6, minute=36, second=0, microsecond=0)
    end_time2 = current_time2.replace(hour=23, minute=52, second=0, microsecond=0)
    
    if current_time2 < start_time2:
        next_draw_time2 = start_time2
    elif current_time2 >= end_time2:
        next_draw_time2 = start_time2 + timedelta(days=1)
    else:
        time_difference2 = (current_time2 - start_time2).total_seconds()
        draw_interval_seconds2 = 4 * 60
        draw_count = int(time_difference2 / draw_interval_seconds2) + 1
        next_draw_time2 = start_time2 + timedelta(seconds=draw_count * draw_interval_seconds2)
    
    time_difference2 = next_draw_time2 - current_time2
    hours2, remainder2 = divmod(time_difference2.total_seconds(), 3600)
    minutes2 = remainder2 // 60
    seconds2 = remainder2 % 60

    next_draw_label2.config(text=f"Następne losowanie o {next_draw_time2.strftime('%H:%M')}")
    time_left_label2.config(text=f"Pozostało: {int(hours2)} godz. {int(minutes2)} min. {int(seconds2)} sek.")
    root.after(1000, szybkie600)

def lotto():
    teraz = datetime.now()
    dzien_tygodnia = teraz.weekday()
    
    if dzien_tygodnia in [1, 3, 5] and teraz.hour < 22:
        godzina_losowania = datetime(teraz.year, teraz.month, teraz.day, 22, 0, 0)
    else:
        if dzien_tygodnia == 5:
            dni_do_nastepnego_losowania = (7 - dzien_tygodnia + 2) % 7
        else:
            dni_do_nastepnego_losowania = (7 - dzien_tygodnia) % 7
        godzina_losowania = datetime(teraz.year, teraz.month, teraz.day + dni_do_nastepnego_losowania, 22, 0, 0)

    czas_do_losowania = godzina_losowania - teraz
    godziny, sekundy = divmod(czas_do_losowania.seconds, 3600)
    godziny, reszta = divmod(czas_do_losowania.total_seconds(), 3600)
    minuty, sekundy = divmod(reszta, 60)
    
    # Wyświetl wynik w oknie
    next_draw_label3.config(text=f"Następne losowanie odbędzie się: {godzina_losowania.strftime('%Y-%m-%d o %H:%M')}")
    time_left_label3.config(text=f"Pozostało: {czas_do_losowania.days} dni {int(godziny)} godz. {int(minuty)} min. {int(sekundy)} sek.")
    root.after(1000, lotto)

def eurojackpot():
    dzis = datetime.now()
    dzien_tygodnia = dzis.weekday()
    
    if dzien_tygodnia == 1:  # Wtorek
        godzina_losowania = datetime(dzis.year, dzis.month, dzis.day, 20, 15)
    elif dzien_tygodnia == 4:  # Piątek
        godzina_losowania = datetime(dzis.year, dzis.month, dzis.day, 20, 0)
    else:
        if dzien_tygodnia < 1:  # Jeśli dzisiaj jest niedziela lub poniedziałek
            dni_do_wtorku = 1 - dzien_tygodnia
            godzina_losowania = datetime(dzis.year, dzis.month, dzis.day + dni_do_wtorku, 20, 15)
        else:  # Jeśli dzisiaj jest środa, czwartek lub sobota
            dni_do_wtorku = (1 + 7 - dzien_tygodnia) % 7
            godzina_losowania = datetime(dzis.year, dzis.month, dzis.day + dni_do_wtorku, 20, 15)
    
    czas_do_losowania = godzina_losowania - dzis
    godziny, sekundy = divmod(czas_do_losowania.seconds, 3600)
    minuty, sekundy = divmod(sekundy, 60)
    sekundy = (sekundy % 60)
    
    czas_str = godzina_losowania.strftime("%Y-%m-%d o %H:%M")
    next_draw_label4.config(text=f"Następne losowanie odbędzie się: {czas_str}")
    time_left_label4.config(text=f"Pozostało: {czas_do_losowania.days} dni {godziny} godz. {minuty} min. {sekundy} sek.")

    root.after(1000, eurojackpot)

def ekstra_pensja_mini_lotto():
    now = datetime.now()
    target_time = datetime(now.year, now.month, now.day, 22, 0, 0)
    
    if now >= target_time:
        target_time += timedelta(days=1)  # Przesunięcie na następny dzień, jeśli jest już po 22:00
    
    time_difference = target_time - now
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    next_draw_label5.config(text="Codzienne losowanie o 22:00")
    time_left_label5.config(text=f"Pozostało: {hours} godz. {minutes} min. {seconds} sek.")
    
    root.after(1000, ekstra_pensja_mini_lotto)

def multi_multi():
    current_time = datetime.now().time()
    target_time_1 = time(14, 0)
    target_time_2 = time(22, 0)

    if current_time < target_time_1:
        time_difference = datetime.combine(datetime.now().date(), target_time_1) - datetime.now()
    elif current_time < target_time_2:
        time_difference = datetime.combine(datetime.now().date(), target_time_2) - datetime.now()
    else:
        tomorrow_date = datetime.now().date() + timedelta(days=1)
        time_difference = datetime.combine(tomorrow_date, target_time_1) - datetime.now()

    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    next_draw_label6.config(text="Codzienne losowanie o 14:00 i 22:00")
    time_left_label6.config(text=f"Pozostało: {hours:02d} godz. {minutes:02d} min. {seconds:02d} sek.")
    root.after(1000, multi_multi)

root = tk.Tk()
root.title("Sprawdź godziny oraz dni losowania")
root.geometry("600x900")
root.resizable(False,False)

frame = tk.Frame(root)
frame.pack(padx=22, pady=22)

lotto_name_label1 = tk.Label(frame, text="Keno", font=("Helvetica", 17))
lotto_name_label1.pack()

next_draw_label1 = tk.Label(frame, text="", font=("Helvetica", 16))
next_draw_label1.pack()

time_left_label1 = tk.Label(frame, text="", font=("Helvetica", 16))
time_left_label1.pack()

space_label = tk.Label(frame, text="", font=("Helvetica", 17))
space_label.pack(pady=10)

lotto_name_label2 = tk.Label(frame, text="Szybkie 600", font=("Helvetica", 17))
lotto_name_label2.pack()

next_draw_label2 = tk.Label(frame, text="", font=("Helvetica", 16))
next_draw_label2.pack()

time_left_label2 = tk.Label(frame, text="", font=("Helvetica", 16))
time_left_label2.pack()

space_label = tk.Label(frame, text="", font=("Helvetica", 17))
space_label.pack(pady=10)

lotto_name_label3 = tk.Label(frame, text="Lotto", font=("Helvetica", 17))
lotto_name_label3.pack()

next_draw_label3 = tk.Label(frame, text="", font=("Helvetica", 16))
next_draw_label3.pack()

time_left_label3 = tk.Label(frame, text="", font=("Helvetica", 16))
time_left_label3.pack()

space_label = tk.Label(frame, text="", font=("Helvetica", 17))
space_label.pack(pady=10)

lotto_name_label4 = tk.Label(frame, text="Eurojackpot", font=("Helvetica", 17))
lotto_name_label4.pack()

next_draw_label4 = tk.Label(frame, text="", font=("Helvetica", 16))
next_draw_label4.pack()

time_left_label4 = tk.Label(frame, text="", font=("Helvetica", 16))
time_left_label4.pack()

space_label = tk.Label(frame, text="", font=("Helvetica", 17))
space_label.pack(pady=10)

lotto_name_label5 = tk.Label(frame, text="Ekstra Pensja, Mini Lotto", font=("Helvetica", 17))
lotto_name_label5.pack()

next_draw_label5 = tk.Label(frame, text="", font=("Helvetica", 16))
next_draw_label5.pack()

time_left_label5 = tk.Label(frame, text="", font=("Helvetica", 16))
time_left_label5.pack()

space_label = tk.Label(frame, text="", font=("Helvetica", 17))
space_label.pack(pady=10)

lotto_name_label6 = tk.Label(frame, text="Multi Multi", font=("Helvetica", 17))
lotto_name_label6.pack()

next_draw_label6 = tk.Label(frame, text="", font=("Helvetica", 16))
next_draw_label6.pack()

time_left_label6 = tk.Label(frame, text="", font=("Helvetica", 16))
time_left_label6.pack()

space_label = tk.Label(frame, text="", font=("Helvetica", 17))
space_label.pack(pady=10)

keno()
szybkie600()
lotto()
eurojackpot()
ekstra_pensja_mini_lotto()
multi_multi()

if __name__ == '__main__':
    root.mainloop()
