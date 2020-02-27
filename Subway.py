#subway chicken tendies

from time import sleep
from random import randint

breads = ['9-Grain Wheat','Italian','Hearty Italian','Flatbread']
salads = ['salad kind']
meats = ['meat']
premade_sandwiches = []

def in_Stock(to_check,compare_with):
    for x in compare_with:
        if x.lower() == to_check.lower():
            return True
        elif to_check.lower == 'none':
            return True
    return False

def welcome():
    print('hello welcome to subway')
    while True:
        bread = input('What bread would you like? ')
        if in_Stock(bread,breads):
            break
        elif not(in_Stock(bread,breads)):
            print('That bread is not in stock')
            continue
        
    print('ok')
    while True:
        meat = input('What meat would you like? ')
        if in_Stock(meat,meats):
            break
        elif not(in_Stock(meat,meats)):
            print('We dont have that in stock')
            continue
    print('ok')
    while True:
        salad = input('What salad would you like? ')
        if in_Stock(salad,salads):
            break
        elif not(in_Stock(salad,salads)):
            print('That salad is not in stock')
            continue
    print('ok')

def payment(bread,meat,salad):
    pass #make here compiles choices


welcome()
