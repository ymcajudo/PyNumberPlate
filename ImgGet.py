import os
from PIL import Image

# 다운받을 이미지 url
#sampleurl = "https://raw.githubusercontent.com/ymcajudo/PyNumberPlate/master/1.jpg"
sampleurl = "https://raw.githubusercontent.com/ymcajudo/PyNumberPlate/master/car_plate1.png"

tmpimgname = "test.jpg"

def imgdownload(imgurl):
    # curl 요청
    # curl "이미지 주소" > "저장 될 이미지 파일 이름(tmpimgname)" 

    os.system("curl " + imgurl + " > {}".format(tmpimgname))

    """
    # 저장 된 이미지 확인
    curl_img = Image.open("./"+tmpimgname)
    curl_img.show()
    """

    return tmpimgname
    
if __name__ == "__main__":
    imgdownload(sampleurl)
    tmpimg = Image.open("./"+tmpimgname)
    tmpimg.show()
