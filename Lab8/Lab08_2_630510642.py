#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab08_2

def avg_number_row(list_x):
    avg = []
    for i in range(len(list_x)):
        lst = [x for x in list_x[i] if isinstance(x,int) or isinstance(x,float)]
        avg_lst = sum(lst)/len(lst)
        avg.append(avg_lst)
    return avg

def main():
    x = [['Python', -23, 40, 500], ['Python', -23, 40, 500, 45, 33.45, 65545, 'az', 1.1, 'za']]
    print(avg_number_row(x))

if __name__ == "__main__":
    main()