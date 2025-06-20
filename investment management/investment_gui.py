import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Machine 1 inputs
        m1_price = float(entry_m1_price.get())
        m1_dep = float(entry_m1_dep.get())
        m1_main = float(entry_m1_main.get())
        m1_setup = float(entry_m1_setup.get())
        m1_serv = float(entry_m1_serv.get())
        m1_end = float(entry_m1_end.get())

        # Machine 2 inputs
        m2_price = float(entry_m2_price.get())
        m2_dep = float(entry_m2_dep.get())
        m2_main = float(entry_m2_main.get())
        m2_setup = float(entry_m2_setup.get())
        m2_serv = float(entry_m2_serv.get())
        m2_end = float(entry_m2_end.get())

        # Condition calculations
        m1_c1 = m1_price - m1_dep - m1_end
        m1_c2 = (m1_main + m1_serv) * 5 + m1_setup

        m2_c1 = m2_price - m2_dep - m2_end
        m2_c2 = (m2_main + m2_serv) * 5 + m2_setup

        # Score logic
        score1 = (m1_c1 < m2_c1) + (m1_c2 < m2_c2)
        score2 = 2 - score1

        # Show results
        summary = f"""Comparison Summary:

Machine 1 - Condition 1: ₹{m1_c1:.2f}, Condition 2: ₹{m1_c2:.2f}
Machine 2 - Condition 1: ₹{m2_c1:.2f}, Condition 2: ₹{m2_c2:.2f}

"""
        if score1 > score2:
            summary += "✅ Machine 1 is the better investment."
        elif score2 > score1:
            summary += "✅ Machine 2 is the better investment."
        else:
            summary += "⚖️ Both machines are equally good investments."

        messagebox.showinfo("Investment Decision", summary)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

# --- GUI Layout ---
root = tk.Tk()
root.title("Investment Decision Chatbot")
root.geometry("500x700")

# Headings
tk.Label(root, text="Machine 1 Details", font=("Arial", 14, "bold")).pack()

# Machine 1 Inputs
entry_m1_price = tk.Entry(root); tk.Label(root, text="Price:").pack(); entry_m1_price.pack()
entry_m1_dep = tk.Entry(root); tk.Label(root, text="Depreciation:").pack(); entry_m1_dep.pack()
entry_m1_main = tk.Entry(root); tk.Label(root, text="Annual Maintenance Cost:").pack(); entry_m1_main.pack()
entry_m1_setup = tk.Entry(root); tk.Label(root, text="One-time Setup Cost:").pack(); entry_m1_setup.pack()
entry_m1_serv = tk.Entry(root); tk.Label(root, text="Annual Servicing Cost:").pack(); entry_m1_serv.pack()
entry_m1_end = tk.Entry(root); tk.Label(root, text="End-of-5th-Year Value:").pack(); entry_m1_end.pack()

# Separator
tk.Label(root, text="").pack()

# Machine 2
tk.Label(root, text="Machine 2 Details", font=("Arial", 14, "bold")).pack()

entry_m2_price = tk.Entry(root); tk.Label(root, text="Price:").pack(); entry_m2_price.pack()
entry_m2_dep = tk.Entry(root); tk.Label(root, text="Depreciation:").pack(); entry_m2_dep.pack()
entry_m2_main = tk.Entry(root); tk.Label(root, text="Annual Maintenance Cost:").pack(); entry_m2_main.pack()
entry_m2_setup = tk.Entry(root); tk.Label(root, text="One-time Setup Cost:").pack(); entry_m2_setup.pack()
entry_m2_serv = tk.Entry(root); tk.Label(root, text="Annual Servicing Cost:").pack(); entry_m2_serv.pack()
entry_m2_end = tk.Entry(root); tk.Label(root, text="End-of-5th-Year Value:").pack(); entry_m2_end.pack()

# Calculate Button
tk.Label(root, text="").pack()
tk.Button(root, text="Compare Machines", command=calculate, font=("Arial", 12), bg="blue", fg="white").pack()

root.mainloop()
