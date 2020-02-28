# 假设：以下内容是从网络上抓取的
# 要求：
# 1.将字符串中的空白字符全部去掉
# 2.再使用 " " 作为分隔符，拼接成一个整齐的字符串

poem_str = "登鹳雀楼\t 王之涣\t 白日依山静\t \n 黄河入海流 \t\t 欲穷千里目\t\n 更上一层楼"

print(poem_str)

# 1.拆分字符串
poem_list = poem_str.split()    # 去除 空白字符 并 创建 一个 列表
print(poem_list)

# 2.合并字符串
result = " ".join(poem_list)
print(result)

#   例1.字符串拼接
t_list = [1, 2]
t_list.extend([3, 4])
print(t_list)

#   例2.字符串拼接
val = [1, 2, 3, 4] + [5, 6, 7, 8]
print(val)

#   例3.字符串拼接
t_list.append(1000)
print(t_list)


# 例4.字符串判断"a"在不在"adcf"中
q0 = "a" in "adcf"
q1 = "b" not in "adcf"
print(q0, q1)
