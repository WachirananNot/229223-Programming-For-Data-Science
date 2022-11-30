#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab08_3
import copy
def remove_row_col(list_a,row,col):
    a = copy.deepcopy(list_a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j == col:
                del(a[i][col])
    del(a[row])
    return a

def main():
    x = [[2, 3, 4, 5], [8, 7, 6, 5], [0, 1, 2, 3]]
    r = 1
    l = 2
    print(remove_row_col(x,r,l))

if __name__ == "__main__":
    main()