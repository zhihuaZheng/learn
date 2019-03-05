"""
    作者：praise
    功能：计算BMR
    版本：3.0
    日期：04/03/2019
    新增功能： 2.0   根据用户输入BMR，程序持续运行
               3.0  用户可以在一行输入所有信息，带单位的信息输出

"""


def main():
    """
    主函数
    """
    control = input('请按要求输入以下信息（Q退出程序）：')
    while control != 'Q':
        # 输入基本信息
        # gender = input('请输入性别(男或女):')
        # height = input('请输入身高(cm)：')
        # weight = input('请输入体重(kg)：')
        # age = input('请输入年龄：')
        print('请输入如下信息，用空格分别隔开')
        content = input('性别 身高(cm) 体重(kg) 年龄：')
        content = content.split(' ')     # 按空格将字符串分隔
        # 性别
        gender = content[0]
        # 身高
        height = content[1]
        # 体重
        weight = content[2]
        # 年龄
        age = content[3]
        if gender == '男':
            # 男性
            bmr = (13.7 * float(weight)) + (5.0 * float(height)) - (6.8 * int(age)) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * float(weight)) + (1.8 * float(height)) - (4.7 * int(age)) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('您的性别:{}，体重:{}千克，身高:{}厘米，年龄:{}岁'.format(gender, weight, height, age))
            print('您的基础代谢率BMR：{}大卡'.format(bmr))
        else:
            print('暂不支持该性别！')
        print()     # 输出空行
        control = input('请按要求输入以下信息（Q退出程序）：')
    print('退出程序！')


if __name__ == '__main__':
    main()
