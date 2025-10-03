def atm_operation(balance: int, action: str, amount: int)-> dict:
    if amount <= 0:
        return "Musbat son kiriting"
    if action == "deposit":
        balance+=amount
        return balance
    if action == "withdraw":
        if amount >= balance:
            return "Balans yetarli emas"
        balance -= amount
        return balance
    else:
        return "xatolikk!!!"
print(atm_operation(10000,"deposit",5000))
print(atm_operation(10000,"withdraw",5000))
print(atm_operation(10000,"deposit",-5000))
print(atm_operation(10000,"withdraw",50000))