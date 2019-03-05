"""
    作者：praise
    功能：52周存钱挑战
    版本：3.0
    日期：05/03/2019
    新增功能：2.0 记录每周的存款数
              3.0 使用循环直接计数
"""
import math


def main():
    """
    主函数
    """
    money_per_week = 10     # 每周的存钱数
    increment_money = 10    # 每周递增金额
    total_week = 52         # 总共的周数
    money_list = []         # 记录每周存钱数
    for i in range(total_week):
        # 存钱操作
        money_list.append(money_per_week)
        total_money = math.fsum(money_list)
        # 输出信息
        print('第{}周，存款{}元,账户累计{}元'.format(i+1, money_per_week, total_money))
        # 更新下一周的存款
        money_per_week += increment_money


if __name__ == '__main__':
    main()
