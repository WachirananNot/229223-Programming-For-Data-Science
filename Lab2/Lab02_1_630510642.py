#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab02_1

def main():
    n = int(input())
    draw_square(n)

def show_sharp_star(i,j):
    print("#"*i,"*"*j)

def draw_square(n):
    half = n//2
    double = 2*n

    show_sharp_star(double-half,half)
    show_sharp_star(n,n)
    show_sharp_star(0,double)
    show_sharp_star(n,n)
    show_sharp_star(double-half,half)

if __name__ == '__main__':
    main()
