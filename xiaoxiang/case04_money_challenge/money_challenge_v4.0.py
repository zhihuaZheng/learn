"""
    作者：praise
    功能：52周存钱挑战
    版本：4.0
    日期：05/03/2019
    新增功能：2.0 记录每周的存款数
              3.0 使用循环直接计数
              4.0 灵活设置每周的存款数，增加的存款数以及存款周数
"""
import math
# saving = 0      # 全局变量


def saving_money(total_week, money_per_week, increment_money):
    """
    存款操作
    """
    # global saving       # 全局变量声明
    money_list = []  # 记录每周存款金额
    for i in range(total_week):
        # 存款操作
        money_list.append(money_per_week)
        total_money = math.fsum(money_list)
        # 输出信息
        print('存款第{}周，存款{}元,账户累计{}元'.format(i+1, money_list[i], total_money))
        # 更新下周存款
        money_per_week += increment_money
    # saving = total_money
    # print('函数内：{}'.format(saving))


def main():
    """
    主函数
    """
    print('请输入如下信息，用空格隔开：')
    info = input('存款周数 每周存款金额(元) 每周的递增金额(元)：')
    info = info.split(' ')
    try:
        total_week = int(info[0])        # 存款周数
        money_per_week = float(info[1])   # 每周存款金额
        increment_money = float(info[2])   # 每周递增金额
        saving_money(total_week, money_per_week, increment_money)
    except ValueError:
        print('信息输入有误！')
    except IndexError:
        print('信息输入太少！')
    # print('函数外：{}'.format(saving))


if __name__ == '__main__':
    main()
