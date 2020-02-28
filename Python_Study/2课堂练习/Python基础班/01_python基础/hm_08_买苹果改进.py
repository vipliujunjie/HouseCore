# 1.输入苹果的单价
price = float(input('请输入苹果的单价：'))
# 2.输入苹果的重量
weight = float(input('请输入苹果的重量：'))

# 3.计算支付总金额
money = price * weight
# 输出
print('收款 ' + str(money) + ' 元')
