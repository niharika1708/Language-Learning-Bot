import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from gtts import gTTS
import os

# Function to load data from an Excel file
def load_data(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        print("Excel file loaded successfully.")
        return dict(zip(df['English'], df['Hindi']))
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        messagebox.showerror("Error", f"Error loading Excel file: {e}")
        return {}

# Function to translate and pronounce
def translate_and_pronounce():
    english_phrase = entry.get().lower().strip()
    hindi_translation = english_to_hindi.get(english_phrase, "Translation Not Found")
    output_label.config(text=hindi_translation)

    if hindi_translation != "Translation Not Found":
        try:
            tts = gTTS(text=hindi_translation, lang='hi')
            audio_file = "translation.mp3"
            tts.save(audio_file)
            if os.name == 'nt':  # For Windows
                os.system(f'start {audio_file}')
            else:  # For Unix-based systems
                os.system(f'open {audio_file}')
        except Exception as e:
            print(f"Error generating or playing audio: {e}")
            messagebox.showerror("Error", f"Error generating or playing audio: {e}")

# Function to open a file dialog and load a new dataset
def open_file():
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        global english_to_hindi
        english_to_hindi = load_data(file_path)

# Main GUI application
root = tk.Tk()
root.title("English to Hindi Translator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter English Phrase:").grid(column=1, row=1, sticky=tk.W)
entry = ttk.Entry(frame, width=50)
entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

translate_button = ttk.Button(frame, text="Translate", command=translate_and_pronounce)
translate_button.grid(column=2, row=2, sticky=tk.W)

output_label = ttk.Label(frame, text="")
output_label.grid(column=1, row=3, columnspan=2, sticky=(tk.W, tk.E))

load_button = ttk.Button(frame, text="Load New Dataset", command=open_file)
load_button.grid(column=2, row=4, sticky=tk.E)

# Initialize with a default dataset
english_to_hindi = load_data('nlp hack dataset1.xlsx')

root.mainloop()