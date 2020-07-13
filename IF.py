is_hot = True
is_cold = True
if is_hot:
    print("It is burning outside")
    print("Drink cold water")
elif is_cold:
    print("It is chilly, wear warm clothes")
elif is_cold & is_hot:
    print("Someone call the doctor")
else:
    print("Drink water and shejeje")

housePrice = 1000000
good_credit = True
if good_credit:
    pay = housePrice * 0.1
else:
    pay = housePrice * 0.2
print(f"Pay: ${round(pay)}")