import scryfallCardGetter
from PIL import Image
from io import BytesIO
import tkinter as tk


cardData = scryfallCardGetter.getRandom()
img = cardData['image']
img = Image.open(BytesIO(img))
img.save(f"card{i}.png", 'png')

name = cardData['name']
text = cardData['text']
typeline = cardData['typeline']