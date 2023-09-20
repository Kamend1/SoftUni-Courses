def vector_generate(idx, vector):
    if idx >= len(vector):
        print(*vector, sep="")
        return
    for i in range(2):
        vector[idx] = i
        vector_generate(idx + 1, vector)

vector_size = int(input())
vector = [0] * vector_size
vector_generate(0, vector)
