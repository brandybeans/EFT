#!/usr/bin/env python3
import math

def get_currency():
    currency = ['USD', 'EUR']
    print("What currency are you selling at?")

    for x, y in enumerate(currency):
        print("  {}. {}".format(x+1, y))

    curselection = int(input(">>: "))
    curselection = currency[curselection-1]
    return curselection

def get_conversion_rate(type):
    print("What is value of 1 {} in RUB?".format(type))
    rate = int(input(">>: "))
    return rate

def get_sell_value():
    print("What is the value of the item(s) you are selling in rubles? Or type '0' to start over.")
    sell_value = int(input(">>: "))
    return sell_value

def get_conv_sell_value(type,rate,sell_value):
    conv_sell_value = math.floor(sell_value / rate)
    return print("Sell the item at {} {}.".format(conv_sell_value, type))

def main():
    type = get_currency()
    rate = get_conversion_rate(type)
    while True:
        sell_value = get_sell_value()
        if sell_value == 0:
            break
        conv_sell_value = get_conv_sell_value(type,rate,sell_value)
    main()

if __name__ == "__main__":
    main()
