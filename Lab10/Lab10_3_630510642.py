#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab10_3
def main():
    text = read_file("D:\Doc\Program\Python\Data\Lab10\in_03.txt")
    text = text.strip("\n")
    text = text.split("\n")
    for i in range(len(text)):
        text[i] = text[i].split(',')
        for j in range(len(text[i])):
            try:
                text[i][j] = float(text[i][j])
            except ValueError:
                continue
            
    output_ = find_avg_number(text)
    print(output_)

def find_avg_number(list_x):
    avg = []
    for i in list_x:
        c = 0
        s = 0
        for j in i:
            if isinstance(j,int) or isinstance(j,float):
                c+=1
                s+=j
        avg.append(s/c)
    return(avg)



def read_file(filename,mode="rt"):
    with open(filename) as fin:
        fin = open(filename,mode,encoding='utf-8')
        contents = fin.read()
    
    return contents

if __name__ == "__main__":
    main()