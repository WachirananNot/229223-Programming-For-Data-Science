#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab03_1

def main():
    number = int(input("Enter n number: "))
    result = divide_3and5(number)
    print(result)

def divide_3and5(n):
    if n%5 == 0 and n%3 == 0:
        return "Both"
    elif n%5 == 0:
        return "Five"
    elif n%3 == 0:
        return "Three"
    else:
        return "None"

if __name__ == '__main__':
    main()