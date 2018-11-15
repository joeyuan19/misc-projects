grid = [
    [3,2,4,4,4,2,3,3],
    [3,2,2,4,4,3,3,3],
    [2,2,3,4,2,4,2,4],
    [3,3,2,3,2,2,4,4],
    [3,4,4,3,3,4,3,4],
    [4,2,3,4,2,4,2,3],
    [3,4,2,4,3,3,3,3]
]

sum_v = [15,15,17,19,14,14,14,21]
sum_h = [19,16,21,16,22,17,18]

H = len(sum_h)
V = len(sum_v)

N = H*V
N = 2**N

for i in range(N):
    b = bin(i)
solution = [[-1 for i in range(V)] for j in range(H)]

def sum_difference(solution,grid,sum_h,sum_v):
    for h in range(H):
        dh = sum(grid[h]) - sum_h[h]
        for i in range(H):
            if grid[h][i] > dh:
                solution[h][i] = 1

    for v in range(V):
        dv = sum([grid[i][v] for i in range(H)]) - sum_v[v]
        for i in range(H):
            if grid[i][v] > dv:
                solution[i][v] = 1
    return solution

for row in solution:
    print(row)
