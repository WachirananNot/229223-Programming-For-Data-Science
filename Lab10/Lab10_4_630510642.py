#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab10_4
from cmath import rect
import numpy as np
import matplotlib.pyplot as plt
import copy
def main():
    text = find_stat_data("D:\Doc\Program\Python\Data\Lab10\Lab10_Dataset\Pokemon.csv")
    text = toList(text)
    x,y = toArray(text)
    plotGraph(x,y)
    
def find_stat_data(filename,mode="rt"):
    with open(filename) as fin:
        fin = open(filename,mode,encoding='utf-8')
        contents = fin.readlines()
    return contents

def toArray(list_x):
    gen = {}
    list_gen = []
    list_total = []
    for i in list_x:
        if(i[11] not in gen.keys()):
            gen[i[11]] = 1
        else:
            gen[i[11]] += 1
    list_gen = copy.deepcopy(list(gen.keys()))
    list_total = copy.deepcopy(list(gen.values()))
    array_total = np.array(list_total)
    return(list_gen,array_total)

def toList(list_x):
    list_ = []
    for i in range(len(list_x)):
        if i == 0:
            continue
        else:
            text_input = list_x[i].strip("\n")
            list_input = text_input.split(',')
            list_.append(list_input)
    return list_
def plotGraph(x,y):
    fig = plt.figure()
    plt.rcParams['font.size'] = 15
    rect = fig.patch
    rect.set_facecolor('lightgoldenrodyellow')
    plt.title('The number of Pokemon in each generation')
    plt.plot(x,y, color='purple')
    plt.grid(True)
    
    plt.xlabel('Generation',color='blue')
    plt.ylabel('Total',color='red')

    plt.show()
if __name__ == "__main__":
    main()