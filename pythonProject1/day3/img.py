import urllib.request as req
import os

path = os.getcwd()
imgdir = path + '/img/'
if os.path.isdir(path + imgdir):
    print('폴더 있음')
else:
    #폴더 생성
    os.mkdir(imgdir)
url = 'https://movie.naver.com/movie/running/current.naver'
req.urlretrieve(url, imgdir + 'dog.jpeg')