#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab01_1

def main():
    x = int(input())
    fncal_area(x)

def fncal_area(n):
    pi = 3.141593
    bSquare = n*n
    sCircle = pi*((n/4)**2)
    SmC = bSquare-(sCircle*4)
    print("%.2f"%(bSquare))
    print("%.2f"%(sCircle))
    print("%.2f"%(SmC))

if __name__ == '__main__':
    main()