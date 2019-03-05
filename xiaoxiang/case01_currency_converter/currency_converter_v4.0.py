"""
    作者：praise
    功能：简单的汇率转换
    版本：4.0
    日期：27/02/2019
    新增功能：2.0 根据输入判断是人民币还是美元，进行相应的转换计算
              3.0 程序可以一直运行，直到用户选择退出
              4.0 汇率兑换功能函数化
"""


def converter(im, rate):
    """
    汇率兑换函数
    """
    out = im * rate
    return out


# 人民币转美元汇率
CNY_VS_USD = 6.77

# 标志，用来计算循环次数（测试使用）
# flag = 0
currency_str = input('请输入带单位的货币金额(输入Q结束)：')
while currency_str != 'Q':
    # 测试使用
    # flag = flag + 1
    # print('循环第', flag, '次')
    unit = currency_str[-3:]       # 获得输入金额的单位
    if unit == 'CNY':
        exchange_rate = 1 / CNY_VS_USD
    elif unit == 'USD':
        exchange_rate = CNY_VS_USD
    else:
        exchange_rate = -1
    if exchange_rate != -1:
        in_money = currency_str[:-3]
        in_money_value = eval(in_money)
        out_money = converter(in_money_value, exchange_rate)
        # print('转换后的金额：', out_money)     # 缺陷：无法转换后输出相应的单位
        # 改进
        if exchange_rate == 1 / CNY_VS_USD:
            print('转换后的金额:{}USD'.format(out_money))
        elif exchange_rate == CNY_VS_USD:
            print('转换后的金额：{}CNY'.format(out_money))
    else:
        print('暂不支持该货币')
    # 为了让交互界面稍微美观点，添加-----
    print('-------------------------------------------')
    currency_str = input('请输入带单位的货币金额(输入Q结束)：')
# 完善交互界面
print('程序结束！')
