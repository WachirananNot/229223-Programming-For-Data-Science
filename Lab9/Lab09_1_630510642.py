#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab09_1
import copy


def upd_student(stu_list,stu_id,new_weight):
    stu_dict = {}
    for i in range(len(stu_list)):
        stu_dict[stu_list[i][0]] = stu_list[i][1:]

    stu_dictold = copy.deepcopy(stu_dict)

    new_stu = ['',0,new_weight]
    if stu_id in stu_dict.keys():
        stu_dict[stu_id][2] = new_weight
    else:
        stu_dict[stu_id] = new_stu
    return(stu_dictold,stu_dict)
def main():
    stu_list = [['6101001', 'Female', 1.38, 50.9],
                ['6102002', 'Male', 1.48, 60.2],
                ['6204222', 'Male', 1.55, 45.75]]
    stu_id  = '6205111'
    new_weight = 50.5
    print(upd_student(stu_list,stu_id,new_weight)[0])
    print()
    print(upd_student(stu_list,stu_id,new_weight)[1])

if __name__ == "__main__":
    main()