#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab09_5

import copy


def grp_search(stu_list,gender,year):
    stu_dict = {'Female':[],'Male':[]}
    year_dict = {}
    list_number = []
    for i in range(len(stu_list)):
        if stu_list[i][1] == "Female":
            stu_dict['Female'].append(stu_list[i][0])
        elif stu_list[i][1] == "Male":
            stu_dict['Male'].append(stu_list[i][0])

        if stu_list[i][0][:2] not in year_dict.keys():
            year_dict[stu_list[i][0][:2]] = []
            year_dict[stu_list[i][0][:2]].append(stu_list[i][0])
        elif stu_list[i][0][:2] in year_dict.keys():
            year_dict[stu_list[i][0][:2]].append(stu_list[i][0])
    list_number.extend(stu_dict[gender])
    try:
        list_number.extend(year_dict[year])
    except KeyError:
        pass
    list_number = set(list_number)
    list_number = sorted(list(list_number))
    return(stu_dict,year_dict,list_number)
def main():
    x = [['6101001', 'Male', 1.38, 50.9],
        ['6102002', 'Male', 1.48, 60.2],
        ['6204222', 'Male', 1.55, 45.75],
        ['6305100', 'Male', 1.65, 63.2],
        ['6403111', 'Male', 1.53, 44.5],
        ['6401127', 'Male', 1.47, 49.8]]
    y = 'Female'
    z = 65
    print(grp_search(x,y,z)[0])
    print(grp_search(x,y,z)[1])
    print(grp_search(x,y,z)[2])

if __name__ == "__main__":
    main()
