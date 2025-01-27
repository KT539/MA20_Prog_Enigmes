# recherche de solutions
# problème des triangles rectangles entiers
# JCY pour illustration étudiants

import tkinter as tk
from tkinter import messagebox
import time
import math

def find_square_harshad():
    try:
        # Récupérer les bornes min et max
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise ValueError("Les bornes doivent être des entiers positifs et min ≤ max.")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []


        # Trouver les triangles rectangles entiers
        # Solution brute


        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun triangle rectangle entier trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def find_square_harshad_smart():
    try:
        # Récupérer les bornes min et max
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise ValueError("Les bornes doivent être des entiers positifs et min ≤ max.")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []


        # Trouver triangles rectangles entiers
        # solution smart


        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions:
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun carré harshad trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


# Interface tkinter
root = tk.Tk()
root.title("Triangles rectangles entiers")

# Labels et champs d'entrée
tk.Label(root, text="Valeur minimale (min):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_min = tk.Entry(root)
entry_min.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Valeur maximale (max):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_max = tk.Entry(root)
entry_max.grid(row=1, column=1, padx=10, pady=5)
entry_min.insert(0, "1000")  # Valeur par défaut pour min
entry_max.insert(0, "1000000")  # Valeur par défaut pour max

# Boutons pour calculer
btn_calculate = tk.Button(root, text="Triangles rect entiers", command=find_square_harshad)
btn_calculate.grid(row=2, column=0,  pady=10)
btn_calculate_smart = tk.Button(root, text="Triangles rect ent. smart", command=find_square_harshad_smart)
btn_calculate_smart.grid(row=2, column=1,  pady=10)
btn_calculate_prim = tk.Button(root, text="Triangles rect primitifs", command=find_square_harshad_smart)
btn_calculate_prim.grid(row=3, column=0,  pady=10)

# Zone de texte pour afficher les résultats (dans un frame)
frame_output = tk.Frame(root)
frame_output.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

text_output = tk.Text(frame_output, width=50, height=15, wrap=tk.WORD)
scrollbar = tk.Scrollbar(frame_output, command=text_output.yview)
text_output.config(yscrollcommand=scrollbar.set)

text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lancement de l'application
root.mainloop()