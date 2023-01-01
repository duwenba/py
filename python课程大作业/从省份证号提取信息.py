'''
1. 输入18位身份证号码,并验证是否符合要求
2. 得到前两位
3. 打开csv文件,查找相应的省份
4. 获取15-17位,判断奇偶
5. 计算校验码,对比
6. 打印结果
'''


#主函数:
def mainloop():
    while True:
        print("=================================================================")
        ID_number = input("请输入18位身份证号码:")
        if not len(ID_number) == 18:
            print("erro:身份证号必须是18位的")
            continue
        pronvince = get_province(ID_number)
        gender = get_gender(ID_number)
        is_standard = get_verification_code(ID_number)
        print('\n',f"省份        {pronvince.split()[0]}",f"性别        {gender.split()[0]}",f"校验码      {is_standard}",sep="\n")
        print("\n"*2,"是否需要继续?(y/n):")
        resp = input() 
        if resp == "n":
            print("查询结束")
            break
        elif not resp == "y":
            print(f"erro: expected Yes(y) or No(n) but got a \'{resp}\'")
            break


#  获取省份信息
def get_province(ID):
    province_id = ID[:2]
    with open("省份信息.csv",encoding='utf-8',mode="rt") as f:
        for line in f:
            if line.split(',')[0] == province_id:
                return line.split(',')[1]
        return "没有找到对应省份,请检查输入是否正确."

#获取性别
def get_gender(ID:str):
    gender_id = int(ID[14:-1])
    if gender_id % 2 == 0:
        return '女'
    else:
        return '男' 

#计算校验码
def get_verification_code(ID):
    verification_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][sum(
        [int(ID[i]) * [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2][i] for i in range(17)]) % 11]
    if ID[-1] == verification_code:
        return '校验码正确'
    else:
        return '校验码错误'

if __name__ == "__main__":
    mainloop()