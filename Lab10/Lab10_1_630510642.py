#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab10_1

def main():
    text_input = read_file("D:\Doc\Program\Python\Data\Lab10\in_01.txt")
    text_input = text_input.strip()
    count_letter("OH oh! HI Happy a nice day")

def count_letter(text):
    count = 0
    percentage = 0
    a = ['a','e','i','o','u']
    n = len(text)
    text = text.lower()
    for i in "aeiou":
        count += text.count(i)
    percentage = count/n*100
    print("Counting = {0:d} ({1:.2f}%)".format(count,percentage))

def read_file(filename,mode="rt"):
    with open(filename) as fin:
        fin = open(filename,mode,encoding='utf-8')
        contents = fin.read()
    
    return contents

if __name__ == "__main__":
    main()