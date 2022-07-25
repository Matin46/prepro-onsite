"""Snack"""
def main():
    """yes"""
    o_money = int(input())
    water = int(input())
    snack_1 = int(input())
    snack_2 = int(input())
    snack_3 = int(input())
    money = o_money - water
    price1 = purchase(money, 1, snack_1)
    money -= price1
    price2 = purchase(money, 2, snack_2)
    money -= price2
    price3 = purchase(money, 3, snack_3)
    money -= price3
    if money >= 0:
        print("Now you have %d left." %int(money))
        print("Here’s your order!")
        print("Water: %d baht\n\
Snack number 1: %d baht\n\
Snack number 2: %d baht\n\
Snack number 3: %d baht" %(int(water), int(price1), int(price2), int(price3)))
    else:
        print("Now you have %d left.\nYou don’t have enough money!" %o_money)

def purchase(money, snack, amount):
    """do the snack"""
    if snack == 1:
        if money % 3 == 0:
            return 10 * amount
        elif money % 3 == 1:
            return 15 * amount
        elif money % 3 == 2:
            return 20 * amount
    if snack == 2:
        if money % 3 == 0:
            return 12 * amount
        elif money % 3 == 1:
            return 15 * amount
        elif money % 3 == 2:
            return 18 * amount
    if snack == 3:
        if money % 3 == 0:
            return 5 * amount
        elif money % 3 == 1:
            return 7 * amount
        elif money % 3 == 2:
            return 9 * amount
main()
