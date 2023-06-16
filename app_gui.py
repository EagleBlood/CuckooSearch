import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()

# Ustawienia głównego okna
root.geometry("800x600")
root.title("Algorytm kukułczy")

# Górna sekcja
upper_frame = tk.Frame(root, pady=10)
upper_frame.pack()

# Wczytanie obrazu
image = Image.open("cuckoo_icon.png")

# Skalowanie obrazu do pożądanego rozmiaru
width, height = 60, 60
image = image.resize((width, height), Image.ANTIALIAS)

# Konwersja obrazu do formatu obsługiwanego przez tkinter
photo = ImageTk.PhotoImage(image)

# Utworzenie etykiety z obrazem
logo_label = tk.Label(upper_frame, image=photo)
logo_label.image = photo
logo_label.pack(side=tk.LEFT)

title_label = tk.Label(upper_frame, text="Algorytm kukułczy", font=("Helvetica", 19, "bold"))
title_label.pack(side=tk.LEFT)

# Kontener przechowujący Ustawienia i Wyniki
settings_results_frame = tk.Frame(root)
settings_results_frame.pack(pady=10)

# Kontener z ustawieniami
settings_frame = ttk.Frame(settings_results_frame, width=400, height=300, borderwidth=1, relief=tk.SOLID)
settings_frame.pack(side=tk.LEFT, padx=(0, 10), fill=tk.Y, pady=(20, 20))

# Wewnętrzny kontener z większym padding w kontenerze ustawień
inner_settings_frame = ttk.Frame(settings_frame, padding=20)
inner_settings_frame.pack(fill=tk.BOTH, expand=True)

settings_label = ttk.Label(inner_settings_frame, text="Ustawienia", font=("Helvetica", 14))
settings_label.pack(pady=(0, 10))

separator = ttk.Separator(inner_settings_frame, orient=tk.HORIZONTAL)
separator.pack(fill=tk.X, padx=10, pady=10)

table_frame = ttk.Frame(inner_settings_frame)
table_frame.pack()

# Tabela w kontenerze z ustawieniami
rows = 5
columns = 3

for i in range(rows):
    for j in range(columns):
        if j == 2:
            text_entry = ttk.Entry(table_frame)
            text_entry.grid(row=i, column=j, padx=10, pady=5)
        else:
            if i == 0 and j == 0:
                label = ttk.Label(table_frame, text="Rozmiar populacji", anchor='w', justify='left')
            elif i == 0 and j == 1:
                label = ttk.Label(table_frame, text="(N)", justify='center')
            elif i == 1 and j == 0:
                label = ttk.Label(table_frame, text="Ilość iteracji", anchor='w', justify='left')
            elif i == 1 and j == 1:
                label = ttk.Label(table_frame, text="(iter)", justify='center')
            elif i == 2 and j == 0:
                label = ttk.Label(table_frame, text="Prawdopodobieństwo", anchor='w', justify='left')
            elif i == 2 and j == 1:
                label = ttk.Label(table_frame, text="(prob)", justify='center')
            elif i == 3 and j == 0:
                label = ttk.Label(table_frame, text="Dolna granica", anchor='w', justify='left')
            elif i == 3 and j == 1:
                label = ttk.Label(table_frame, text="(Lb)", justify='center')
            elif i == 4 and j == 0:
                label = ttk.Label(table_frame, text="Górna granica", anchor='w', justify='left')
            elif i == 4 and j == 1:
                label = ttk.Label(table_frame, text="(Ub)", justify='center')
            if j == 0:
                label.grid(row=i, column=j, padx=10, pady=5, sticky='w')
            else:
                label.grid(row=i, column=j, padx=10, pady=5)

# Napis i rozwijany choice box
text_label = ttk.Label(inner_settings_frame, text="Wybierz funkcje celu:", anchor='center')
text_label.pack(pady=10)

options = ["rosenbrock", "rastrigin", "schwefel", "M/M/m/FIFO/m+N"]
choice_box = ttk.Combobox(inner_settings_frame, values=options, width=40, justify='center')
choice_box.pack()

# Przyciski Reset i Oblicz
buttons_frame = ttk.Frame(inner_settings_frame)
buttons_frame.pack(pady=20)

reset_button = ttk.Button(buttons_frame, text="Reset", width=19)
reset_button.pack(side=tk.LEFT, padx=10)

calculate_button = ttk.Button(buttons_frame, text="Oblicz", width=19)
calculate_button.pack(side=tk.LEFT, padx=10)

# Kontener z wynikami
results_frame = ttk.Frame(settings_results_frame, width=400, height=200, borderwidth=1, relief=tk.SOLID)
results_frame.pack(side=tk.LEFT, padx=(10, 0), fill=tk.Y, pady=(20, 20))

# Wewnętrzny kontener z większym padding w kontenerze wyników
inner_results_frame = ttk.Frame(results_frame, padding=20)
inner_results_frame.pack(fill=tk.BOTH, expand=True)

results_label = ttk.Label(inner_results_frame, text="Wyniki", font=("Helvetica", 14))
results_label.pack(pady=(0, 10))

separator2 = ttk.Separator(inner_results_frame, orient=tk.HORIZONTAL)
separator2.pack(fill=tk.X, padx=10, pady=10)

# Dodanie napisu "Optymalne Wyniki:"
optimal_results_label = ttk.Label(inner_results_frame, text="Optymalne Wyniki:", font=("Helvetica", 10))
optimal_results_label.pack(pady=(0, 10))

# Tabela z optymalnymi wynikami
results_table_frame = ttk.Frame(inner_results_frame, borderwidth=1, relief=tk.SOLID)
results_table_frame.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

rows = 5

for i in range(rows):
    label = ttk.Label(results_table_frame, text=f"Wynik {i+1}", anchor=tk.CENTER)
    label.pack(padx=10, pady=5, ipady=3)

# Napis "Najlepszy wynik"
best_result_label = ttk.Label(inner_results_frame, text="Najlepszy wynik:", font=("Helvetica", 10))
best_result_label.pack(pady=10)

# Napis "123" pogrubiony pod etykietą "Najlepszy wynik"
best_result_value_label = ttk.Label(inner_results_frame, text="Wynik 1", font=("Helvetica", 9, "bold"))
best_result_value_label.pack()

# Miejsca na wykresy
charts_frame = ttk.Frame(root)
charts_frame.pack(pady=20)

chart1_frame = ttk.Frame(charts_frame, width=400)
chart1_frame.pack(side=tk.LEFT, padx=(0, 10))

chart2_frame = ttk.Frame(charts_frame, width=400)
chart2_frame.pack(side=tk.LEFT)

root.mainloop()
