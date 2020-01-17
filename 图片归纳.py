import os
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('请以要整理的文件夹路径作为参数')
        sys.exit()
    else:
        path = sys.argv[1]

    try:
        import exifread
    except ModuleNotFoundError as x:
        print('缺少 exifread 模块，准备安装\n')
        os.system('pip install exifread')
        import exifread
        print('\nexifread 模块安装完成')

    supportImgList = ['.jpg','.jpeg','.png']

    for root,dir,files in os.walk(path):
        for file in files:
            filePath = os.path.join(root,file)
            if sys.argv[0] == filePath:
                continue
            if os.path.splitext(filePath)[-1] in supportImgList:
                with open(filePath,'rb') as f:
                    img = exifread.process_file(f)
                    if('EXIF DateTimeOriginal' in img):
                        imgTime = str(img['EXIF DateTimeOriginal']).replace(' ',':').split(':')
                        # print(imgTime)

                    else:
                        ctime = os.path.getctime(filePath)
                        mtime = os.path.getmtime(filePath)
                        if ctime > mtime:
                            imgTime = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(mtime)).replace(' ',':').split(':')
                        else:
                            imgTime = time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(ctime)).replace(' ',':').split(':')
                        # print(imgTime)

                yearPath = os.path.join(path,imgTime[0])
                monPath = os.path.join(yearPath,imgTime[1])
                dayPath = os.path.join(monPath,imgTime[2])

                if not os.path.exists(yearPath):
                    os.mkdir(yearPath)
                    print('\n创建年份文件夹',imgTime[0])
                elif os.path.isfile(yearPath):
                    print('文件夹',os.path.dirname(yearPath),'下存在以年份命名的文件，请手动重命名或删除后重试')
                    sys.exit()

                if not os.path.exists(monPath):
                    os.mkdir(monPath)
                    print('创建月份文件夹',imgTime[1])
                elif os.path.isfile(monPath):
                    print('文件夹',os.path.dirname(monPath),'下存在以月份命名的文件，请手动重命名或删除后重试')
                    sys.exit()

                if not os.path.exists(dayPath):
                    os.mkdir(dayPath)
                    print('创建日期文件夹',imgTime[2])
                elif os.path.isfile(dayPath):
                    print('文件夹',os.path.dirname(dayPath),'下存在以日期命名的文件，请手动重命名或删除后重试')
                    sys.exit()
                        
                i = 0
                while True:
                    fileName = imgTime[3] + imgTime[4] + imgTime[5] + '_' + str(i) + os.path.splitext(filePath)[-1]
                    movePath = os.path.join(dayPath,fileName)
                    if os.path.exists(movePath):
                        i+=1
                    else:
                        os.rename(filePath,movePath)
                        print('移动文件',filePath,'到',movePath)
                        break