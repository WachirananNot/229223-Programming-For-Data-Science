#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab02_3

import math

def fncal_all_area(n):
    Square = n*n
    BC = 4*fncal_cycle_area((n/2)/2)
    SC = 3*fncal_cycle_area(((n/4)*(math.sqrt(2)-1))/2)
    result = Square-(BC+SC)
    
    print("%.2f"%(Square))
    print("%.2f"%(BC))
    print("%.2f"%(SC))
    print("%.2f"%(result))
def fncal_cycle_area(r):
    return(math.pi*r*r)

def main():
    n = int(input())
    fncal_all_area(n)

if __name__ == '__main__':
    main()