def main(input):
    f = open(input, "r").readlines()
    results = {}

    i = 0
    while len(f) > 0:
        next_i = True
        circut = f[i].strip().split(" -> ")
        if circut[0].isdigit():
            results[circut[1]] = int(circut[0])
            f.pop(i)
            next_i = False
        else:
            circuit_split = circut[0].split(" ")

            if len(circuit_split) > 1 and circuit_split[1] in ["AND", "OR", "LSHIFT", "RSHIFT"]:
                bitwise = circuit_split[1]
                isPossible, nums = getNumber(results, [circuit_split[0], circuit_split[2]])
            elif circuit_split[0] == "NOT":
                bitwise = circuit_split[0]
                isPossible, nums = getNumber(results, [circuit_split[1]])
            else:
                bitwise = "NONE"
                isPossible, nums = getNumber(results, [circuit_split[0]])

            if isPossible:
                res = doBitwise(bitwise, nums)
                results[circut[1]] = int(res)
                f.pop(i)
                next_i = False

        if next_i and i == len(f) - 1: i = 0
        elif next_i: i += 1
        elif i > len(f) - 1: i = 0

    print(results["a"])

def getNumber(results, vals):
    nums = []
    values_exist = True
    for i in vals:
        if i.isdigit():
            nums.append(int(i))
        elif i in results.keys():
            nums.append(int(results[i]))
        else:
            values_exist = False

    return values_exist, nums

def doBitwise(bitwise, nums):
    if bitwise == "AND":
        return nums[0] & nums[1]
    if bitwise == "OR":
        return nums[0] | nums[1]
    if bitwise == "LSHIFT":
        return nums[0] << nums[1]
    if bitwise == "RSHIFT":
        return nums[0] >> nums[1]
    if bitwise == "NOT":
        return ~nums[0] & 0xFFFF
    if bitwise == "NONE":
        return nums[0]

def part2():
    f = open("input.txt", "r")




# main("input.txt")  # part 1
main("input_2.txt")  # part 2
