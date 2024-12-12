import itertools

f = open("input.txt", "r").readlines()

dist = {}
for a in f:
    town1, _, town2, _, d = a.strip().split(" ")
    if town1 not in dist.keys():
        dist[town1] = {town2: int(d)}
    elif town1 in dist.keys():
        dist[town1][town2] = int(d)

    if town2 not in dist.keys():
        dist[town2] = {town1: int(d)}
    elif town2 in dist.keys():
        dist[town2][town1] = int(d)


def calculate_route(route = [], route_calc = 0):
    if len(route) == len(dist.keys()):
        return route_calc
    else:
        return [calculate_route(route + [a], route_calc + dist[route[-1]][a]) for a in dist.keys() if a not in route]

ans1 = 0
ans2 = 0

res = []
for a in dist.keys():
    res += calculate_route([a], 0)

m = list(itertools.chain(*itertools.chain(*itertools.chain(*itertools.chain(*itertools.chain(*itertools.chain(*res)))))))
# m = list(itertools.chain(*res))

ans1 = min(m)
ans2 = max(m)

print("PART 1", ans1)
print("PART 2", ans2)
