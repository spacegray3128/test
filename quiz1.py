string = input()
string = string.split(",")
m = int(string[0])
n = int(string[1])
vector_list = []
for i in range(m):
    vector = input()
    vector = vector.split(",")
    vector_list.append(vector)





distance_list = []
for i in range(m):
    j = i + 1
    while j < m:
        distance = calculatedis(vector_list[i], vector_list[j])
        distance_list.append(distance)
        j += 1
distance_list.sort()
print(distance_list[0])
