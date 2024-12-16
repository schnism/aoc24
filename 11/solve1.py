#stones=[125,17]
stones=[4189,413,82070,61,655813,7478611,0,8]



for i in range(25):
    print(i)
    next = []
    for stone in stones:
        stone_s = str(stone)

        if stone == 0: 
            next.append(1)
        elif len(stone_s)%2==0: 
            next.append(int(stone_s[0:int(len(stone_s)/2)]))
            next.append(int(stone_s[int(len(stone_s)/2):len(stone_s)]))
        else:
            next.append(stone*2024)

    stones=next.copy()

print(len(stones))
        