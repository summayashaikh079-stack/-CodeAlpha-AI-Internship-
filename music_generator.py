import tkinter as tk
from music21 import stream, note, chord, tempo
import random

def generate_music():
    s = stream.Score()
    part = stream.Part()
    
    t = tempo.MetronomeMark(number=120)
    part.append(t)
    
    notes_list = ['C4','D4','E4','F4','G4','A4','B4','C5']
    
    for i in range(16):
        if random.random() > 0.3:
            n = note.Note(random.choice(notes_list))
            n.quarterLength = random.choice([0.5, 1, 2])
            part.append(n)
        else:
            r = note.Rest()
            r.quarterLength = 1
            part.append(r)
    
    s.append(part)
    s.write('midi', fp='generated_music.mid')
    result_label.config(text="Music generated! File: generated_music.mid ✅")

root = tk.Tk()
root.title("AI Music Generator - CodeAlpha")
root.geometry("400x200")

tk.Label(root, text="AI Music Generator", font=("Arial", 16)).pack(pady=20)
tk.Button(root, text="Generate Music 🎵", command=generate_music, 
          font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()