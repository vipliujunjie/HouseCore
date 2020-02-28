import socket

def main():
	# 1.创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 2.绑定一个本地信息
	localaddr = ("", 7788)
	udp_socket.bind(localaddr)
	while True:
		# 3.接收数据
		recv_data = udp_socket.recvfrom(1024)
		# recv_data这个变量中储存的是一个元组(接收到的数据,(发送方的ip,port))
		recv_msg = recv_data[0]  # 储存接收的数据
		send_addr = recv_data[1]  # 储存发送方的地址信息

		# 4.打印接收到的数据
		# print("\n\n发送者:%s\n内容:%s\n\n" % (str(send_addr), recv_msg.decode("utf-8")))
		print("\n发送者:%s\n内容:%s" % (str(send_addr), recv_msg.decode("gbk")))
		if recv_msg.decode("gbk") == "exit":
			print(("-" * 50) + "\n退出运行\n" + ("-" * 50))
			break
	# 5.关闭套接字
	udp_socket.close()

if __name__ == '__main__':
	main()
