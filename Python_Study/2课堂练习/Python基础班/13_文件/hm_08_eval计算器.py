input_str = input("请输入算术题：")

print(eval(input_str))

# 在开发时千万不要使用 eval 直接转换 input 的结果
# __import__("os").system("ls")
# 可以直接执行任何终端命令
