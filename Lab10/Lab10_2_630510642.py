#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab10_2

import string

def main():
    text = read_file("D:\Doc\Program\Python\Data\Lab10\in_02.txt")
    text = text.strip("\n")
    print("text:",text)

    output_ = word_count(text)
    print(output_)

def make_list_clean(list_x):
    ans = []
    for i in list_x:
        j = i.strip(',')
        ans.append(j.strip('.').strip('$').lower())
        for i in range(len(ans)):
            ans[i] = ans[i].strip(string.punctuation)
    return ans

def word_count(text):
    ans = dict()
    list_seen = []

    list_ = text.split(' ')
    list_word = make_list_clean(list_)
    for i in list_word:
        if i  in ans.keys():
            ans[i] += 1
        else:
            ans[i] = 1
    return ans
def read_file(filename,mode="rt"):
    with open(filename) as fin:
        fin = open(filename,mode,encoding='utf-8')
        contents = fin.read()
    
    return contents

if __name__ == "__main__":
    main()

