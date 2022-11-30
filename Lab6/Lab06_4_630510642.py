#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab06_4

def new_string(name1,name2,name3,name4,name5):
    str1 = name1[:2]+"_"+name2[:2]+"_"+name3[:2]+"_"+name4[:2]+"_"+name5[:2]
    str2 = name1[len(name1)-2:][::-1]+'/'+name2[len(name2)-2:][::-1]+'/'+name3[len(name3)-2:][::-1]+'/'+name4[len(name4)-2:][::-1]+'/'+name5[len(name5)-2:][::-1]
    str3 = name1[0]+name1[len(name1)-1]+'*'+name2[0]+name2[len(name2)-1]+'*'+name3[0]+name3[len(name3)-1]+'*'+name4[0]+name4[len(name4)-1]+'*'+name5[0]+name5[len(name5)-1]
    return(str1,str2,str3)
def main():
    name1,name2,name3,name4,name5 = input().split(',')
    str_ = new_string(name1,name2,name3,name4,name5)
    print(str_[0])
    print(str_[1])
    print(str_[2])

if __name__ == "__main__":
    main()