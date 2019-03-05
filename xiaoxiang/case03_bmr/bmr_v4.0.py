"""
    作者：praise
    功能：计算BMR
    版本：4.0.1
    日期：05/03/2019
    新增功能： 2.0   根据用户输入BMR，程序持续运行
               3.0  用户可以在一行输入所有信息，带单位的信息输出
               4.0  异常处理

"""


def main():
    """
    主函数
    """
    control = input('请按要求输入以下信息（Q退出程序）：')
    while control != 'Q':
        # 输入基本信息
        print('请输入如下信息，用空格分别隔开')
        content = input('性别 身高(cm) 体重(kg) 年龄：')
        content = content.split(' ')     # 按空格将字符串分隔
        try:
            # 性别
            gender = content[0]
            # 身高
            height = content[1]
            # 体重
            weight = float(content[2])
            # 年龄
            age = int(content[3])
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
        except ValueError:
            print('输入的信息不正确！')
        except IndexError:
            print('输入的信息太少！')
        except:
            print('程序异常！')
        print()     # 输出空行
        control = input('请按要求输入以下信息（Q退出程序）：')
    print('退出程序！')


if __name__ == '__main__':
    main()
