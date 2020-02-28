import time

def sing():
	"""唱歌5秒钟"""
	for i in range(5):
		print("-----正在唱歌:菊花茶-----", end="")
		time.sleep(1)
		print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S:%S",time.localtime(time.time())))

def dance():
	"""唱歌5秒钟"""
	for i in range(5):
		print("-----正在跳舞-----", end="")
		time.sleep(1)
		m = time.time()
		print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S:%S",time.localtime(time.time())))

def main():
	sing()
	dance()


if __name__ == '__main__':
	main()

