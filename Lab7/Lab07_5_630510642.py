#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab07_5

def replace_sorting(list_input,item):
    for i in range(len(list_input)):
        if list_input[i] == item:
            list_input[i] = 0
    return sorted(list_input)

def main():
    list_input = [45,3, 8, 3, 42]
    item = 3
    print(replace_sorting(list_input,item))

if __name__ == "__main__":
    main()