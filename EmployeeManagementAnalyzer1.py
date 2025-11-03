import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Employee Performance Analyzer")
root.geometry("500x600")
root.config(bg="#E9F5FF")

# -------------------- HEADER --------------------
header_frame = tk.Frame(root, bg="#0078D7")
header_frame.pack(fill="x")

tk.Label(
    header_frame,
    text="Employee Performance Analyzer",
    bg="#0078D7",
    fg="white",
    font=("Helvetica", 18, "bold"),
    pady=15
).pack()

# -------------------- INPUT AREA --------------------
main_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="groove")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Employee name input
tk.Label(main_frame, text="Employee Name:", font=("Arial", 12, "bold"), bg="#FFFFFF").pack(pady=(15, 5))
name_entry = tk.Entry(main_frame, width=35, font=("Arial", 12), bd=2, relief="solid")
name_entry.pack(pady=5)

# Skill list
skills = ["Teamwork", "Communication", "Punctuality", "Problem Solving", "Productivity"]
entries = {}

tk.Label(main_frame, text="Enter Ratings (0–10):", font=("Arial", 12, "italic"), bg="#FFFFFF", fg="#333").pack(pady=(10, 5))

form_frame = tk.Frame(main_frame, bg="#FFFFFF")
form_frame.pack(pady=10)

for skill in skills:
    row = tk.Frame(form_frame, bg="#FFFFFF")
    row.pack(pady=8)
    tk.Label(row, text=f"{skill}:", font=("Arial", 12), width=15, anchor="w", bg="#FFFFFF").pack(side="left")
    e = tk.Entry(row, width=10, font=("Arial", 12), bd=2, relief="solid", justify="center")
    e.pack(side="left")
    entries[skill] = e

# -------------------- FUNCTIONS --------------------
def analyze_performance():
    try:
        name = name_entry.get().strip()
        if not name:
            messagebox.showerror("Missing Input", "Please enter the employee name.")
            return

        ratings = np.array([float(entries[s].get()) for s in skills])

        # Validate
        if any(r < 0 or r > 10 for r in ratings):
            messagebox.showerror("Invalid Input", "All ratings must be between 0 and 10.")
            return

        total = np.sum(ratings)
        avg = np.mean(ratings)

        # Determine grade
        if avg >= 9:
            grade = "Outstanding 🌟"
        elif avg >= 8:
            grade = "Excellent"
        elif avg >= 7:
            grade = "Very Good"
        elif avg >= 5:
            grade = "Average"
        else:
            grade = "Needs Improvement ⚠️"

        result = (
            f"Employee: {name}\n"
            f"Total Score: {total:.1f} / 50\n"
            f"Average Score: {avg:.2f}\n"
            f"Performance: {grade}"
        )

        messagebox.showinfo("Performance Summary", result)

        # -------------------- CHART --------------------
        plt.figure(figsize=(6, 4))
        plt.bar(skills, ratings, color="#00BFFF", edgecolor="black")
        plt.title(f"{name}'s Performance Analysis", fontsize=14, fontweight='bold')
        plt.xlabel("Skill Areas")
        plt.ylabel("Ratings (out of 10)")
        plt.ylim(0, 10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric ratings for all skills.")

def clear_all():
    name_entry.delete(0, tk.END)
    for e in entries.values():
        e.delete(0, tk.END)

# -------------------- BUTTONS --------------------
btn_frame = tk.Frame(main_frame, bg="#FFFFFF")
btn_frame.pack(pady=20)

analyze_btn = tk.Button(
    btn_frame,
    text="Analyze Performance",
    command=analyze_performance,
    font=("Arial", 12, "bold"),
    bg="#0078D7",
    fg="white",
    width=20,
    bd=0,
    relief="flat",
    cursor="hand2",
    activebackground="#005BB5",
    activeforeground="white"
)
analyze_btn.grid(row=0, column=0, padx=10, pady=5)

clear_btn = tk.Button(
    btn_frame,
    text="Clear All",
    command=clear_all,
    font=("Arial", 12, "bold"),
    bg="#FF4C4C",
    fg="white",
    width=15,
    bd=0,
    relief="flat",
    cursor="hand2",
    activebackground="#CC0000",
    activeforeground="white"
)
clear_btn.grid(row=0, column=1, padx=10, pady=5)

# Footer
tk.Label(root, text="© 2025 Employee Performance Analyzer", font=("Arial", 9, "italic"), bg="#E9F5FF", fg="#444").pack(side="bottom", pady=5)

root.mainloop()
