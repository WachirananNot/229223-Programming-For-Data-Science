#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab05_5

def triangle_tree(n):
    for i in range(1,n+1):
        k = (n-1)*2
        for j in range(1,i+1):
            print(" "*(k)+"* "*((2*j)-1))
            k-=2
def main():
    n = int(input("Enter star number: "))
    triangle_tree(n)

if __name__ == "__main__":
    main()