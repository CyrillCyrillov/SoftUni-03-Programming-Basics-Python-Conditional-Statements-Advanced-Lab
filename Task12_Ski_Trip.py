days = int(input())
type_of_room = input()
rating = input()
price = 0
discount = 0

if type_of_room == "room for one person":
    discount = 0
    price = 18
elif type_of_room == "apartment" and days < 10:
    discount = 0.3
    price = 25
elif type_of_room == "apartment" and 10 <= days <= 15:
    discount = 0.35
    price = 25
elif type_of_room == "apartment" and days > 15:
    discount = 0.5
    price = 25
elif type_of_room == "president apartment" and days < 10:
    discount = 0.1
    price = 35
elif type_of_room == "president apartment" and 10 <= days <= 15:
    discount = 0.15
    price = 35
elif type_of_room == "president apartment" and days > 15:
    discount = 0.20
    price = 35

total_price = (days - 1) * price * (1 - discount)

if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")
