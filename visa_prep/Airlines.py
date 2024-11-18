import math
def min_planes_to_buy(X, N):
    current_capacity = X * 100
    if  current_capacity >= N:
        return 0
    required_planes = math.ceil(N / 100)
    new_planes = required_planes - X
    return new_planes
X, N = map(int, input().split())
print(min_planes_to_buy(X, N))
