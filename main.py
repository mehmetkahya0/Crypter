"""
GUI VERSION OF THE ENCRYPTER & DECRYPTER PROGRAM
Text encrypter & Decrypt program
02/27/2024
Mehmet Kahya
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import font
from colorama import Fore

def encrypt(text):
    encryption_dict = {
        "A": "!", "B": "@", "C": "#", "D": "$", "E": "%", "F": "^", "G": "&", "H": "*", "I": "(",
        "J": ")", "K": "-", "L": "_", "M": "+", "N": "=", "O": "{", "P": "}", "Q": "[", "R": "]",
        "S": "\\", "T": "|", "U": ":", "V": ";", "W": "\"", "X": "'", "Y": "<", "Z": ">"
    }
    encrypted_text = "".join(encryption_dict.get(letter, letter) for letter in text)
    return encrypted_text

def decrypt(text):
    encryption_dict = {
        "A": "!", "B": "@", "C": "#", "D": "$", "E": "%", "F": "^", "G": "&", "H": "*", "I": "(",
        "J": ")", "K": "-", "L": "_", "M": "+", "N": "=", "O": "{", "P": "}", "Q": "[", "R": "]",
        "S": "\\", "T": "|", "U": ":", "V": ";", "W": "\"", "X": "'", "Y": "<", "Z": ">"
    }
    decryption_dict = {v: k for k, v in encryption_dict.items()}  # Reverse the dictionary
    decrypted_text = "".join(decryption_dict.get(letter, letter) for letter in text)
    return decrypted_text

def main():
    def encrypt_text():
        text = text_entry.get().upper()
        text = list(text)  # Split the text into a list of characters
        encrypted_text = ''.join(encrypt(letter) for letter in text)  # Encrypt each character and join them into a string
        result_text.delete("1.0", tk.END)  # Clear the Text widget
        result_text.insert(tk.END, "Encrypted text: " + encrypted_text)  # Insert the encrypted text

    def decrypt_text():
        text = text_entry.get().upper()
        text = list(text)  # Split the text into a list of characters
        decrypted_text = ''.join(decrypt(letter) for letter in text)  # Decrypt each character and join them into a string
        result_text.delete("1.0", tk.END)  # Clear the Text widget
        result_text.insert(tk.END, "Decrypted text: " + decrypted_text)  # Insert the decrypted text

    window = tk.Tk()
    window.title("CRYPTER©")
    window.geometry("300x300")
    window.resizable(False, False)

    text_label = ttk.Label(window, text="Enter the text to encrypt/decrypt:", font=("Arial", 13, "bold"))
    text_label.pack(pady=10)

    text_entry = ttk.Entry(window)
    text_entry.pack()

    encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_text)
    encrypt_button.pack(pady=10)

    decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt_text)
    decrypt_button.pack(pady=10)

    result_text = tk.Text(window, height=5, width=30)
    result_text.pack()
    
    copyright = ttk.Label(window, text="© 2024 Mehmet Kahya")
    copyright.pack()

    window.mainloop()

main()