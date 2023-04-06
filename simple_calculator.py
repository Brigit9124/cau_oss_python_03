def arithmetic_ops(op):
    num1 = int(input("input first number:"))
    num2 = int(input("input second number:"))
    return num1, num2, op(num1,num2)

def add(x,y): return x+y
def sub(x,y): return x-y

while True:
    op = input("input operation")
    if op == "end":
        break
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add)
    elif op == "-":
        num1,num2,ret = arithmetic_ops(sub)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda x,y:x*y)
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda x,y:x/y)
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda x,y:x%y)
    else:
        print("오류")
        continue
    print(f"{num1}{op}{num2} = {ret}")
print("Exit Program")
