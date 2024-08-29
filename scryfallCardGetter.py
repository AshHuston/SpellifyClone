import requests


def getRandom():
    url = 'https://api.scryfall.com/cards/random'
    while(True):
        request = requests.get(url)
        card_json = request.json()
        if card_json['type_line'] != None:
            break

    if 'name' in card_json:
        cardname = card_json['name']
    else:
        cardname = None

    if 'mana_cost' in card_json:
        mana_cost = card_json['mana_cost']
    else:
        mana_cost = None

    if 'type_line' in card_json:
        typeline = card_json['type_line']
    else:
        typeline = None

    if "oracle_text" in card_json:
        oracle_text = card_json['oracle_text']
    else:
        oracle_text = None

    if "power" in card_json:
        power = card_json['power']
    else:
        power = None

    if "toughness" in card_json:
        toughness = card_json['toughness']
    else:
        toughness = None

    if "loyalty" in card_json:
        loyalty = card_json['loyalty'] 
    else:
        loyalty = None

    if "defense" in card_json:
        battle_defense = card_json['defense'] 
    else:
        battle_defense = None

    if 'image_uris' in card_json:
        imageURI = card_json['image_uris']['png']
        image = requests.get(imageURI).content

    cardInfo = {
        'name': cardname,
        'mana_cost': mana_cost,
        'typeline': typeline,
        'text': oracle_text,
        'power': power, 
        'toughness': toughness,
        'loyalty': loyalty,
        'battle_defense': battle_defense,
        'image': image
    }
    return cardInfo

#print(getRandom())