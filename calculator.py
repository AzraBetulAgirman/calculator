import tkinter as tk
from math import sqrt

def click(value):
    m = entry.get()

    if value == "C":
        entry.delete(0, tk.END)
        entry.insert(0, "0")

    elif value == "←":
        if len(m) > 1:
            entry.delete(len(m)-1)
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "0")

    elif value == "√":
        try:
            sonuc = sqrt(float(m))
            entry.delete(0, tk.END)
            entry.insert(0, f"{sonuc:.10g}".rstrip('.'))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Hata")

    elif value == "x²":
        try:
            sayi = float(m)
            sonuc = sayi ** 2
            entry.delete(0, tk.END)
            entry.insert(0, f"{sonuc:.10g}".rstrip('.'))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Hata")

    elif value == "=":
        try:
            ifade = m.replace("%", "/100")
            ifade = ifade.replace("×", "*") 
            ifade = ifade.replace("÷", "/") 
            
            sonuc = eval(ifade)
            entry.delete(0, tk.END)
            entry.insert(0, f"{sonuc:.10g}".rstrip('.'))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Hata")

    else:
        if m == "0" or m == "Hata":
            entry.delete(0, tk.END)
        entry.insert(tk.END, value)


window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("420x620")
window.configure(bg="#1e1e1e")
window.resizable(False, False)

entry = tk.Entry(window, font=("Consolas", 36), bg="#000000", fg="#00ff00",bd=0, relief=tk.FLAT, justify="right", insertbackground="#00ff00")
entry.pack(fill=tk.X, padx=20, pady=25, ipady=30)

buttons = ['C',  '←',  '%',  '√', '7',  '8',  '9',  '÷', '4',  '5',  '6',  '×', '1',  '2',  '3',  '-', '0',  'x²', '=',  '+']

frame = tk.Frame(window, bg="#1e1e1e")
frame.pack(expand=True, fill="both", padx=20, pady=10)

for i in range(20):
    r = i // 4
    c = i % 4
    text = buttons[i]

    if text == "C":
        bg, fg = "#ff3b30", "white"      
    elif text == "=":
        bg, fg = "#30d158", "white"  
    elif text in ("÷", "×", "-", "+", "√", "x²", "%"):
        bg, fg = "#3a3a3c", "#ffffff"  
    else:
        bg, fg = "#2c2c2e", "#ffffff"    

    btn = tk.Button(frame, text=text, font=("Arial", 24, "bold"),
                    bg=bg, fg=fg, activebackground="#555",
                    relief=tk.FLAT, bd=0, highlightthickness=0,
                    command=lambda x=text: click(x))

    btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4, ipady=20)

    frame.grid_rowconfigure(r, weight=1)
    frame.grid_columnconfigure(c, weight=1)

window.mainloop()