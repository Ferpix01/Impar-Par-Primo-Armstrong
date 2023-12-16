import math #Importa a biblioteca math para fins matemáticos

def eh_par(num): #Verifica se o número é divisível por 2 para saber se é par
    return num % 2 == 0

def eh_impar(num): #Verifica se o número é divisível por 2 para saber se é ímpar
    return num % 2 != 0

def eh_primo(num): #Verifica se é um número inteiro
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def eh_narcisista(num): #Checa se o número é Armstrong/Narcisista
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

def calculadora(num):
    if eh_par(num):
        print(f'{num} é par.')
    else:
        print(f'{num} é ímpar.')

    if eh_primo(num):
        print(f'{num} é primo.')
    else:
        print(f'{num} não é primo.')

    if eh_narcisista(num):
        print(f'{num} é narcisista.')
    else:
        print(f'{num} não é narcisista.')

calculadora(153) #Define o número