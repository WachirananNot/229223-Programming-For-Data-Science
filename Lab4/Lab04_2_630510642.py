#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab04_2

def reverse_sequence_number(m,n):
    i = 0
    while(m-i >=n):
        print(m-i,end=" ")
        i+=2

def main():
    m,n = input().split(",")
    reverse_sequence_number(int(m),int(n))

if __name__ == "__main__":
    main() 