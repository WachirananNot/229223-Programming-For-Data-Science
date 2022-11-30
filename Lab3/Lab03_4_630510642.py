#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab03_4

def cal_bmi(w,h):
    if h*30.48 < 300:
        BMI = (w/((h*12)**2))*703

    else:
        BMI = (w)/((h/100)**2)

    print("%.1f"%(BMI))

def main():
    w = float(input())
    h = float(input())
    cal_bmi(w,h)

if __name__ == '__main__':
    main()