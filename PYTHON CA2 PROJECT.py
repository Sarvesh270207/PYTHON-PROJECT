import tkinter as tk
from tkinter import messagebox

# PALINDROME FUNCTION
def check_palindrome():
    text = palindrome_entry.get()
    try:
        if text.strip() == "":
            raise ValueError("Input cannot be empty.")
        # Remove spaces and special characters
        cleaned_text = ""
        for char in text.lower():
            if char.isalnum():
                cleaned_text += char
        # Check palindrome
        if cleaned_text == cleaned_text[::-1]:
            result = "It is a Palindrome"
        else:
            result = "It is NOT a Palindrome"
        palindrome_result.config(text=result)
        save_history("Palindrome", text, result)    
    except ValueError as error:                                              
        messagebox.showerror("Invalid Input", str(error))

# ANAGRAM FUNCTION
def check_anagram():
    text1 = anagram_entry1.get()
    text2 = anagram_entry2.get()
    try:
        if text1.strip() == "" or text2.strip() == "":
            raise ValueError("Both fields must be filled.")
        # Remove spaces and special characters
        cleaned1 = ""
        cleaned2 = ""
        for char in text1.lower():
            if char.isalnum():
                cleaned1 += char
        for char in text2.lower():
            if char.isalnum():
                cleaned2 += char
        # Count characters using dictionaries
        count1 = {}
        count2 = {}
        for char in cleaned1:
            count1[char] = count1.get(char, 0) + 1
        for char in cleaned2:
            count2[char] = count2.get(char, 0) + 1
        if count1 == count2:
            result = "They are Anagrams!"
        else:
            result = "They are NOT Anagrams"
        anagram_result.config(text=result)
        save_history("Anagram", text1 + " / " + text2, result)    
    except ValueError as error:
        messagebox.showerror("Invalid Input", str(error))

# SAVE HISTORY
def save_history(check_type, text, result):
    try:
        with open("checker_history.txt", "a" , encoding = "utf-8") as file:
            file.write(f"{check_type}: {text} -> {result}\n")
    except Exception as error:
        messagebox.showerror("File Error", f"Could not save history.\n{error}")

# CLEAR FUNCTION
def clear_all():
    palindrome_entry.delete(0, tk.END)
    anagram_entry1.delete(0, tk.END)
    anagram_entry2.delete(0, tk.END)
    palindrome_result.config(text="")
    anagram_result.config(text="")

# MAIN WINDOW
root = tk.Tk()
root.title("Palindrome & Anagram Checker")
root.geometry("600x600")
root.resizable(False, False)

#TITLE
title = tk.Label(root,text="Palindrome & Anagram Checker",font=("Arial", 22, "bold"))
title.pack(pady=20)

# PALINDROME SECTION
palindrome_frame = tk.LabelFrame(root,text="Palindrome Checker",font=("Arial", 19, "bold"),padx=15,pady=15)
palindrome_frame.pack(padx=30, pady=10, fill="x")
tk.Label(palindrome_frame,text="Enter a word or sentence:").pack()
palindrome_entry = tk.Entry(palindrome_frame,width=50,font=("Arial", 18))
palindrome_entry.pack(pady=8)
tk.Button(palindrome_frame,text="Check Palindrome",command=check_palindrome,width=20).pack(pady=5)
palindrome_result = tk.Label(palindrome_frame,text="",font=("Arial", 18, "bold"))
palindrome_result.pack(pady=5)

# ANAGRAM SECTION
anagram_frame = tk.LabelFrame(root,text="Anagram Checker",font=("Arial", 19, "bold"),padx=15,pady=15)
anagram_frame.pack(padx=30, pady=10, fill="x")
tk.Label(anagram_frame,text="Enter first word/sentence:").pack()
anagram_entry1 = tk.Entry(anagram_frame,width=50,font=("Arial", 18))
anagram_entry1.pack(pady=5)
tk.Label( anagram_frame,text="Enter second word/sentence:").pack()
anagram_entry2 = tk.Entry(anagram_frame,width=50,font=("Arial", 18))
anagram_entry2.pack(pady=5)
tk.Button(anagram_frame,text="Check Anagram",command=check_anagram,width=20).pack(pady=5)
anagram_result = tk.Label(anagram_frame,text="",font=("Arial", 18, "bold"))
anagram_result.pack(pady=5)

# BOTTOM BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
tk.Button(button_frame,text="Clear",command=clear_all,width=12).grid(row=0, column=0, padx=10)
tk.Button(button_frame,text="Exit",command=root.destroy,width=12).grid(row=0, column=1, padx=10)

root.mainloop()
