"""
    作者：praise
    功能：52周存钱挑战
    版本：1.0
    日期：05/03/2019
"""


def main():
    """
    主函数
    """
    money_per_week = 10     # 每周的存钱数
    i = 1                   # 记录周数
    increment_money = 10    # 每周递增金额
    total_week = 52         # 总共的周数
    total_money = 0         # 总共存钱数
    while i <= total_week:
        # 存钱操作
        total_money += money_per_week
        # 输出信息
        print('第{}周，存款{}元,账户累计{}元'.format(i, money_per_week, total_money))
        # 更新下周存款
        money_per_week += increment_money
        i += 1


if __name__ == '__main__':
    main()
