from fatsecret import Fatsecret

consumer_key = 'acb25fdc66d84c7e8583de30cf976c4f'
consumer_secret = '7e6e661c41a94f538ab74bcfae08b63a'


fs = Fatsecret(consumer_key, consumer_secret)

foods = fs.foods_search("Hormel Bacon")

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

print('This '+ brand + ' ' + name + ' has ' + fat_str + ' ' + carb_str + ' ' + prot_str)
'''
fat = seg[1].replace('Fat: ','').replace('g','')
carb = seg[2].replace('Carbs: ','').replace('g','')
prot = seg[3].replace('Protein: ','').replace('g','')
tot = seg[0]
print(food['brand_name'] + ' ' + food['food_name'] + ' ' + 'Carbs: ' + carb + 'Fat: ' + fat + 'Protien: ' + prot)

    fat = float(fat)
    carb = float(carb)
    prot = float(prot)
    fat_cal = fat * 9
    carb_cal = carb * 4
    prot_cal = prot * 4
    total = fat_cal + carb_cal + prot_cal

    carb_perc = carb_cal / total
    carb_perc = carb_perc * 100
    carb_perc = round(carb_perc, 2)
    '''
