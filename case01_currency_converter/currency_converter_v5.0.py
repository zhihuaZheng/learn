"""
    作者：郑致华
    功能：简单的汇率转换
    版本：5.0
    日期：27/02/2019
    新增功能：2.0 根据输入判断是人民币还是美元，进行相应的转换计算
              3.0 程序可以一直运行，直到用户选择退出
              4.0 汇率兑换功能函数化
              5.0 （1）使函数结构化 （2）简单函数定义 lambda

"""


def main():
    # 人民币转美元汇率
    cny_vs_usd = 6.77

    # 标志，用来计算循环次数（测试使用）
    # flag = 0
    currency_str = input('请输入金额(输入Q结束)：')
    while currency_str != 'Q':
        # 测试使用
        # flag = flag + 1
        # print('循环第', flag, '次')
        unit = currency_str[-3:]       # 获得输入金额的单位
        if unit == 'CNY':
            exchange_rate = 1 / cny_vs_usd
        elif unit == 'USD':
            exchange_rate = cny_vs_usd
        else:
            exchange_rate = -1
        if exchange_rate != -1:
            in_money = currency_str[:-3]
            in_money_value = eval(in_money)
            converter = lambda im, rate: im * rate      # pep8不建议编写lambda函数
            out_money = converter(in_money_value, exchange_rate)
            print('转换后的金额：', out_money)     # 缺陷：无法转换后输出相应的单位
        else:
            print('暂不支持该货币')
        # 为了让交互界面稍微美观点，添加-----
        print('-------------------------------------------')
        currency_str = input('请输入金额(输入Q结束)：')
    # 完善交互界面
    print('程序结束！')


if __name__ == '__main__':
    main()
