#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab07_1

def classify_lists(list_x):
    list_a = [x for x in list_x if isinstance(x,int)]
    list_b = [x for x in list_x if isinstance(x,float)]
    list_c = [x for x in list_x if isinstance(x,str)]
    return list_a,list_b,list_c

def main():
    list_x = [10, 'hello', 23.5, 4]
    list_a,list_b,list_c = classify_lists(list_x)
    print(list_a)
    print(list_b)
    print(list_c)

if __name__ == "__main__":
    main()