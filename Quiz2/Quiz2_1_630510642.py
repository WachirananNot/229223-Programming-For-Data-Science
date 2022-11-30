#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Quiz2_1
def multiple_mn(m,n):
    out_ = []
    for i in range(1,m+1):
        in_ = []
        for j in range(1,n+1):
            if i == 1 or i == m:
                in_.append(1)
            elif j == 1 or j == n:
                in_.append(1)
            else:
                in_.append(0)
        out_.append(in_)
    return(out_)

def main():
    m = int(input())
    n = int(input())
    print(multiple_mn(m,n))

if __name__ == "__main__":
    main()

