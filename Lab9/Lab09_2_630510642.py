#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab09_2

from concurrent.futures.process import _system_limited
import copy


def grp_reports(stu_list):
    stu_dict = {'Female':[],'Male':[]}
    room_dict = {'01':[],'02':[],'03':[],'04':[],'05':[]}

    for i in range(len(stu_list)):
        if stu_list[i][1] == "Female":
            stu_dict['Female'].append(stu_list[i][0])
        elif stu_list[i][1] == "Male":
            stu_dict['Male'].append(stu_list[i][0])
        
        for j in room_dict.keys():
            if stu_list[i][0][2:4] == j:
                room_dict[j].append(stu_list[i][0])
    
    for i in room_dict.keys():
        room_dict[i] = tuple(room_dict[i])
    
    return(stu_dict,room_dict)
def main():
    stu_list = [['6101022', 'Female', 1.68, 66.9],
                ['6102127', 'Male', 1.58, 50.2],
                ['6104222', 'Male', 1.61, 60.1],
                ['6105533', 'Female', 1.51, 53.2],
                ['6105711', 'Male', 1.35, 40.5],
                ['6301127', 'Male', 1.57, 50.8],
                ['6301321', 'Male', 1.51, 60.1],
                ['6303432', 'Female', 1.77, 53.2],
                ['6405411', 'Male', 1.55, 45.5],
                ['6405711', 'Male', 1.85, 60.5]]

    print(grp_reports(stu_list)[0])
    print()
    print(grp_reports(stu_list)[1])

if __name__ == "__main__":
    main()

