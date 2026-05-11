import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog, Toplevel, Button, Label, Tk


def wybierz_plik():
    test = filedialog.askopenfilename(
        title="Podaj plik excela",
        filetypes=[("plik excel", "*.xlsx *.xls")]
    )
    if test:
        dt = pd.read_excel(test)
        if 'X' in dt.columns and 'Y' in dt.columns:
            x = dt["X"]
            y = dt["Y"]
            plt.hist2d(x, y, bins=10, cmap='inferno')
            plt.colorbar()
            plt.xlabel("Os x")
            plt.ylabel("Os y")
            plt.title("Histogram 2d Aplikacja")
            plt.show()
        else:
            print("nieprawidlowy plik")
    else:
        print("nie wybrales zadnego pliku")


def wersja_testowa():
    x = np.random.randn(100)
    y = np.random.randn(100)
    plt.hist2d(x, y, bins=10, cmap='inferno')
    plt.title("Dane Losowe")
    plt.xlabel("Os x")
    plt.ylabel("Os y")
    plt.colorbar()
    plt.show()


def click_fun(root, label):
    """Funkcja wywoływana przez główny program"""
    # Tworzymy nowe okno (jako dziecko głównego)
    okno = Toplevel(root)
    okno.title("Aplikacja hist2d")
    okno.geometry("500x300")

    napis = Label(okno, text="STWÓRZ WŁASNĄ MAPĘ CIEPLNĄ!",
                  font=('Arial', 20, 'bold'), fg="black",
                  bd=10)
    napis.pack(pady=10)

    wybierz_przycisk = Button(okno, text="Wybieram plik z danymi",
                              command=wybierz_plik, bg="lightskyblue",
                              font=('Arial', 15, 'bold'))
    losowe_przycisk = Button(okno, text="Generuj dane losowo",
                             command=wersja_testowa, bg="#39db64",
                             font=('Arial', 15, 'bold'))
    zamknij_przycisk = Button(okno, text="Wyjdź",
                              command=okno.destroy, bg="#E42020",
                              font=('Arial', 15, 'bold'))

    wybierz_przycisk.pack(pady=10)
    losowe_przycisk.pack(pady=10)
    zamknij_przycisk.pack(pady=10)

    # Aktualizujemy etykietę w głównym oknie
    label.config(text="Temat 09 - Histogram 2D")


if __name__ == "__main__":
    def interface():
        """Funkcja wywoływana przez główny program"""
        # Tworzymy nowe okno (jako dziecko głównego)
        okno = Tk()
        okno.title("Aplikacja hist2d")
        okno.geometry("500x300")

        napis = Label(okno, text="STWÓRZ WŁASNĄ MAPĘ CIEPLNĄ!",
                      font=('Arial', 20, 'bold'), fg="black",
                      bd=10)
        napis.pack(pady=10)

        wybierz_przycisk = Button(okno, text="Wybieram plik z danymi",
                                  command=wybierz_plik, bg="lightskyblue",
                                  font=('Arial', 15, 'bold'))
        losowe_przycisk = Button(okno, text="Generuj dane losowo",
                                 command=wersja_testowa, bg="#39db64",
                                 font=('Arial', 15, 'bold'))
        zamknij_przycisk = Button(okno, text="Wyjdź",
                                  command=okno.destroy, bg="#E42020",
                                  font=('Arial', 15, 'bold'))

        wybierz_przycisk.pack(pady=10)
        losowe_przycisk.pack(pady=10)
        zamknij_przycisk.pack(pady=10)
        okno.mainloop()

    interface()
