import calc
import fina

gastos = []

while True:
    print("=== MENU ===")
    print("1 - Calculadora")
    print("2 - Financeiro")
    print("0 - Sair")
    
    op = input("Escolha: ")
    
    if op == "1":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        
        escolha = input("Operação: ")
        
        if escolha == "1":
            print("Resultado:", calc.calculadora(a, b, 'soma'))
        elif escolha == "2":
            print("Resultado:", calc.calculadora(a, b, 'subtracao'))
        elif escolha == "3":
            print("Resultado:", calc.calculadora(a, b, 'multiplicacao'))
        elif escolha == "4":
            print("Resultado:", calc.calculadora(a, b, 'divisao'))
    
    elif op == "2":
        fina.financeiro(gastos)
    
    elif op == "0":
        print("Saindo...")
        break