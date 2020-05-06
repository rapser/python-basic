# modulos propios
# modulos de terceros
# modulos de python

# se debe especificar el archivo y el metodo
# import datetime
# print(datetime.date.today())
# print(datetime.timedelta(minutes=80))

# solo invocamos al metodo
# from fmath import add
# print(add(5,9))

from colorama import init, Fore, Back, Style
init()

print(Fore.YELLOW + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
