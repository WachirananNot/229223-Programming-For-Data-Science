#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab08_4

def multiple_list(n):
    a = []
    if 1<=n<=12:
        for i in range(1,n+1):
            b = []
            k = 0
            for j in range(n):
                k += i
                b.append(k)
            a.append(b)
        return a
    else:
        return("Invalid Input")

def main():
    x = 10
    print(multiple_list(x))

if __name__ == "__main__":
    main()
