import socket

def main():
	# 1.创建套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 2.获取服务器的IP / port
	dest_ip = input("请输入下载服务器的IP：")
	dest_port = int(input("请输入下载服务器的Port："))
	dest_addr = (dest_ip, dest_port)
	# 3.链接服务器
	tcp_socket.connect(dest_addr)

	# 4.获取下载的文件名字
	download_file_name = input("请输入要下载的文件名字：")

	# 5.将文件名字发送到服务器
	tcp_socket.send(download_file_name.encode("utf-8"))

	# 6.接收文件中的数据
	recv_data = tcp_socket.recv(1024 * 1024)

	if recv_data:
		# 7.保存接收到的数据到一个文件中
		with open("[新]" + download_file_name, "wb") as f:
			f.write(recv_data)
	elif not recv_data:
		print("没有能从服务器上获取到(%s)" % download_file_name)

	# 8.关闭套接字
	tcp_socket.close()

if __name__ == '__main__':
	main()

