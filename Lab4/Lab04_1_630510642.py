#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab04_1

def sequence_number(n):
    for i in range(1,(2*n)+1,2):
        print(i,end=" ")

def main():
    n = int(input("Enter n:"))
    sequence_number(n)

if __name__ == "__main__":
    main()