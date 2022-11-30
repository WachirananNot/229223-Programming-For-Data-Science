#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab04_5

def triangle(n):
    j = 1
    for i in range(n,0,-1):
        print(" "*(i-1)+("*"*(j)))
        j+=2
def main():
    n = int(input("Enter star number: "))
    triangle(n)
    main()

if __name__ == "__main__":
    main()
