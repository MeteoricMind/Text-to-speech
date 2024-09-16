import tkinter as tk
from gtts import gTTS
from googletrans import Translator
import os

# Function to translate text to the desired language
def translate_text(text, target_language_code):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language_code)
        return translated.text
    except Exception as e:
        return "Translation error: " + str(e)

# Function to convert text to speech
def text_to_speech():
    user_text = text_entry.get()
    language_code = language_var.get()
    if user_text:
        try:
            translated_text = translate_text(user_text, language_code)
            tts = gTTS(translated_text, lang=language_code)
            tts.save("output.mp3")
            os.system("start output.mp3")
            result_label.config(text="Translated Text: " + translated_text)
        except Exception as e:
            result_label.config(text="An error occurred: " + str(e))

# Main program
if __name__ == "__main__":
    print("Multilingual Text-to-Speech Converter")

    root = tk.Tk()
    root.title("Text-to-Speech Converter")

    # Create a label
    label = tk.Label(root, text="Enter the text you want to hear:")
    label.pack(pady=10)

    # Create a text entry field
    text_entry = tk.Entry(root, width=40)
    text_entry.pack()

    # Create a label for language selection
    language_label = tk.Label(root, text="Select Language:")
    language_label.pack(pady=5)

    # Language options (language code, language name)
    languages = [
        ("en", "English"),
        ("es", "Spanish"),
        ("fr", "French"),
        ("hi", "Hindi"),
        ("ja", "Japanese"),
        ("te", "Telugu"),
        ("ta", "Tamil")
    ]

    # Create a variable to store the selected language
    language_var = tk.StringVar()
    language_var.set("en")  # Set a default language

    # Create radio buttons for language selection
    for lang_code, lang_name in languages:
        lang_radio = tk.Radiobutton(root, text=lang_name, variable=language_var, value=lang_code)
        lang_radio.pack()

    # Create a button to trigger conversion
    convert_button = tk.Button(root, text="Convert", command=text_to_speech)
    convert_button.pack(pady=10)

    # Create a label for displaying the result
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
