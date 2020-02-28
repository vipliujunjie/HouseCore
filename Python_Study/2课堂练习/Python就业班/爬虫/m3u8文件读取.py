# 打开文件
import urllib.request
from gevent import monkey
import gevent

monkey.patch_all()

def download(url_list):
	i = 0
	c = len(url_list)
	for url_num in url_list:
		read = urllib.request.urlopen(url_list[i])
		video_data = read.read()
		with open("./test_video/%02d.ts" % i, 'wb') as v:
			v.write(video_data)
			i += 1

			print("\r爬虫进度：%.02f%%" % (i * 100 / c), end="")
	print()



# def main(url_list):
# 	i = 0
# 	for url_num in url_list:

# 	    gevent.joinall([
# 	        gevent.spawn(download, "%s.ts" % i, url_num[i]),
# 	        ])
# 	    i += 1


def open_url():
	l_url = "http://videows1.douyucdn.cn/live/normal_1290643420200224140509-upload-733a/"

	f = open("playlist.m3u8", "r")
	print("文件名为: ", f.name)

	url_list = list()
	 
	for line in f.readlines():  # 依次读取每行
	    if line.endswith("a22ef\n"):  # 读取结尾为  a22ef 的行
	        line = line.strip()  # 去掉每行头尾空白
	        z_url = (l_url + line)
	        url_list.append(z_url)
	# print(nums)
	# 关闭文件
	f.close()
	download(url_list)



if __name__ == '__main__':
	open_url()
