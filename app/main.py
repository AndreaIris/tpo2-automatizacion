from calculator import add, subtract, multiply, divide


def main():
    print("Calculadora simple")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")

    option = input("Elegí una opción: ")

    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))

    if option == "1":
        print(add(num1, num2))
    elif option == "2":
        print(subtract(num1, num2))
    elif option == "3":
        print(multiply(num1, num2))
    elif option == "4":
        try:
            print(divide(num1, num2))
        except ValueError as error:
            print(error)
    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()