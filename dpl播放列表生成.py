import os
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('请以要整理的文件夹路径作为参数')
        sys.exit()
    else:
        path = sys.argv[1]

    fileList = {}

    supportVideoList = ['.mp4']

    for root, dir, files in os.walk(path):
            for file in files:
                filePath = os.path.join(root, file)
                if os.path.splitext(filePath)[-1] in supportVideoList:
                    fileList[os.path.basename(filePath).split('.')[0]] = os.path.basename(filePath)

    PlayList = './play.dpl'
    PlayListPath = os.path.join(sys.argv[1],PlayList)


    print('正在生成播放列表：\n')

    with open(PlayListPath,'w+') as target:
        target.writelines('DAUMPLAYLIST'+'\n')
        target.writelines('topindex=0'+'\n')
        for i in range(1,len(fileList)+1):
            print(' '*100,end='\r',file=sys.stdout,flush=True)
            print(fileList[str(i)],end='\r',file=sys.stdout,flush=True)
            target.writelines(str(i)+'*file*'+fileList[str(i)]+'\n')
            target.writelines(str(i)+'*played*0'+'\n')
            time.sleep(0.0001)
    
    print('\n\n播放列表生成成功')
