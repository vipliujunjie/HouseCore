import socket

def main():
	#创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
	# 从键盘获取数据
	send_data = input("请输入要发送的数据:")

	# 可以使用套接字收发数据
	# udp_socket.sendto("hahaha hello", 对方的ip以及port)
	# udp_socket.sendto(b"hello udp JunJie %d \n" % i, ("192.168.0.108", 8080))
	udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.108", 8080))
	# 可以关闭套接字

	udp_socket.close()
	print("-" * 50)
	print("发送成功！")


if __name__ == '__main__':
	main()
