"""
作者：praise
功能：简单的汇率转换（人民币和美元）
版本：2.0
日期：25/02/2019
新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
"""

# 人民币转换美元的汇率
rmb_vs_usd = 6.77

# 输入字符串
currency_str = input('请输入金额：')
# 获得输入字符串的末尾三位字符
currency_unit = currency_str[-3:]
if currency_unit == 'CNY':
    # 获得输入内容除后三位之外的字符串
    rmb_str = currency_str[:-3]
    # 字符串转换为数值
    rmb_value = eval(rmb_str)
    # 美元金额
    usd_value = rmb_value / rmb_vs_usd
    print('美元金额（USD）：', usd_value)

elif currency_unit == 'USD':
    usd_str = currency_str[:-3]
    usd_value = eval(usd_str)
    rmb_value = usd_value * rmb_vs_usd
    print('人民币金额（CNY）:', rmb_value)
else:
    print('暂时不支持人民币（CNY）以及美元（USD）之外的货币')

