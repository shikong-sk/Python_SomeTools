import os
import binascii
import struct

misc = open("upload.png","rb").read()

for i in range(1024):
    data = misc[12:20] + struct.pack('>i',i) + misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == struct.unpack('>i',misc[29:33])[0]:
        print i
        data = misc[0:20] + struct.pack('>i',i) + misc[24:]
        open('upload_repaire.png','wb').write(data)