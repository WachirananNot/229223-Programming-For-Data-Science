#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab02_4

def fncal_shaded_area(a,b):
    print("%.2f %.2f"%(triangle_area(a,b),square_area(a)-triangle_area(a,b)))

def square_area(a):
    return a*a

def triangle_area(a,b):
    return (((4*(b**2)-(a**2))**0.5)*(a/4))

def main():
    a,b = input().split(',')
    a = float(a)
    b = float(b)
    fncal_shaded_area(a,b)
    
if __name__ == '__main__':
    main()