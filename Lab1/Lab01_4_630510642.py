#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab01_4

def main():
    d,h,m,s = input().split(',')
    to_seconds(d,h,m,s)

def to_seconds(d,h,m,s):
    d = int(d)
    h = int(h)
    m = int(m)
    s = int(s)
    sum_s = 0
    sum_s += s+(m*60)+(h*3600)+(d*86400)
    print(sum_s)

if __name__ == '__main__':
    main()