import scryfallCardGetter
from PIL import Image, ImageTk, ImageFont, ImageDraw
from io import BytesIO
import tkinter as tk
import textwrap
import threading
import time

global img
img = Image.open("blank card images/red.png").resize((298, 416))

def get_wrapped_text(text):
    #print(text)
    output_text = ""
    text_wrapped_list = textwrap.wrap(text, 35)
    for each in text_wrapped_list:
        output_text += f"{each}\n"
    return output_text

def get_dashed_text(text, charactersToShow = []):
    defaultCharactersToShow = [' ', '\n', ':', '{', '}', '-', "'", ',', '"', '.', '*', '/']
    charactersToShow.extend(defaultCharactersToShow)
    dashedText = ""
    for character in text:
        if character.upper() in charactersToShow or character.lower() in charactersToShow:
            dashedText += character
        else:
            dashedText += "_"

    wrappedText = get_wrapped_text(dashedText)
    return wrappedText

def add_spaces_between_characters(text):
    outputText = ""
    for each in text:
        outputText += f"{each} "
    return outputText

def runWindow():
    global img
    global root
    root = tk.Tk()
    root.geometry("298x416")
    tk_image = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_image, compound='center')
    label.pack()
    root.mainloop()

card_data = scryfallCardGetter.getRandom()
correct_card_image = card_data['image']
correct_card_image = Image.open(BytesIO(correct_card_image))
name = card_data['name']
text = card_data['text']
typeline = card_data['typeline']
mana_cost = card_data['mana_cost']
stats = f"{card_data['power']}/{card_data['toughness']}"
pressedCharacters = []
windowThread = threading.Thread(None, runWindow)
windowThread.start()
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i = 0
while True:
    dashedText = get_dashed_text(text, pressedCharacters)
    img = Image.open("blank card images/artifact.png")
    img = img.resize((298, 416))
    name_font = ImageFont.truetype("arial.ttf", 18)
    text_font = ImageFont.truetype("calibri.ttf", 12)
    edit_image = ImageDraw.Draw(img)
    edit_image.text((26, 23), name, ("black"), font=name_font)
    edit_image.text((28, 265), dashedText, ("black"), font=text_font)
    try:
        pressedCharacters += letters[i]
    except:
        pass
    time.sleep(2)
    i += 1