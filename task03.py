def calculate_tax(salary: int) -> dict:
    if 0 <= salary <= 5000000:
        rate=0
    if 5000001 <= salary <= 10000000:
        rate=12
    if 10000001 <= salary <= 20000000:
        rate=18
    if salary >= 20000001:
        rate=25
    tax=salary*rate//100
    net=salary-tax
    return  {
        "gross": salary,
        "tax": tax,
        "net": net,
        "rate": f"{rate}%"
    }
print(calculate_tax(6000000))