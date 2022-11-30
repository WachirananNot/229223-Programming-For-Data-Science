#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab04_4

def xy_factors(x,y,n):
    count = 0
    for i in range (1,n+1):
        if i%x ==0 or i%y ==0:
            count +=1

    return count
def main():
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    n = int(input("Enter n:"))
    print(xy_factors(x,y,n))
    main()

if __name__ == "__main__":
    main()