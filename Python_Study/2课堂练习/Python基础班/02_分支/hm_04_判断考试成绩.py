# 练习2：定义两个整数变量 python_score` c_score，编写代码判断 成绩
python_score = int(input('请输入Python成绩：'))
c_score = int(input('请输入C语言成绩：'))

# 要求只要有一门成绩 > 60分就算合格
if python_score > 60 or c_score > 60:
    print('恭喜你成绩合格 🎉')
else:
    print('成绩不合格，继续努力 💪')
