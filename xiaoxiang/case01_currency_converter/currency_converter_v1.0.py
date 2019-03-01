""""
作者：praise
功能：简单的汇率转换（人民币和美元）
版本：1.0
日期：22/02/2019
"""
# 输入人民币
rmb_str_value = input('请输入人民币（CYN）金额：')
# 获得输入的数值
rmb_num_value = eval(rmb_str_value)
# 人民币和美元的汇率
rmb_vs_usd = 6.77
# 转换为美元的公式
usd_value = rmb_num_value / rmb_vs_usd
# 输出美元
print('对应的美元（USD）金额：', usd_value)
