#StudentID: 630510642
#Name: Wachiranan Phuangpanya
#Lab09_4

import copy
def bmi_reports(stu_list):
    bmi_dict = {'Under': [],'Normal':[],'Over':[],'Obesity':[]}
    for i in range(len(stu_list)):
        bmi = round(stu_list[i][3]/(stu_list[i][2]**2),1)
        list_bmi = [stu_list[i][0],bmi]
        if bmi < 18.5:
            bmi_dict['Under'].append(list_bmi)
        elif 18.5 <= bmi <= 24.9:
            bmi_dict['Normal'].append(list_bmi)
        elif 25 <= bmi <= 29.9:
            bmi_dict['Over'].append(list_bmi)
        else:
            bmi_dict['Obesity'].append(list_bmi)
    c_bmi = copy.deepcopy(bmi_dict)
    for i in c_bmi.keys():
        if len(bmi_dict[i]) == 0:
            del bmi_dict[i]
    return bmi_dict

def main():
    x = [['6101022', 'Female', 1.68, 66.9],
         ['6102127', 'Male', 1.58, 50.2],
         ['6104222', 'Male', 1.61, 60.1],
         ['6105533', 'Female', 1.51, 53.2],
         ['6105711', 'Male', 1.35, 40.5],
         ['6301127', 'Male', 1.57, 50.8],
         ['6301321', 'Male', 1.51, 60.1],
         ['6303432', 'Female', 1.77, 53.2],
         ['6405411', 'Male', 1.55, 45.5],
         ['6405711', 'Male', 1.85, 60.5]]
    print(bmi_reports(x))

if __name__ == "__main__":
    main()