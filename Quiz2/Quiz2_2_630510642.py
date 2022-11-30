#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Quiz2_2

def pair_request(list_input,sum):
    sum1 = []
    for i in range (len(list_input)):
        sum2 = []
        for j in range (i,len(list_input)):
            if list_input[i] != list_input[j]:
                if list_input[i] + list_input[j] == sum:
                    sum2.append(list_input[i])
                    sum2.append(list_input[j])
                else:
                    continue
            else:
                continue
        if len(sum2)!=0:
            sum1.append(sum2)
    
    return(sum1)
def main():
    list_input = [1, 9, 5, 7, 10, 3]
    sum = 20
    print(pair_request(list_input,sum))

if __name__ == "__main__":
    main()