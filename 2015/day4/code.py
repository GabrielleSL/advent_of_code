import hashlib

secret_key = 'yzbqklnj'

ans1 = 0
ans2 = 0

for i in range(10000000):
    key_num = secret_key + str(i)

    h = hashlib.md5(key_num.encode())
    if ans1 == 0 and h.hexdigest()[:5] == '00000':
        ans1 = i
    if ans2 == 0 and h.hexdigest()[:6] == '000000':
        ans2 = i

    if ans1 != 0 and ans2 != 0:
        break

print("PART 1:", ans1)
print("PART 2:", ans2)
