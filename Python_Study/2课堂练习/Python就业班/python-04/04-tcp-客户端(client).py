
import socket

def main():
	# 1.创建tcp的套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 2.链接服务器
	server_ip = input("请输入要链接的服务器ip：")
	server_port = int(input("请输入要链接的服务器port："))
	server_addr = (server_ip, server_port)
	# tcp_socket.connect(("192.168.0.100", 7890))
	tcp_socket.connect(server_addr)

	# 3.发送数据/接收数据
	send_data = input("请输入要发送的数据：")
	tcp_socket.send(send_data.encode("utf-8"))

	# 4.关闭套接字	
	tcp_socket.close()


if __name__ == '__main__':
	main()

