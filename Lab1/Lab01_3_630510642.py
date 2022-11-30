#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab01_3

def main():
    w = float(input())
    h = float(input())
    fncal_bmi(w,h)

def fncal_bmi(w,h):
    w = w/2.2
    h = h*30.48
    h /= 100
    BMI = w/(h**2)
    print("%.2f"%(BMI))

if __name__ == '__main__':
    main()