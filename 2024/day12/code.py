garden = [list(a.strip()) for a in open("input.txt", "r").readlines()]

def find_regions(region, plot, region_value):
    if plot[0]-1 >= 0 and garden[plot[0]-1][plot[1]] == region_value and [plot[0]-1, plot[1]] not in region:
        region.append([plot[0]-1, plot[1]])
        garden[plot[0]-1][plot[1]] = '0'
        find_regions(region, [plot[0]-1, plot[1]], region_value)

    if plot[0]+1 < len(garden) and garden[plot[0]+1][plot[1]] == region_value and [plot[0]+1, plot[1]] not in region:
        region.append([plot[0]+1, plot[1]])
        garden[plot[0]+1][plot[1]] = '0'
        find_regions(region, [plot[0]+1, plot[1]], region_value)

    if plot[1]-1 >= 0 and garden[plot[0]][plot[1]-1] == region_value and [plot[0], plot[1]-1] not in region:
        region.append([plot[0], plot[1]-1])
        garden[plot[0]][plot[1]-1] = '0'
        find_regions(region, [plot[0], plot[1]-1], region_value)

    if plot[1]+1 < len(garden[0]) and garden[plot[0]][plot[1]+1] == region_value and [plot[0], plot[1]+1] not in region:
        region.append([plot[0], plot[1]+1])
        garden[plot[0]][plot[1]+1] = '0'
        find_regions(region, [plot[0], plot[1]+1], region_value)

    return region

def find_perimeter(region):
    perimeter = 0
    for a in region:
        if [a[0]-1, a[1]] not in region:
            perimeter += 1
        if [a[0]+1, a[1]] not in region:
            perimeter += 1
        if [a[0], a[1]-1] not in region:
            perimeter += 1
        if [a[0], a[1]+1] not in region:
            perimeter += 1

    return perimeter

def find_sides(region):
    sides = 0

    for a in region:
        # TOP LINE: (nothing above and nothing right) or (nothing above, one right and one right and above)
        if ([a[0]-1, a[1]] not in region and [a[0], a[1]+1] not in region) or ([a[0]-1, a[1]] not in region and [a[0], a[1]+1] in region and [a[0]-1, a[1]+1] in region):
            sides += 1
        # BOTTOM LINE: (nothing below and nothing right) or (nothing below, one right and one right and below)
        if ([a[0]+1, a[1]] not in region and [a[0], a[1]+1] not in region) or ([a[0]+1, a[1]] not in region and [a[0], a[1]+1] in region and [a[0]+1, a[1]+1] in region):
            sides += 1
        # LEFT LINE: (nothing left and nothing below) or (nothing left, one below and one left and below)
        if ([a[0], a[1]-1] not in region and [a[0]+1, a[1]] not in region) or ([a[0], a[1]-1] not in region and [a[0]+1, a[1]] in region and [a[0]+1, a[1]-1] in region):
            sides += 1
        # RIGHT LINE: (nothing right and nothing below) or (nothing right, one below and one right and below)
        if ([a[0], a[1]+1] not in region and [a[0]+1, a[1]] not in region) or ([a[0], a[1]+1] not in region and [a[0]+1, a[1]] in region and [a[0]+1, a[1]+1] in region):
            sides += 1

    return sides

ans1 = 0
ans2 = 0

for a in range(len(garden)):
    for b in range(len(garden[a])):
        if garden[a][b] != '0':
            r = find_regions([[a,b]], [a,b], garden[a][b])
            ans1 += (find_perimeter(r) * len(r))
            ans2 += (find_sides(r) * len(r))
            garden[a][b] = '0'


print("PART 1", ans1)
print("PART 2", ans2)

