import socket

def send_msg(udp_socket):
	"""发送消息"""
	# 1.发数据
	# 获取要发送的内容
	dest_ip = input("请输入对方ip：")
	dest_port = int(input("请输入对方端口："))
	send_data = input("请输入要发送的消息：")
	udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def recv_msg(udp_socket):
	"""接收数据"""
	recv_data = udp_socket.recvfrom(1024)
	print("\n来自ip：%s\n内容：%s\n" % (str(recv_data[1]), recv_data[0].decode("gbk")))

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定信息
	udp_socket.bind(("", 7788))	

	#循环循环来进行处理事情

	while True:
		print("_______udp聊天器_______")
		print("1.发送消息\n2.接收消息\n0.退出系统")
		op = input("请输入功能选项：")
		if op == "1":
			# 发送
			send_msg(udp_socket)
		elif op == "2":
			# 2.接收并显示
			recv_msg(udp_socket)
		elif op == "0":
			print("欢迎下次使用！再见👋")
			break
		else:
			print("输入错误请重新输入！")


if __name__ == '__main__':
	main()

