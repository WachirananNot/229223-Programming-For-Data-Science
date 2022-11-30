#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab07_3

def list_number(n):
    num = [(2*x)+1 for x in range(n)]
    return num

def main():
    n = int(input("Enter n: "))
    print(list_number(n))

if __name__ == "__main__":
    main()
