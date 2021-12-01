def defNumbers():
    while True:
        try:
            n1 = float(input('Digite o primeiro número  '
                    )
                )

            if n1:
                break
        except (ValueError, TypeError):
            print(f'ERRO, Por favor, digite um número válido  ')
    while True:
        try:
            n2 = float(input('Digite o segundo número  '
                    )
                )

            if n2:
                break
        except (ValueError, TypeError):
            print(f'Erro, Por favor, digite um número válido')
    return (n1, n2)


def sum():
    num = defNumbers()
    resultado = num[0] + num[1]
    print(f'o resultado é {resultado:.0f}')


def subtract():
    num = defNumbers()
    resultado = num[0] - num[1]
    print(f'o resultado é {resultado:.0f}')


def multiply():
    num = defNumbers()
    resultado = num[0] * num[1]
    print(f'o resultado é {resultado:.0f}')


def divide():
    try:
        num = defNumbers()
        resultado = num[0] / num[1]
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    print(f'o resultado é {resultado:.0f}')


operation = 0
function = (sum, subtract, multiply, divide)
while True:
    print(f'=-' * 15)
    print(f'Bem-Vindo a calculadora Python')
    print(f'=-' * 15)
    print()
    while True:
        operation = -1
        try:
            operation += int(input('Qual operação deseja realizar?\n 1 Para somar\n 2 Para subtrair\n 3 Para multiplicar\n 4 para dividir\n 5 para sair\n'
                    )
                )
            if operation != -1:
                break

        except (ValueError, TypeError,):
            print(f'Erro, digite um número válido\n'
                    )
    if operation == 4:
        break
    function[operation]()
print(f'ADIÓS')
    
    
