#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab01_2

def main():
    x = int(input())
    fncal_shade_area(x)
    main()

def fncal_shade_area(n):
    Square = 3*n*n
    r = n/8
    pi = 3.141593
    miniC = pi*r*r
    sum_C = miniC*16*3
    Square -= sum_C
    print("%.2f"%(Square))


if __name__ == '__main__':
    main()