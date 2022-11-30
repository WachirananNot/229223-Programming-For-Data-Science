#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab03_2

def main():
    w = int(input())
    print(wavelength(w))


def wavelength(w):
    if 380 <= w < 450:
        return "Violet"
    elif 450 <= w < 495:
        return "Blue"
    elif 495 <= w < 570:
        return "Green"
    elif 570 <= w < 590:
        return "Yellow"
    elif 590 <= w < 620:
        return "Orange"
    elif 620 <= w < 750:
        return "Red"
    else:
        return "Invalid Input"

if __name__ == '__main__':
    main()
