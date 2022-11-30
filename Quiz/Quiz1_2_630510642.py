#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Quiz1_2

def show_series(a,b):
    if a>0 and b>0 and a!=b:
        if a<b:
            for i in range(a,b+1):
                print(i)
        elif a>b:
            for i in range(a,b-1,-1):
                print(i)
    else:
        print(0)

def main():
    a = int(input())
    b = int(input())
    show_series(a,b)

if __name__ == "__main__":
    main()