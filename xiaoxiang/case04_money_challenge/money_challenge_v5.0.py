"""
    作者：praise
    功能：52周存钱挑战
    版本：5.0
    日期：05/03/2019
    新增功能：2.0 记录每周的存款数
              3.0 使用循环直接计数
              4.0 灵活设置每周的存款数，增加的存款数以及存款周数
              5.0 根据用户输入的日期，判断是一年中的哪一周，然后输出相应的存款金额
"""
import math
import datetime


def judge_week(date):
    """
    判断日期是一年的第几周
    """
    date = datetime.datetime.strptime(date, '%Y/%m/%d')     # 字符串解析为datetime.datetime类型
    week_num = date.isocalendar()[1]
    return week_num


def saving_money(total_week, money_per_week, increment_money):
    """
    存款操作
    """
    money_list = []             # 记录每周存款金额
    total_money_list = []       # 记录每周总存款
    for i in range(total_week):
        # 存款操作
        money_list.append(money_per_week)
        total_money = math.fsum(money_list)
        total_money_list.append(total_money)
        # 输出信息
        # print('存款第{}周，存款{}元,账户累计{}元'.format(i+1, money_list[i], total_money))
        # 更新下周存款
        money_per_week += increment_money
    return total_money_list


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
        total_money_list = saving_money(total_week, money_per_week, increment_money)    # 调用函数，并获得总金额列表
        date = input('请按格式输入日期（yyyy/mm/dd）:')
        week_num = judge_week(date)     # 一年中的第几周
        print('{}年中的第{}周，总金额{}元'.format(date.split('/')[0], week_num, total_money_list[week_num-1]))
    except ValueError:
        print('信息输入有误！')
    except IndexError:
        print('信息输入太少！')


if __name__ == '__main__':
    main()
