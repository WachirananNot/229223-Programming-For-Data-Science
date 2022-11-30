#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab07_4

def reverse_list_number(m,n):
    reverse = []
    while(m >= n):
        reverse.append(m)
        m -= 2
    return reverse

def main():
    m,n = input().split(',')
    print(reverse_list_number(int(m),int(n)))

if __name__ =="__main__":
    main()