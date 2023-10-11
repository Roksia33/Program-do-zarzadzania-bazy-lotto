import sys
import os
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "datetime", "mysql.connector","subprocess","requests","json"],
    "include_files": ['pic/lotto.png','kll.py','nll.py','Slr.py','spl.py','sprawdz_godzine.py','zmiana_danych.py','dodawanie_danych/Ekstra_pensja.py','dodawanie_danych/Eurojackpot.py','dodawanie_danych/Keno.py','dodawanie_danych/Lotto.py','dodawanie_danych/Mini_lotto.py','dodawanie_danych/Multi_multi.py','dodawanie_danych/Szybkie_600.py'],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base)]

setup(
    name="Aplikacja do zarządzania bazą Lotto",
    version="1.1",
    description="",
    options={"build_exe": build_exe_options},
    executables=executables,
)

#python setup.py build