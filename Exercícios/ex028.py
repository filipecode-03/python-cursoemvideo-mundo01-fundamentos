from random import randint
from time import sleep
from colorama import Fore
com = randint(0, 5)
print(Fore.YELLOW + '-=-' * 20)
print(Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(Fore.YELLOW + '-=-' * 20)
jog = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jog == com:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! eu pensei no número {com} e não no {jog}!')