from __future__ import division
from __future__ import print_function

import random
import functools

_PRIME = 2**127 - 1

_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(minimum, shares, prime=_PRIME):
    if minimum > shares:
        raise ValueError("pool secret would be irrecoverable")
    poly = [_RINT(prime) for i in range(minimum)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return poly[0], points

def _extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a%b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    if len(shares) < 2:
        raise ValueError("need at least two shares")
    x_s, y_s = zip(*shares)
    print (x_s)
    return _lagrange_interpolate(0, x_s, y_s, prime)

def main():
    p=0xC45467BBF4C87D781F903249243DF8EE868EBF7B090203D2AB0EDA8EA48719ECE9B914F9F5D0795C23BF627E3ED40FBDE968251984513ACC2B627B4A483A6533
    a1=(1,0x729FB38DB9E561487DCE6BC4FB18F4C7E1797E6B052AFAAF56B5C189D847EAFC4F29B4EB86F6E678E0EDB1777357A0A33D24D3301FC9956FFBEA5EA6B6A3D50E)
    a2=(2,0x478B973CC7111CD31547FC1BD1B2AAD19522420979200EBA772DECC1E2CFFCAE34771C49B5821E9C0DDED7C24879484234C8BE8A0B607D8F7AF0AAAC7C7F19C6)
    a4=(4,0xBFCFBAD74A23B3CC14AF1736C790A7BC11CD08141FB805BCD9227A6E9109A83924ADEEDBC343464D42663AB5087AE26444A1E42B688A8ADCD7CF2BA7F75CD89D)
    b3=(3,0x9D3D3DBDDA2445D0FE8C6DFBB84C2C30947029E912D7FB183C425C645A85041419B89E25DD8492826BD709A0A494BE36CEF44ADE376317E7A0C70633E3091A61)
    b4=(4,0x79F9F4454E84F32535AA25B8988C77283E4ECF72795014286707982E57E46004B946E42FB4BE9D22697393FC7A6C33A27CE0D8BFC990A494C12934D61D8A2BA8)
    b5=(5,0x2A074DA35B3111F1B593F869093E5D5548CCBB8C0ADA0EBBA936733A21C513ECF36B83B7119A6F5BEC6F472444A3CE2368E5A6EBF96603B3CD10EAE858150510)
    shares=[a1,a2,a4,b3,b4,b5]
    r1=recover_secret(shares[:3],p)
    r2=recover_secret(shares[-3:],p)
    print(hex(r1))
    print(hex(r2))
    r3=r1^r2
    print(hex(r3))
    c1=(1,r1)
    c2=(2,r2)
    shares=[c1,c2]
    r4=recover_secret(shares,p)
    print(hex(r4))
    print(hex(r4)[2:-1].decode('hex'))

if __name__ == '__main__':
    main()