def calculate(a, b, op):
    if op == "+":
        return a+b
    if op == "-":
        return a-b
    if op == "*":
        return a*b
    if op == "/":
        if b == 0:
            return "Nolga bolish mumkin emas!!!"
        return round(a/b) 
    else:
        return "Notogri operator"
print(calculate(10,5,"+"))
print(calculate(10,5,"-"))
print(calculate(10,5,"*"))
print(calculate(10,5,"/"))
print(calculate(10,0,"/"))
print(calculate(10,5,"%"))