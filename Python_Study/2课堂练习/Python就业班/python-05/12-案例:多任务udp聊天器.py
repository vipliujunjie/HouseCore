import socket
import threading

send_data = ""

def send_msg(udp_socket, dest_ip, dest_port):
	global send_data
	while True:
		"""发送消息"""
		# 获取要发送的数据
		send_data = input("请输入要发送的数据：")
		udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))  # 发送
		if send_data == "exit":
			break

def recv_msg(udp_socket):
	global send_data
	while True:   
		"""接收消息"""
		recv_data = udp_socket.recvfrom(1024)  # 接收消息
		print("\n消息来自:%s\n内容:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))
		if recv_data[0].decode("gbk") == "exit":
			break


def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定信息
	udp_socket.bind(("", 7890))

	# 获取要发送的数据
	dest_ip = input("请输入对方IP：")
	dest_port = int(input("请输入对方port："))

	# 创建多任务
	t1 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
	t2 = threading.Thread(target=recv_msg, args=(udp_socket,))

	t1.start()
	t2.start()


if __name__ == '__main__':
	main()


