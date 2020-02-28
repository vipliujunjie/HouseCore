import time
import threading


def sing():
	"""唱歌5秒钟"""
	for i in range(5):
		print("-----正在唱歌:菊花茶-----", end="")
		print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S:%S",time.localtime(time.time())))
		time.sleep(1)

def dance():
	"""唱歌5秒钟"""
	for i in range(5):
		print("-----正在跳舞-----", end="")
		print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S:%S",time.localtime(time.time())))
		time.sleep(1)

def main():
	# sing()
	# dance()
	t1 = threading.Thread(target = sing)
	t2 = threading.Thread(target  = dance)
	t1.start()
	t2.start()

if __name__ == '__main__':
	main()

