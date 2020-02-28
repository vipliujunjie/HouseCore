l_url = "http://videows1.douyucdn.cn/live/normal_1290643420200224140509-upload-733a/"

f = open("playlist.m3u8", "r")
print("文件名为: ", f.name)

nums = list()
 
for line in f.readlines():  # 依次读取每行
    if line.endswith("a22ef\n"):  # 读取结尾为  a22ef 的行
        line = line.strip()  # 去掉每行头尾空白
        # print("读取的数据为: %s" % (line))

        z_url = (l_url + line)
        nums.append(z_url)
print(nums)

# 关闭文件
f.close()