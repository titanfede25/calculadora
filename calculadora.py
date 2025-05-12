def main():

    print("calculadora")
    print("")
    resultado=float(input("Ingrese un número: "))

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
    print("Aplicar raíz: 6")
    print("")

    selector=int(input("Ingrese: "))
    while(selector > 6 or selector < 1):
        print("")
        selector = int(input("ERROR! Ingrese un valor válido(1-6): "))
    
    if (selector==1):
        print("")
        num=float(input("Ingrese un número para sumar al anterior: "))
        resultado += num
    if (selector==2):
        print("")
        num=float(input("Ingrese un número para restar al anterior: "))
        resultado -= num
    if (selector==3):
        print("")
        num=float(input("Ingrese un número para multiplicar al anterior: "))
        resultado *= num
    if (selector==4):
        print("")
        num=float(input("Ingrese un número para dividir al anterior: "))
        resultado /= num
    if (selector==5):
        print("")
        num=int(input("Ingrese un número entero para potenciar al anterior: "))
        resultado2 = resultado
        for i in range (num-1):
            resultado2=resultado2*resultado
        if num<0:
            resultado2 = 1/resultado2#no funciona
        resultado=resultado2
    if(selector==6):
        print("")
        raiz=int(input("Ingrese raíz: "))
        while (raiz <= 0):
            print("")
            raiz=int(input("ERROR! Ingrese raíz válida: "))
        if (raiz%2==0 and resultado<0):
            print("ERROR! Esta cálculo es inválido matemáticamente")
        else:
            resultado = resultado ** (1/raiz)
    print("")
    print(resultado)

main()