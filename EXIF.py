#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'A program used to get GPS information in picture'

__author__ = 'Albert Yang'

import exifread
import re

def FindGPSTime(filePath):
    GPS={}
    Data=""
    f=open(filePath,'rb')
    tags=exifread.process_file(f)
    #print("f:",f.read())
    #print("tags:",tags)
    #for key in tags:
    #    print(key)

    for tag,value in tags.items():
        if re.match('GPS GPSLatitudeRef',tag):
            GPS['GPSLatitudeRef(纬度标识)']=str(value)
        elif re.match('GPS GPSLongitudeRef',tag):
            GPS['GPSLongitudeRef(经度标识)']=str(value)
        elif re.match('GPS GPSAltitudeRef',tag):
            GPS['GPSAltitudeRef(高度标识)']=str(value)
        elif re.match('GPS GPSLatitude',tag):
            try:
                match_result=re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]',str(value)).groups()   #匹配临近的字符
                GPS['GPSLatitude(纬度)']=int(match_result[0]),int(match_result[1]),int(match_result[2])/int(match_result[3])
            except:
                GPS['GPSLatitude(纬度)']=str(value)
        elif re.match('GPS GPSLongitude',tag):
            try:
                match_result=re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]',str(value)).groups()
                GPS['GPSLongitude(经度)']=[int(match_result[0]),int(match_result[1]),int(match_result[2])/int(match_result[3])]
            except:
                GPS['GPSLongitude(经度)']=str(value)
        elif re.match('GPS GPSAltitude',tag):
            GPS['GPSAltitude(高度)']=str(value)
        elif re.match('Image DateTime',tag):
            Data=str(value)
    return {'GPS 信息':GPS,'时间信息':Data}
    #http: // www.gpsspg.com / maps.htm

if __name__=='__main__':
    print(FindGPSTime("EXIF.jpg"))