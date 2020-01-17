from PyCrytodome.Cipher import DES

key = b'92d915250119e12b'  # 密钥 8位或16位,必须为bytes


def pad(text):
    """
    # 加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
    :param text:
    :return:
    """
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key, DES.MODE_ECB)  # 创建一个DES实例
text = 'Python rocks!'
padded_text = pad(text)
encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密
encrypted_text = 'e0be661032d5f0b676f82095e4d67623628fe6d376363183aed373a60167af537b46abc2af53d97485591f5bd94b944a3f49d94897ea1f699d1cdc291f2d9d4a5c705f2cad89e938dbacaca15e10d8aeaed90236f0be2e954a8cf0bea6112e84'
print(encrypted_text)
# rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本
plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')  # 解密
print(plain_text)
#