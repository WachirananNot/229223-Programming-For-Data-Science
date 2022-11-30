#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab06_2

def create_new_string(n,str_):
    len_old_str = (len(str_))
    count_g = str_.count(',')+1
    if(count_g<n):
        temp_str = "meaw meaw cat song".upper()
        m = 0
        for k in range(count_g,n):
            new_str = temp_str[m:m+2]
            str_ = str_ +","+new_str
            m += 2
    elif(count_g>n):
        for i in range(count_g-n):
            j = str_.find(',')
            str_ = str_.replace(str_[j],'',1)
        str_ = str_.upper()
    else:
        str_ = str_[::-1].lower()
    len_new_str = len(str_)
    return len_old_str,str_,len_new_str
def main():
    n = int(input("Enter n: "))
    str = input("Enter str: ")
    new_str = create_new_string(n,str)
    print(new_str[0])
    print(new_str[1])
    print(new_str[2])
    
if __name__ == "__main__":
    main()