string = input()
string = string.split(",")
m = int(string[0])
n = int(string[1])
vector_list = []
for i in range(m):
    vector = input()
    vector = vector.split(",")
    vector_list.append(vector)


def calculatedis(vector1, vector2):
    distance = 0
    for i in range(n):
        distance += (int(vector1[i]) - int(vector2[i])) * (int(vector1[i]) - int(vector2[i]))
    return distance


distance_list = []
for i in range(m):
    j = i + 1
    while j < m:
        distance = calculatedis(vector_list[i], vector_list[j])
        distance_list.append(distance)
        j += 1
distance_list.sort()
print(distance_list[0])
