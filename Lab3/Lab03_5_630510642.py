#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab03_5

def cal_bmi(w,h):
    if h*30.48 < 300:
        BMI = (w/((h*12)**2))*703

    else:
        BMI = (w)/((h/100)**2)

    return BMI
def bmi_guide(bmi):
    print("%.1f"%(bmi))
    if bmi < 18.5:
        print ("underweight")
    elif 18.5 <= bmi < 22.99:
        print ("normal")
    elif 23.0 <= bmi < 24.99:
        print ("overweight")
    elif 25.0 <= bmi < 29.99:
        print ("obese")
    else:
        print("severely obese")

def main():
    w = float(input())
    h = float(input())
    bmi = cal_bmi(w,h)
    bmi_guide(bmi)


if __name__ == '__main__':
    main()