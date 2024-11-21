saida = ''

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao in ('+', 'adicao'):
        return adicao(num1, num2)
    elif operacao in ('-', 'subtracao'):
        return subtracao(num1, num2)
    elif operacao in ('*', 'multiplicacao'):
        return multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        return divisao(num1, num2)
    else:
        return "Operação inválida. Tente novamente."

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou nome): ").lower()
        resultado = calculadora(num1, num2, operacao)
        print("Resultado da operação:", resultado)
        
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        
    saida = input("Deseja continuar? (S/N): ").lower()  
    
    if saida not in ('s', 'n'):
        print("Resposta inválida! Considere apenas S ou N.")