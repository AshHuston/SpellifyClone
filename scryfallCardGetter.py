import requests


def getRandom():
    url = 'https://api.scryfall.com/cards/random'
    while(True):
        request = requests.get(url)
        cardJson = request.json()
        if cardJson['type_line'] != None:
            break

    if 'name' in cardJson:
        cardname = cardJson['name']
    else:
        cardname = None

    if 'mana_cost' in cardJson:
        manaCost = cardJson['mana_cost']
    else:
        manaCost = None

    if 'type_line' in cardJson:
        typeline = cardJson['type_line']
    else:
        typeline = None

    if "oracle_text" in cardJson:
        oracleText = cardJson['oracle_text']
    else:
        oracleText = None

    if "power" in cardJson:
        power = cardJson['power']
    else:
        power = None

    if "toughness" in cardJson:
        toughness = cardJson['toughness']
    else:
        toughness = None

    if "loyalty" in cardJson:
        loyalty = cardJson['loyalty'] 
    else:
        loyalty = None

    if "defense" in cardJson:
        battleDefense = cardJson['defense'] 
    else:
        battleDefense = None

    if 'image_uris' in cardJson:
        imageURI = cardJson['image_uris']['png']
        image = requests.get(imageURI).content

    cardInfo = {
        'name': cardname,
        'manaCost': manaCost,
        'typeline': typeline,
        'text': oracleText,
        'power': power, 
        'toughness': toughness,
        'loyalty': loyalty,
        'battleDefense': battleDefense,
        'image': image
    }
    return cardInfo

#print(getRandom())