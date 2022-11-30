#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab08_5

def pretty_print_list(list_a):
    max1 = 0
    rows = len(list_a)
    cols = len(list_a[0])
    for i in list_a:
        x = [len(str(x)) for x in i]
        if max(x) >= max1:
            max1 = max(x)

    
    max_l = "%" + str(max1)+"d"
    print('[',end="")
    for row in range(rows):
        if row == 0:
            print("[",end="")
        else:
            print(" [",end="")
        for col in range(cols):
            if col == cols-1:
                print(max_l%(list_a[row][col]),end="")
            else:
                print(max_l%(list_a[row][col]),end =",")
        if row == rows-1:
            print("]",end="")
        else:
            print("],")
    print("]")

    

def main():
    x = [[134, 2, 3], [4, 75, 6]]
    pretty_print_list(x)

if __name__ == "__main__":
    main()