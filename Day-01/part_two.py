with open("input.txt") as lists_raw:
    lists:str = lists_raw.read()
lines:list[str] = lists.split("\n")
list_1:list[int] = []
list_2:list[int] = []

for line in lines:
    init_pairs:list[str] = line.split("   ")
    list_1.append(int(init_pairs[0]))
    list_2.append(int(init_pairs[1]))

similarity_score:int = 0

for id_1 in list_1:
    id_score:int = 0
    for id_2 in list_2:
        if id_1 == id_2:
            id_score += id_1
    similarity_score += id_score

print(similarity_score)