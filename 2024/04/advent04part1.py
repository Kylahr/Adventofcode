def count_xmas(grid):
    n = len(grid)  
    m = len(grid[0])  
    word = "XMAS"
    count = 0
    
    def check_direction(r, c, dr, dc):
        for i in range(len(word)):
            nr = r + dr * i
            nc = c + dc * i
            if not (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == word[i]):
                return False
        return True

    for r in range(n):
        for c in range(m):
            if check_direction(r, c, 0, 1):
                count += 1
            if check_direction(r, c, 1, 0):
                count += 1
            if check_direction(r, c, 1, 1):
                count += 1
            if check_direction(r, c, 1, -1):
                count += 1
            if check_direction(r, c, 0, -1):
                count += 1
            if check_direction(r, c, -1, 0):
                count += 1
            if check_direction(r, c, -1, -1):
                count += 1
            if check_direction(r, c, -1, 1):
                count += 1

    return count

def read_input(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid

filename = 'advent04.txt'
grid = read_input(filename)

result = count_xmas(grid)
print(result)
