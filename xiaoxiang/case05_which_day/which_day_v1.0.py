"""
    作者：praise
    版本：1.0
    功能：输入某年某月某天，判断这一天是这一年的第几天
    日期：05/03/2019
"""
from datetime import datetime


def main():
    """
    主函数
    """
    try:
        # 字符串格式化并获取相应年月日
        date_str = input('请输入日期(yyyy/mm/dd):')
        date = datetime.strptime(date_str, '%Y/%m/%d')
        year = date.year
        month = date.month
        day = date.day
        print(date)
        # 存储12个月的各个天数
        days_per_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30)
        # 计算当前月份之前的天数以及当月所过的天数总和
        sum_days = sum(days_per_month[:month-1]) + day
        # 判断是否是闰年
        if (year % 100 != 0) or ((year % 4 == 0) and (year % 400 == 0)):
            if month > 2:
                sum_days += 1
        print('{}是{}的第{}天'.format(date, year, sum_days))
    except ValueError:
        print('输入的日期不符合格式！')


if __name__ == '__main__':
    main()
