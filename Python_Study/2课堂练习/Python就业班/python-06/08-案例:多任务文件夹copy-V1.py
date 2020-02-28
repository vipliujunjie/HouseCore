import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
	"""完成文件的复制"""
	print("====>模拟copy文件：从%s--->到%s 文件名是：%s" % (old_folder_name, new_folder_name, file_name))
	old_f = open(old_folder_name + "/" + file_name, "rb")
	content = old_f.read()
	old_f.close()

	new_f = open(new_folder_name + "/" + file_name, "wb")
	new_f.write(content)
	new_f.close()


def main():
	# 1.获取用户要copy的文件夹的名字
	old_folder_name = input("请输入要复制的文件夹：")

	# 2.创建一个新的文件夹
	try:
		new_folder_name = "[复件]" + old_folder_name
		os.mkdir(new_folder_name)
	except:
		print("已有此文件夹-跳过创建")

	# 3.获取文件夹内所有待copy的名字    listdir()
	file_names = os.listdir(old_folder_name)
	# print(file_names)

	# 4.创建进程池
	po = multiprocessing.Pool(5)

	# 5.向进程池中添加 copy文件的任务
	for file_name in file_names:
		po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
		
	po.close()
	po.join()  # 等待进程池里面的进程运行完 再关闭主进程


if __name__ == '__main__':
	main()

