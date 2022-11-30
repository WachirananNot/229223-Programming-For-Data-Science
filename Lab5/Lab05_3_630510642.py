#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab05_3

def divide_3or7(m,n):
    last_number = None
    count_3 = 0
    count_7 = 0
    for i in range(m,n+1):
        if i%3 == 0:
            count_3 += 1
            last_number = i
        if i%7 == 0:
            count_7 += 1
            last_number = i
    return last_number,count_3,count_7

def main():
    m,n = input().split(" ")
    print(divide_3or7(int(m),int(n)))

if __name__ == "__main__":
    main()