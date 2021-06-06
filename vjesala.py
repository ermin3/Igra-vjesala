import csv
import random

rijec = []
emoji = ['\U0001F600', '\U0001F605', '\U0001F642', '\U0001F914', '\U0001F928', '\U0001F915', '\U0001F631',
         '\U0001F92C', ]
win = '\U0001F973'


def rijeci():
    with open('py.csv', 'r', newline='')as py:
        read = csv.reader(py, delimiter=',')
        for line in read:
            rijec.append(''.join(line))
    return rijec


def igra():
    crtice = []
    pogodi = random.choice(rijec)
    for i in pogodi:
        crtice.append('_')

    bir_slova = []
    rijeci()
    brojac = -1
    while '_' in crtice:
        print(' '.join(crtice))
        unos = str(input('pogodi slovo')).upper()

        if unos.lower() in bir_slova:
            print(f'Slovo {unos} ste vec birali\n')

        elif unos.lower() in pogodi:
            for i in range(0, len(pogodi)):
                if unos.lower() == pogodi[i]:
                    crtice[i] = unos.upper()
            bir_slova.append(unos)

        elif unos.lower() not in pogodi:
            brojac += 1
            if brojac == 7:
                print('LOSERRRR', emoji[brojac] * 10, 'LOSERRRRR')
                break
            else:
                print(emoji[brojac])

            bir_slova.append(unos)
        print('Ova slova si vec birao', bir_slova)
        if '_' not in crtice:
            print('win', win * 10, 'win')


ponovo = 'da'
while ponovo == 'da':
    rijeci()
    igra()
    ponovo = input('Zelis pogati ponovo da/ne:')
