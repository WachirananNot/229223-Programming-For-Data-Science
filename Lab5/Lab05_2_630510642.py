#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab05_2

def print_triangle(n,type):
    if type == "U" or type == "u":
        if n>0:
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print(j,end="")
                print()

        else:
            for i in range(abs(n),0,-1):
                for j in range(abs(n),i-1,-1):
                    print(j,end="")
                print()
    elif type == "D" or type == "d":
        if n>0:
            for i in range(n,0,-1):
                for j in range(1,i+1):
                    print(j,end="")
                print()

        else:
            for i in range(abs(n),0,-1):
                for j in range(i,0,-1):
                    print(j,end="")
                print()

def main():
    n = int(input("Enter n: "))
    type = input("Enter \"U\"or\"D\": ")
    print_triangle(n,type)

if __name__ == "__main__":
    main()