#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab07_2

def sum_number(list_x):
    sum_ = 0
    for i in list_x:
        if isinstance(i,int) or isinstance(i,float):
            sum_ += i
    return sum_

def main():
    list_x = [34.65, 65.22, "FB", 'IG', 'Tiktok']
    print(sum_number(list_x))

if __name__ == "__main__":
    main()