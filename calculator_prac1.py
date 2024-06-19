# add subtract multiply divide
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
        choice =
