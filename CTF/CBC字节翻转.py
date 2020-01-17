from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

明文 = "0123456789ABCDEFhellocbcflipping"
密钥 = "1234567890123456"
初始向量 = "ABCDEFGH12345678"


def encrypt(iv, plaintext):
    if len(plaintext) % 16 != 0:
        print("plaintext length is invalid")
        return
    if len(iv) != 16:
        print("IV length is invalid")
        return
    key = 密钥.encode('utf-8')
    aes_encrypt = AES.new(key, AES.MODE_CBC, IV=iv)
    return b2a_hex(aes_encrypt.encrypt(plaintext))


def decrypt(iv, cipher):
    if len(iv) != 16:
        print("IV length is invalid")
        return
    key = 密钥.encode('utf-8')
    aes_decrypt = AES.new(key, AES.MODE_CBC, IV=iv)
    return b2a_hex(aes_decrypt.decrypt(a2b_hex(cipher)))


def test():
    iv = 初始向量.encode('utf-8')
    plaintext = 明文.encode('utf-8')
    cipher = encrypt(iv, plaintext)
    print('密钥对1：' + cipher.decode('utf-8'))
    de_cipher = decrypt(iv, cipher)
    print('密文1：' + de_cipher.decode('utf-8'))
    print('明文1：' + str(a2b_hex(de_cipher))[2:])

    print()

    bin_cipher = bytearray(a2b_hex(cipher))
    bin_cipher[15] = bin_cipher[15] ^ ord('g') ^ ord('G')
    print('密钥对2：' + str(bytes(bin_cipher))[2:])
    de_cipher = decrypt(iv, b2a_hex(bin_cipher))
    print('密文2：' + de_cipher.decode('utf-8'))
    print('明文2：' + str(a2b_hex(de_cipher))[2:])

    print()

    bin_decipher = bytearray(a2b_hex(de_cipher))
    print('密钥对3：' + str(bytes(bin_cipher))[2:])
    bin_iv = bytearray(iv)
    for i in range(0, len(iv)):
        bin_iv[i] = bin_iv[i] ^ bin_decipher[i] ^ ord('X')
    de_cipher = decrypt(bytes(bin_iv), b2a_hex(bin_cipher))
    print("密文3：" + bytes(de_cipher).decode('utf-8'))
    print('明文3：' + str(a2b_hex(de_cipher))[2:])


test()
