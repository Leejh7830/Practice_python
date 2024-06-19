def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by Zero."
    return x / y


def calculator():
    print("원하는 계산의 번호를 입력하세요..")
    print("1. 더하기(Add)")
    print("2. 빼기(Sub)")
    print("3. 곱하기(multi)")
    print("4. 나누기(Div)")

    while True:
        choice = input("1,2,3,4 중에 입력하세요: ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("첫번째 수 입력: "))
            num2 = float(input("두번째 수 입력: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("추가로 다른 계산을 할까요?(yes/no): ")
            if next_calculation.lower() != 'yes':  # Yes 가 아니면
                break
        else:
            print("잘못된 입력입니다.")

