#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab08_1

def classify_lists_result(list_x):
    list_a = sum([x for x in list_x if isinstance(x,int)])
    list_b = [x for x in list_x if isinstance(x,float)]
    list_b = sum(list_b)/len(list_b)
    list_c = sorted([x for x in list_x if isinstance(x,str)],key=str.casefold)
    return list_a,list_b,list_c

def main():
    x = [40.0, 10, 'Hello', 20.5, 30, 'world', 'I am Happy']
    print(classify_lists_result(x))

if __name__ == "__main__":
    main()