#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Quiz1_1
def leap_year(y,m):
    leap = True
    if y%400 == 0 and y%100 == 0:
        print("Leap Year")
    elif y%100 == 0 and y%4 == 0:
        print("Non Leap Year")
        leap = False
    elif y%4==0:
        print("Leap Year")
    else:
        print("Non Leap Year")
        leap = False

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print("31")

    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("30")
    else:
        if leap == True:
            print("29")
        else:
            print("28")


def main():
    y = int(input())
    m = int(input())
    leap_year(y,m)

if __name__ == "__main__":
    main()