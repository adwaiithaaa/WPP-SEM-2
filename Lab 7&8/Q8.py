def decode(s, indx=0, path='', res=None):
    if res is None: res = []
    if indx == len(s): res.append(path); return  # End, store path
    num1 = int(s[indx])  # 1 dig
    if 1 <= num1 <= 9: decode(s, indx + 1, path + chr(64 + num1), res)
    if indx + 1 < len(s):
        num2 = int(s[indx:indx + 2])  # 2 dig
        if 10 <= num2 <= 26: decode(s, indx + 2, path + chr(64 + num2), res)
    return res

s = "11106"
result = decode(s)
for r in result: print(r)
