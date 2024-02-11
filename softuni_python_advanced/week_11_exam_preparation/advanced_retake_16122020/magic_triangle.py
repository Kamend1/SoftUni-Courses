def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    for row in range(2, n):
        magic_triangle.append([])
        for idx in range(row):
            if idx == 0:
                magic_triangle[row].append(1)
            else:
                magic_triangle[row].append(magic_triangle[row - 1][idx - 1] + magic_triangle[row - 1][idx])

        magic_triangle[row].append(1)

    return magic_triangle

print(get_magic_triangle(5))
