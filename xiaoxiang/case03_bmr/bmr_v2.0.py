"""
    作者：praise
    功能：计算BMR
    版本：2.0
    日期：04/03/2019
    新增功能： 根据用户输入BMR，程序持续运行
"""


def main():
    """
    主函数
    """
    control = input('请按要求输入以下信息（Q退出程序）：')
    while control != 'Q':
        # 输入基本信息
        gender = input('请输入性别(男或女):')
        height = input('请输入身高(cm)：')
        weight = input('请输入体重(kg)：')
        age = input('请输入年龄：')
        if gender == '男':
            # 男性
            bmr = (13.7 * float(weight)) + (5.0 * float(height)) - (6.8 * int(age)) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * float(weight)) + (1.8 * float(height)) - (4.7 * int(age)) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('基础代谢率BMR(大卡)：', bmr)
        else:
            print('暂不支持该性别！')
        print()     # 输出空行
        control = input('请按要求输入以下信息（Q退出程序）：')
    print('退出程序！')


if __name__ == '__main__':
    main()
