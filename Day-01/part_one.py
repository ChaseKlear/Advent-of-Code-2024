#[function for item in iterable if condition]

with open("input.txt") as lists_raw:
    lists:str = lists_raw.read()
    lines:list[str] = lists.split("\n")
    list_1:list[int] = []
    list_2:list[int] = []
    
    for line in lines:
        init_pairs:list[str] = line.split("   ")
        list_1.append(int(init_pairs[0]))
        list_2.append(int(init_pairs[1]))
    list_1.sort()
    list_2.sort()

    total_dif:int = 0
    for i in range(len(list_1)):
        total_dif += abs(list_2[i] - list_1[i])

    print(total_dif)