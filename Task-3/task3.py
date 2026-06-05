import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests

# ================= WINDOW ================= #

root = Tk()
root.title("Cyber Security Scanner")
root.geometry("850x600")
root.config(bg="#ffe6f2")

# ================= TITLE ================= #

title = Label(
    root,
    text="💻 CYBER SECURITY SCANNER 💻",
    font=("Arial Black", 24),
    fg="#ff1493",
    bg="#ffe6f2"
)
title.pack(pady=20)

# ================= URL ================= #

label = Label(
    root,
    text="Enter Website URL",
    font=("Arial", 14, "bold"),
    fg="#d1006f",
    bg="#ffe6f2"
)
label.pack()

url_entry = Entry(
    root,
    width=45,
    font=("Arial", 14),
    bg="white",
    fg="#ff1493",
    bd=3
)
url_entry.pack(pady=10)

# ================= OUTPUT ================= #

output = Text(
    root,
    width=90,
    height=18,
    font=("Consolas", 11),
    bg="white",
    fg="#ff1493"
)
output.pack(pady=20)

# ================= FUNCTION ================= #

def start_scan():

    output.delete("1.0", END)

    url = url_entry.get()

    if url == "":
        messagebox.showerror("Error", "Please Enter URL")
        return

    try:

        response = requests.get(url)

        output.insert(END, "💻 WEBSITE SECURITY REPORT 💻\n\n")

        output.insert(END, f"URL : {url}\n")
        output.insert(END, f"Status Code : {response.status_code}\n\n")

        output.insert(END, "🔍 Security Headers Check\n\n")

        headers = response.headers

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security"
        ]

        for header in security_headers:

            if header in headers:
                output.insert(END, f"✅ {header} Found\n")

            else:
                output.insert(END, f"⚠️ {header} Missing\n")

        output.insert(END, "\n✔️ Scan Completed Successfully")

    except Exception as e:

        output.insert(END, f"\nError : {e}")

# ================= BUTTON ================= #

scan_button = Button(
    root,
    text="START SCAN",
    font=("Arial Black", 14),
    bg="#ff1493",
    fg="white",
    padx=20,
    pady=10,
    command=start_scan
)

scan_button.pack(pady=10)

# ================= RUN ================= #

root.mainloop()
