def main():
    print("calculadora")
    print("")
    print("Opciones de ingreso:")
    print("")
    print("Aplicar raíz: 1")
    print("")
    print("Ingresar un número: 2")
    print("")

    selector=int(input("Ingrese: "))
    while(selector > 2 or selector < 1):
        selector = int(input("ERROR! Ingrese valores válidos (1-2): "))

    if (selector==1):
        print("")
        raiz=float(input("Ingrese raíz: "))
        while (raiz <= 0):
            print("")
            raiz=float(input("ERROR! Ingrese raíz válida: "))
        print("")
        num=float(input("Ingrese un número positivo: "))
        while (num <= 0):
            print("")
            num=float(input("ERROR! Ingrese un número positivo: "))
        resultado = num ** (1/raiz)
    else: 
        print("")
        resultado=float(input("Ingrese un número: "))

    print("")
    print(resultado)
    print("")
    print("Opciones de operaciones: ")
    print("")
    print("Suma: 1")
    print("")
    print("Resta: 2")
    print("")
    print("Multiplicar: 3")
    print("")
    print("Dividir: 4")
    print("")
    print("Potenciar: 5")

    print("")
    selector=int(input("Ingrese: "))
    while(selector > 5 or selector < 1):
        print("")
        selector = int(input("ERROR! Ingrese valores válidos (1-5): "))
    
    if (selector==1):
        print("")
        num=float(input("Ingrese un número para sumar al anterior"))
        resultado += num
    if (selector==2):
        print("")
        num=float(input("Ingrese un número para restar al anterior"))
        resultado -= num
    if (selector==3):
        print("")
        num=float(input("Ingrese un número para multiplicar al anterior"))
        resultado *= num
    if (selector==4):
        print("")
        num=float(input("Ingrese un número para multiplicar al anterior"))
        resultado /= num
    else:
        print("")
        num=float(input("Ingrese un número para potenciar al anterior"))
        

    print("")
    print(resultado)
main()