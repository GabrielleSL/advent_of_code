def iterate_vals_p1(values, index, current, results=None):
    if results is None:
        results = set()

    if index == len(values):
        results.add(current)
        return results

    iterate_vals_p1(values, index + 1, current + values[index], results)
    iterate_vals_p1(values, index + 1, current * values[index], results)

    return results

def iterate_vals_p2(values, index, current, results=None):
    if results is None:
        results = set()

    if index == len(values):
        results.add(current)
        return results

    iterate_vals_p2(values, index + 1, current + values[index], results)
    iterate_vals_p2(values, index + 1, current * values[index], results)
    iterate_vals_p2(values, index + 1, int(f"{current}{values[index]}"), results)

    return results

file = [a.strip().split(': ') for a in open("input.txt", "r").readlines()]

ans1 = 0
ans2 = 0

for a in file:

    result = int(a[0])
    vals = list(map(int, a[1].split(" ")))

    results = iterate_vals_p1(vals, 0, 0)
    if result in results:
        ans1 += result

    results = iterate_vals_p2(vals, 0, 0)
    if result in results:
        ans2 += result


print(ans1)
print(ans2)
