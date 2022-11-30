#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab06_3

def replace_string(i,c,r):
    for j in range(len(c)):
        i = i.replace(c[j],r[j])
    return(i)
def main():
    i = input("Enter str: ")
    c = input()
    r = input()
    print(replace_string(i,c,r))

if __name__ == "__main__":
    main()