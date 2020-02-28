# 定义字符串变量 name，输出 我的名字叫 小明 ，请多多关照
name = '大小明'
print('我的名字叫  %s，请多多关照\n' % name)

# 定义赠数变量 student_no,输出 我的学号是 000001
student_no = 199
print('我的学号是: %06d\n' % student_no)

# 定义小数 price `weight`money
# 输出 苹果的单价 9.00 元/斤，购买了 5.00 斤，需要支付 45.00 元

price = 8.5
weight = 7.4
money = price * weight
print('苹果的单价 %.02f 元/斤，购买了 %.03f 斤，需要支付 %.02f 元\n' % (price, weight, money))

# 定义一个小数 scale 输出 数据比例是 10。00%
scale = 0.8
print('输出 数据比例是 %.02f%%\n' % (scale * 100))

import keyword

print(keyword.kwlist)
