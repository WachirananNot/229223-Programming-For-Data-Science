#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab02_5

def net_price(price1,price2,price3):
    price1 = cal_price(price1,0.05)
    price2 = cal_price(price2,0.10)
    price3 = cal_price(price3,0.20)
    sum_p = price1+price2+price3
    print("%.2f %.2f %.2f %.2f"%(price1,price2,price3,sum_p))

def cal_price(price,discount):
    price -= price*discount
    price += price*0.07
    return price


def main():
    price1 = int(input())
    price2 = int(input())
    price3 = int(input())
    net_price(price1,price2,price3)

if __name__ == '__main__':
    main()