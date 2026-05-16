import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src = src_lang.get()
    dest = dest_lang.get()
    if text:
        result = GoogleTranslator(source=src, target=dest).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

root = tk.Tk()
root.title("Language Translator - CodeAlpha")
root.geometry("500x400")

tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5)
input_text.pack()

tk.Label(root, text="Source Language (e.g. en):").pack()
src_lang = tk.Entry(root)
src_lang.insert(0, "en")
src_lang.pack()

tk.Label(root, text="Target Language (e.g. ur):").pack()
dest_lang = tk.Entry(root)
dest_lang.insert(0, "ur")
dest_lang.pack()

tk.Button(root, text="Translate", command=translate_text).pack(pady=10)

tk.Label(root, text="Translation:").pack()
output_text = tk.Text(root, height=5)
output_text.pack()

root.mainloop()