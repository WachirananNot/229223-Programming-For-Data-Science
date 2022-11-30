#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab09_3

import copy


def counting_reports(stu_list):
    count_s = {'Female':0,'Male':0}
    count_r = {'01':0,'02':0,'03':0,'04':0,'05':0}
    count_y = {4:0,3:0,2:0,1:0}

    for i in range(len(stu_list)):
        if 'Female' in stu_list[i]:
            count_s['Female'] += 1
        elif 'Male' in stu_list[i]:
            count_s['Male'] += 1
        if stu_list[i][0][2:4] == '01':
            count_r['01'] += 1
        elif stu_list[i][0][2:4] == '02':
            count_r['02'] += 1
        elif stu_list[i][0][2:4] == '03':
            count_r['03'] += 1
        elif stu_list[i][0][2:4] == '04':
            count_r['04'] += 1
        elif stu_list[i][0][2:4] == '05':
            count_r['05'] += 1
        if stu_list[i][0][:2] == '64':
            count_y[1] += 1
        elif stu_list[i][0][:2] == '63':
            count_y[2] += 1
        elif stu_list[i][0][:2] == '62':
            count_y[3] += 1
        elif stu_list[i][0][:2] == '61':
            count_y[4] += 1
    c_y = copy.deepcopy(count_y)
    for i in c_y.keys():
        if count_y[i] == 0:
            del count_y[i]
    return(count_s,count_r,count_y)
def main():
    x = [['6101022', 'Female', 1.68, 66.9],['6102127', 'Male', 1.58, 50.2],
['6104222', 'Male', 1.61, 60.1], ['6105533', 'Female', 1.51, 53.2],
['6105711', 'Male', 1.35, 40.5], ['6301127', 'Male', 1.57, 50.8],
['6301321', 'Male', 1.51, 60.1], ['6303432', 'Female', 1.77, 53.2],
['6405411', 'Male', 1.55, 45.5], ['6405711', 'Male', 1.85, 60.5]]

    print(counting_reports(x)[0])
    print(counting_reports(x)[1])
    print(counting_reports(x)[2])

if __name__ == "__main__":
    main()