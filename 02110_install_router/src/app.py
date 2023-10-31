def count_installed_routers(houses, distance):
    count = 1  # Install a router at the first house
    curr_house = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - curr_house >= distance:
            count += 1
            curr_house = houses[i]

    return count


def parametric_search(houses, start, end, target):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = count_installed_routers(houses, mid)

        if count >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


N, C = map(int, input().split())  # Number of houses N and number of routers C
houses = []

for _ in range(N):
    houses.append(int(input()))

houses.sort()  # Sort the house coordinates in ascending order

min_distance = 1
# Maximum distance between the two closest routers
max_distance = houses[-1] - houses[0]

result = parametric_search(houses, min_distance, max_distance, C)
print(result)