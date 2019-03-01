"""
作者：praise
功能：简单的汇率转换（人民币和美元）
版本：3.0
日期：25/02/2019
新增功能： 2.0 根据输入判断是人民币还是美元，进行相应的转换计算
           3.0 程序可以一直运行，直到用户选择退出
"""

# 人民币转换美元的汇率
rmb_vs_usd = 6.77
# 标志，用来计算循环次数（测试使用）
# flag = 0
currency_str = input('请输入金额(输入Q结束)：')
while currency_str != 'Q':
    # 测试使用
    # flag = flag + 1
    # print('循环第', flag, '次')
    currency_unit = currency_str[-3:]       # 获得输入金额的单位
    if currency_unit == 'CNY':
        # 获得输入金额的数值
        rmb_str = currency_str[:-3]
        rmb_value = eval(rmb_str)
        # 计算美元金额
        usd_value = rmb_value / rmb_vs_usd
        print('美元金额（USD）：', usd_value)

    elif currency_unit == 'USD':
        # 获得输入金额的单位
        usd_str = currency_str[:-3]
        usd_value = eval(usd_str)
        # 计算人民币金额
        rmb_value = usd_value * rmb_vs_usd
        print('人民币金额（CNY）:', rmb_value)
    else:
        print('暂时不支持人民币（CNY）以及美元（USD）之外的货币')
    # 为了让交互界面稍微美观点，添加-----
    print('-------------------------------------------')
    currency_str = input('请输入金额(输入Q结束)：')
# 完善交互界面
print('程序结束！')
