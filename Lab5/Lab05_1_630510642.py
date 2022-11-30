#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab05_1

def multiple_table(n):
    if n>12 or n<0:
        print("Invalid Input")
    else:
        for i in range(1,n+1):
            for j in range(1,n+1):
                result = ("%4d"%(i*j))
                print(result,end="")
            print()
            
def main():
    n = int(input())
    multiple_table(n)

if __name__ == "__main__":
    main()