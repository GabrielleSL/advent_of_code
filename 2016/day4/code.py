import string
from collections import Counter

file = [a.strip() for a in open("input.txt", "r").readlines()]

ans1 = 0
ans2 = 0

for a in file:
    room = Counter(''.join(b for b in sorted(a.split("[")[0].replace('-', '')) if b.isalpha())).most_common(5)
    sector_id = int(a.split('[')[0].split('-')[-1])
    checksum = a[-6:-1]

    if len(room) != 5: continue
    c = ''.join(b[0] for b in room)
    if c != checksum: continue

    ans1 += sector_id

    decrypt = a.split("[")[0][:-4]
    shifter = sector_id % 26

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shifter:] + alphabet[:shifter]
    table = str.maketrans(alphabet, shifted_alphabet)

    decrypt = decrypt.translate(table).replace('-', ' ')

    if "northpole object" in decrypt:
        print(decrypt)
        ans2 = sector_id

print("PART 1:", ans1)

print("PART 2:", ans2)

