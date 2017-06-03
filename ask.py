from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
from fatsecret import Fatsecret

consumer_key = 'acb25fdc66d84c7e8583de30cf976c4f'
consumer_secret = '7e6e661c41a94f538ab74bcfae08b63a'
fs = Fatsecret(consumer_key, consumer_secret)

app = Flask(__name__)
ask = Ask(app, "/macros")

def get_macros():
    consumer_key = 'acb25fdc66d84c7e8583de30cf976c4f'
    consumer_secret = '7e6e661c41a94f538ab74bcfae08b63a'
    fs = Fatsecret(consumer_key, consumer_secret)

    foods = fs.foods_search("Hormel bacon")
    food = foods[0]

    brand = food['brand_name']
    name = food['food_name']
    desc = food['food_description']
    desc = desc.split('|')
    desc = desc[1:]

    fat = desc[0].replace(' Fat: ','').replace('g','')
    carb = desc[1].replace(' Carbs: ','').replace('g','')
    prot = desc[2].replace(' Protein: ','').replace('g','')

    fat_str = '{} grams of fat'.format(fat)
    carb_str = '{} grams of carbs'.format(carb)
    prot_str = 'And {} grams of protien'.format(prot)

    text = 'This '+ brand + ' ' + name + ' has ' + fat_str + ' ' + carb_str + ' ' + prot_str

    return text


@app.route('/')
def homepage():
    return "how's it going today?"

@ask.launch
def start_skill():
    welcome_message = "What's up?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_macros():
    macros = get_macros()
    macro_msg = 'The macros for {}'.format(macros)
    return statement(macro_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "Ok...well I'm here if you need me."
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
