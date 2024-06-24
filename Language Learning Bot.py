# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xFmjo00NEy5w1c4bdY2gwvzYYQ-ZmCtS
"""

!pip install pandas openpyxl

!pip install gTTS

import pandas as pd
from gtts import gTTS
from IPython.display import Audio, display, HTML
import re
import time

# Load data from Excel file
df = pd.read_excel('hindi basic.xlsx', engine='openpyxl')

# Function to check if a string contains Hindi characters
def contains_hindi(text):
    # Regular expression to match Hindi characters
    hindi_pattern = re.compile("[\u0900-\u097F\u0975-\u097F]+")
    return bool(hindi_pattern.search(text))

# Function to pronounce Hindi words sequentially
def pronounce_hindi_words(words):
    for word in words:
        if contains_hindi(word):
            # Generate audio pronunciation
            tts = gTTS(text=word, lang='hi')
            tts.save('pronunciation.mp3')

            # Display underlined text and play audio
            display(HTML(f"<u>{word}</u>"))
            display(Audio('pronunciation.mp3', autoplay=True))

            # Pause between pronunciations (adjust as needed)
            time.sleep(2)  # Pause for 2 seconds between each word

            # Ask user if they want to exit
            exit_input = input("Enter 'exit' to stop pronunciation, or press Enter to continue: ").strip().lower()
            if exit_input == 'exit':
                break

# Function to choose alphabets or numbers
def choose_category():
    while True:
        category = input("Choose category (alphabets/numbers): ").strip().lower()
        if category == 'alphabets':
            return df['Alphabets'].tolist()  # Assuming 'Hindi' column contains Hindi alphabets
        elif category == 'numbers':
            return df['Numbers'].tolist()  # Assuming 'Numbers' column contains Hindi numbers
        else:
            print("Invalid category. Please choose 'alphabets' or 'numbers'.")

# Choose category (alphabets or numbers)
selected_words = choose_category()

# Pronounce selected words sequentially
pronounce_hindi_words(selected_words)

import pandas as pd
from gtts import gTTS
import IPython.display as ipd

# Load data from Excel file using openpyxl engine
df = pd.read_excel('nlp hack dataset1.xlsx', engine='openpyxl',usecols=['English', 'Hindi'])

# Display the first few rows to verify data
print(df.head())

# Assuming df contains two columns: 'English' and 'Hindi'
english_phrases = df['English'].tolist()
hindi_phrases = df['Hindi'].tolist()

# Create a dictionary for mapping English to Hindi
english_to_hindi = dict(zip(english_phrases, hindi_phrases))

# Function to translate English to Hindi and pronounce it
def translate_and_pronounce(english_phrase):
    # Lookup in the dictionary; return None if not found
    hindi_translation = english_to_hindi.get(english_phrase, "Translation Not Found")

    # Generate speech in Hindi
    tts = gTTS(text=hindi_translation, lang='hi')

    # Save speech to a temporary file
    tts.save("translation.mp3")

    # Play the generated speech
    return ipd.Audio("translation.mp3", autoplay=True)

# Interactive loop for user input
while True:
    # Take input from the user
    user_input = input("You: ").strip().lower()

    # Exit condition
    if user_input == 'exit':
        print("Chatbot: Bye!")
        break

    # Translate and pronounce the input
    if user_input in english_to_hindi:
        hindi_translation = english_to_hindi[user_input]
        print(f"Chatbot: {hindi_translation}")
        audio_output = translate_and_pronounce(user_input)
        display(audio_output)
    else:
        print("Chatbot: I don't know that phrase yet. You can teach me!")