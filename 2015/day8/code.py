f = open("input.txt", "r").readlines()

ans1 = 0
ans2 = 0

for a in f:
    ans1 += len(a.strip())
    eval_res = eval(a.strip())
    ans1 -= len(eval_res)

    ans2 -= len(a.strip())
    enc_res = '\"' + a.strip().replace('\\', '\\\\').replace('\"', '\\\"') + "\""
    ans2 += len(enc_res)

print("PART 1", ans1)
print("PART 2", ans2)
