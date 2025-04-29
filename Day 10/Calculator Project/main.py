import  art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def calculate():
    print(art)
    continue_with_results = True
    num1 = float(input("What is your first number?: "))
    while continue_with_results:

        for symbol in operations:
            print(symbol)

        operations_choice = input("Please choose your operation ")

        num2 = float(input("What is your second number?: "))
        answer = operations[operations_choice](num1,num2)
        print(f' {num1} {operations_choice} {num2} = {answer}')

        save_results = input(f'Do you want to continue with {answer}?? (y or n)' ).lower()
        if save_results == "y":
            num1 = answer
        else:
            continue_with_results = False
            print(" \n" * 20)
            calculate()
calculate()


