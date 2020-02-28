import urllib.request
from gevent import monkey
import gevent

monkey.patch_all()

def download(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, 'wb') as f:
        f.write(img_content)



def main():
    gevent.joinall([
        gevent.spawn(download, "1.ts", "http://videows1.douyucdn.cn/live/normal_1290643420200224140509-upload-733a/138d042406eb4dba89a096c8d11d9a36_0000000.ts"),
        gevent.spawn(download, "2.ts", "http://videows1.douyucdn.cn/live/normal_1290643420200224140509-upload-733a/138d042406eb4dba89a096c8d11d9a36_0000001.ts")
        ])





if __name__ == '__main__':
        main()

