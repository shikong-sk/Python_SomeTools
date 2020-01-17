import sys
import cv2
import numpy as np
import face_recognition

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('请输入至少2个参数：')
        print('\t 例：人脸比对.py [图片路径1] [图片路径2] (对比阈值{0.0~1.0}(数值越低越精准))')
    else:
        a = sys.argv[1]
        b = sys.argv[2]
        if len(sys.argv) == 4:
            try:
                tolerance = float(sys.argv[3])
            except:
                print('\n对比阈值输入有误')
                sys.exit(0)
        else:
            tolerance = 0.6

        print()

        image_a = face_recognition.load_image_file(a)
        image_b = face_recognition.load_image_file(b)

        organ = {
            'chin':'下巴',
            'left_eyebrow':'左眉',
            'right_eyebrow':'右眉',
            'nose_bridge':'鼻梁',
            'nose_tip':'鼻尖',
            'left_eye':'左眼',
            'right_eye':'右眼',
            'top_lip':'上嘴唇',
            'bottom_lip':'下嘴唇',
            }

        color = {
            '下巴':(255,255,255),
            '左眉':(30,144,255),
            '右眉':(30,144,255),
            '鼻梁':(0,255,255),
            '鼻尖':(0,255,255),
            '左眼':(255,140,0),
            '右眼':(255,140,0),
            '上嘴唇':(99,71,255),
            '下嘴唇':(99,71,255),
        }

        if(len(face_recognition.face_encodings(image_a))< 1):
            print('图片 ' + a +' 中未识别到人脸')
            sys.exit(0)
        else:
            # img = cv2.imread((a.replace('\\','/')))
            img_a = cv2.imdecode(np.fromfile(a,dtype=np.uint8),-1)
            imgsp_a = img_a.shape
            res_a = face_recognition.face_encodings(image_a)[0]
            # print(face_recognition.face_locations(image_a, number_of_times_to_upsample=0, model="cnn"))
            print('图片 ' + a + ' 人脸识别信息：\n')
            for x in face_recognition.face_landmarks(image_a):
                for y in x:
                    print(organ[y] + ':')
                    for z in x[y]:
                        print('\t'+ str(z),end='')
                    if organ[y] == '下巴':
                        cv2.polylines(img_a,np.array([x[y]], np.int32),False,color['下巴'])
                    else:
                        cv2.polylines(img_a,np.array([x[y]], np.int32),True,color[organ[y]])
                    print('\n')
        
        if(len(face_recognition.face_encodings(image_b))< 1):
            print('图片 ' + b +' 中未识别到人脸')
            sys.exit(0)
        else:
            img_b = cv2.imdecode(np.fromfile(b,dtype=np.uint8),-1)
            imgsp_b = img_b.shape
            res_b = face_recognition.face_encodings(image_b)[0]
            # print(face_recognition.face_locations(image_b, number_of_times_to_upsample=0, model="cnn"))
            print('图片 ' + b + ' 人脸识别信息：\n')
            for x in face_recognition.face_landmarks(image_b):
                for y in x:
                    print(organ[y] + ':')
                    for z in x[y]:
                        print('\t'+ str(z),end='')
                    if organ[y] == '下巴':
                        cv2.polylines(img_b,np.array([x[y]], np.int32),False,color['下巴'])
                    else:
                        cv2.polylines(img_b,np.array([x[y]], np.int32),True,color[organ[y]])
                    print('\n')


        res = face_recognition.compare_faces([res_a],res_b,tolerance=tolerance)

        if True in res:
            print('图片中人物为同一个人的可能性较高')
        else:
            print('图片中人物为同一个人的可能性较低')

        cv2.namedWindow(a, 0)
        cv2.namedWindow(b, 0)
        w_a = (imgsp_a[1]//imgsp_a[2])
        h_a = (imgsp_a[0]//imgsp_a[2])
        if w_a < 500 or h_a < 500:
            w_a *= 2
            h_a *= 2
        elif w_a > 1000 or h_a > 1000:
            w_a //= 2
            h_a //= 2

        w_b = (imgsp_b[1]//imgsp_b[2])
        h_b = (imgsp_b[0]//imgsp_b[2])
        if w_b < 500 or h_b < 500:
            w_b *= 2
            h_b *= 2
        elif w_b > 1000 or h_b > 1000:
            w_b //= 2
            h_b //= 2

        cv2.resizeWindow(a,w_a,h_a)
        cv2.resizeWindow(b,w_b,h_b)
        cv2.imshow(a,img_a)
        cv2.imshow(b,img_b)
        cv2.waitKey(30 * 1000)