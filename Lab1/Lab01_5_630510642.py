#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab01_5

def main():
    sec = int(input())
    display_time(sec)
    main

def display_time(sec):
    d,sec = divmod(sec,86400)
    h,sec = divmod(sec,3600)
    m,s = divmod(sec,60)

    time = "%d:%.2d:%.2d:%.2d"%(d,h,m,s)
    print(time)

if __name__ == '__main__':
    main()