#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab03_3

def main():
    price = float(input("Enter price: "))
    n = int(input("Enter N: "))
    money = int(input("Enter Money: "))
    credit_balance(price,n,money)

def credit_balance(price,n,money):
    s_price = price*n
    print("%.1f*%d=%.1f"%(price,n,s_price))

    balance = money - s_price
    if balance < 0:
        print("Not enough money")
    else:
        print("%.1f"%(balance))

if __name__ == '__main__':
    main()