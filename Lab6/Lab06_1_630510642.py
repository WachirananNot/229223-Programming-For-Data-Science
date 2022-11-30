#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab06_1

def replace_string(str_input):
    check = 'AEIOU'
    replace = '@#$&*'
    check2 = '0123456789'
    replace2 = '0000000000'
    str_input = str_input.upper()
    for i in range(5):
        str_input = str_input.replace(check[i],replace[i])
    for i in range(10):
        str_input = str_input.replace(check2[i],replace2[i])
    return str_input
def main():
    str_input = input()
    print(replace_string(str_input))

if __name__ == "__main__":
    main()