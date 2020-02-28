# 1.输入苹果的单价
price_str = input("请输入单价：")

# 2.输入苹果的重量
weight_str = input('苹果的重量：')

# 3.计算支付总金额
money = float(price_str) * float(weight_str)

# 输出

print('收款：' + str(money) + '元')
