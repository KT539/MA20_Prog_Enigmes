# recherche de solutions
# problème des briques Euler
# JCY pour illustration étudiants

import tkinter as tk
from tkinter import messagebox
import time
import math

def find_briques_euler_brutes():
    try:
        # Récupérer les bornes min et max

        max_val = int(entry_max.get())
        if max_val < 0:
            raise ValueError("Le maximum donné doit être un entier positif")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []


        # Trouver briques Euler brute
        for a in range(1, max_val + 1):
            for b in range(a, max_val + 1):
                for c in range(b, max_val + 1):
                    numbers_tested += 1
                    if (math.sqrt(a ** 2 + b ** 2)).is_integer():
                        if (math.sqrt(b ** 2 + c ** 2)).is_integer():
                            if (math.sqrt(c ** 2 + a ** 2)).is_integer():
                                solutions.append((a, b, c))


        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Briques Euler trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucune brique Euler entier trouvée.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def find_briques_euler_smart():
    try:
        # Récupérer les bornes min et max
        max_val = int(entry_max.get())
        if max_val < 0:
            raise ValueError("Le maximum donné doit être un entier positif")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []


        # Trouver briques Euler smart
        squares = {i ** 2: i for i in range(1, math.isqrt(2 * max_val ** 2) + 1)}
        for a in range(1, max_val + 1):
            for b in range(a, max_val + 1):
                ab = a ** 2 + b ** 2
                numbers_tested += 1
                if ab not in squares:
                    continue

                for c in range(b, max_val + 1):
                    bc = b ** 2 + c ** 2
                    ac = a ** 2 + c ** 2
                    if bc in squares and ac in squares:
                        solutions.append((a, b, c))


        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Briques Euler trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions:
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucune brique Euler trouvée.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


# Interface tkinter
root = tk.Tk()
root.title("Briques Euler")

tk.Label(root, text="Valeur maximale (max):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_max = tk.Entry(root)
entry_max.grid(row=1, column=1, padx=10, pady=5)
entry_max.insert(0, "1000")  # Valeur par défaut pour max

# Boutons pour calculer
btn_calculate = tk.Button(root, text="Briques Euler brutes", command=find_briques_euler_brutes)
btn_calculate.grid(row=2, column=0,  pady=10)
btn_calculate_smart = tk.Button(root, text="Briques Euler smart", command=find_briques_euler_smart)
btn_calculate_smart.grid(row=2, column=1,  pady=10)


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