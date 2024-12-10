data = open('../adventofcode/2023/3.txt', mode='r').read()

# data = '''
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# '''

# part 1
def sum_of_part_numbers(data):
    li2=[]
    li3=[]
    part_numbers=[]
    li1=data.splitlines()
    for x in li1:
        li2=[]
        for y in x:            
            li2.append(y)
        li3.extend([li2])

    for i in range(len(li3)):
        for j in range(len(li3[i])):
            if not(li3[i][j].isdigit() or li3[i][j] is '.'):
                # ..123$..
                if li3[i][j-1].isdigit() and j != 0:
                    if li3[i][j-2].isdigit() and j-1 != 0:
                        if li3[i][j-3].isdigit() and j-2 != 0:
                            part_numbers.append(100*int(li3[i][j-3])+10*int(li3[i][j-2])+int(li3[i][j-1]))
                        else:
                            part_numbers.append(10*int(li3[i][j-2])+int(li3[i][j-1]))
                    else:
                        part_numbers.append(int(li3[i][j-1]))
                # ..$123
                if li3[i][j+1].isdigit():
                    if li3[i][j+2].isdigit():
                        if li3[i][j+3].isdigit():
                            part_numbers.append(100*int(li3[i][j+1])+10*int(li3[i][j+2])+int(li3[i][j+3]))
                        else:
                            part_numbers.append(10*int(li3[i][j+1])+int(li3[i][j+2]))
                    else:
                        part_numbers.append(int(li3[i][j+1]))
                # ..123...
                # .....$..
                if li3[i-1][j-1].isdigit() and (not li3[i-1][j].isdigit()) and i != 0:
                    if li3[i-1][j-2].isdigit():
                        if li3[i-1][j-3].isdigit():
                            part_numbers.append(100*int(li3[i-1][j-3])+10*int(li3[i-1][j-2])+int(li3[i-1][j-1]))
                        else:
                            part_numbers.append(10*int(li3[i-1][j-2])+int(li3[i-1][j-1]))
                    else:
                        part_numbers.append(int(li3[i-1][j-1]))
                # ..123...
                # ....$...
                if li3[i-1][j-2].isdigit() and li3[i-1][j-1].isdigit() and li3[i-1][j].isdigit() and (not li3[i-1][j+1].isdigit()) and i != 0:
                    part_numbers.append(100*int(li3[i-1][j-2])+10*int(li3[i-1][j-1])+int(li3[i-1][j]))
                # ...12...
                # ....$...
                if (not li3[i-1][j-2].isdigit()) and li3[i-1][j-1].isdigit() and li3[i-1][j].isdigit() and (not li3[i-1][j+1].isdigit()) and i != 0:
                    part_numbers.append(10*int(li3[i-1][j-1])+int(li3[i-1][j]))
                # ...123..
                # ....$...
                if li3[i-1][j-1].isdigit() and li3[i-1][j].isdigit() and li3[i-1][j+1].isdigit() and i != 0:
                    part_numbers.append(100*int(li3[i-1][j-1])+10*int(li3[i-1][j])+int(li3[i-1][j+1]))
                # ....1...
                # ....$...
                if (not li3[i-1][j-1].isdigit()) and li3[i-1][j].isdigit() and (not li3[i-1][j+1].isdigit()) and i != 0:
                    part_numbers.append(int(li3[i-1][j]))
                # ....123.
                # ...$....
                if li3[i-1][j+1].isdigit() and (not li3[i-1][j].isdigit()) and i != 0:
                    if li3[i-1][j+2].isdigit():
                        if li3[i-1][j+3].isdigit():
                            part_numbers.append(100*int(li3[i-1][j+1])+10*int(li3[i-1][j+2])+int(li3[i-1][j+3]))
                        else:
                            part_numbers.append(10*int(li3[i-1][j+1])+int(li3[i-1][j+2]))
                    else:
                        part_numbers.append(int(li3[i-1][j+1]))
                # ....12..
                # ....$...
                if not (li3[i-1][j-1].isdigit()) and li3[i-1][j].isdigit() and li3[i-1][j+1].isdigit() and not (li3[i-1][j+2].isdigit()) and i != 0:
                    part_numbers.append(10*int(li3[i-1][j])+int(li3[i-1][j+1]))
                # ....123.
                # ....$...
                if not (li3[i-1][j-1].isdigit()) and li3[i-1][j].isdigit() and li3[i-1][j+1].isdigit() and li3[i-1][j+2].isdigit() and i != 0:
                    part_numbers.append(100*int(li3[i-1][j])+10*int(li3[i-1][j+1])+int(li3[i-1][j+2]))
                # .....$..
                # ..123...
                if li3[i+1][j-1].isdigit() and (not li3[i+1][j].isdigit()):
                    if li3[i+1][j-2].isdigit():
                        if li3[i+1][j-3].isdigit():
                            part_numbers.append(100*int(li3[i+1][j-3])+10*int(li3[i+1][j-2])+int(li3[i+1][j-1]))
                        else:
                            part_numbers.append(10*int(li3[i+1][j-2])+int(li3[i+1][j-1]))
                    else:
                        part_numbers.append(int(li3[i+1][j-1]))
                # ....$...
                # ..123...
                if li3[i+1][j-2].isdigit() and li3[i+1][j-1].isdigit() and li3[i+1][j].isdigit() and (not li3[i+1][j+1].isdigit()):
                    part_numbers.append(100*int(li3[i+1][j-2])+10*int(li3[i+1][j-1])+int(li3[i+1][j]))
                # ....$...
                # ...12...
                if (not li3[i+1][j-2].isdigit()) and li3[i+1][j-1].isdigit() and li3[i+1][j].isdigit() and (not li3[i+1][j+1].isdigit()):
                    part_numbers.append(10*int(li3[i+1][j-1])+int(li3[i+1][j]))
                # ....$...
                # ...123..
                if li3[i+1][j-1].isdigit() and li3[i+1][j].isdigit() and li3[i+1][j+1].isdigit():
                    part_numbers.append(100*int(li3[i+1][j-1])+10*int(li3[i+1][j])+int(li3[i+1][j+1]))
                # ....$...
                # ....1...
                if (not li3[i+1][j-1].isdigit()) and li3[i+1][j].isdigit() and (not li3[i+1][j+1].isdigit()):
                    part_numbers.append(int(li3[i+1][j]))
                # ...$....
                # ....123.
                if li3[i+1][j+1].isdigit() and (not li3[i+1][j].isdigit()):
                    if li3[i+1][j+2].isdigit():
                        if li3[i+1][j+3].isdigit():
                            part_numbers.append(100*int(li3[i+1][j+1])+10*int(li3[i+1][j+2])+int(li3[i+1][j+3]))
                        else:
                            part_numbers.append(10*int(li3[i+1][j+1])+int(li3[i+1][j+2]))
                    else:
                        part_numbers.append(int(li3[i+1][j+1]))
                # ....$... 
                # ....12..
                if not (li3[i+1][j-1].isdigit()) and li3[i+1][j].isdigit() and li3[i+1][j+1].isdigit() and not (li3[i+1][j+2].isdigit()):
                    part_numbers.append(10*int(li3[i+1][j])+int(li3[i+1][j+1]))
                # ....$...
                # ....123.
                if not (li3[i+1][j-1].isdigit()) and li3[i+1][j].isdigit() and li3[i+1][j+1].isdigit() and li3[i+1][j+2].isdigit():
                    part_numbers.append(100*int(li3[i+1][j])+10*int(li3[i+1][j+1])+int(li3[i+1][j+2]))
                
    print(sum(part_numbers))

sum_of_part_numbers(data)

# part 2
def sum_of_gear_ratio(data):
    li2=[]
    li3=[]
    gear_ratio=[]
    
    li1=data.splitlines()
    for x in li1:
        li2=[]
        for y in x:            
            li2.append(y)
        li3.extend([li2])

    for i in range(len(li3)):
        for j in range(len(li3[i])):
            if li3[i][j] is '*':
                part_numbers=[]
                # ..123$..
                if li3[i][j-1].isdigit() and j != 0:
                    if li3[i][j-2].isdigit() and j-1 != 0:
                        if li3[i][j-3].isdigit() and j-2 != 0:
                            part_numbers.append(100*int(li3[i][j-3])+10*int(li3[i][j-2])+int(li3[i][j-1]))
                        else:
                            part_numbers.append(10*int(li3[i][j-2])+int(li3[i][j-1]))
                    else:
                        part_numbers.append(int(li3[i][j-1]))
                # ..$123
                if li3[i][j+1].isdigit():
                    if li3[i][j+2].isdigit():
                        if li3[i][j+3].isdigit():
                            part_numbers.append(100*int(li3[i][j+1])+10*int(li3[i][j+2])+int(li3[i][j+3]))
                        else:
                            part_numbers.append(10*int(li3[i][j+1])+int(li3[i][j+2]))
                    else:
                        part_numbers.append(int(li3[i][j+1]))
                # ..123...
                # .....$..
                if li3[i-1][j-1].isdigit() and (not li3[i-1][j].isdigit()) and i != 0:
                    if li3[i-1][j-2].isdigit():
                        if li3[i-1][j-3].isdigit():
                            part_numbers.append(100*int(li3[i-1][j-3])+10*int(li3[i-1][j-2])+int(li3[i-1][j-1]))
                        else:
                            part_numbers.append(10*int(li3[i-1][j-2])+int(li3[i-1][j-1]))
                    else:
                        part_numbers.append(int(li3[i-1][j-1]))
                # ..123...
                # ....$...
                if li3[i-1][j-2].isdigit() and li3[i-1][j-1].isdigit() and li3[i-1][j].isdigit() and (not li3[i-1][j+1].isdigit()) and i != 0:
                    part_numbers.append(100*int(li3[i-1][j-2])+10*int(li3[i-1][j-1])+int(li3[i-1][j]))
                # ...12...
                # ....$...
                if (not li3[i-1][j-2].isdigit()) and li3[i-1][j-1].isdigit() and li3[i-1][j].isdigit() and (not li3[i-1][j+1].isdigit()) and i != 0:
                    part_numbers.append(10*int(li3[i-1][j-1])+int(li3[i-1][j]))
                # ...123..
                # ....$...
                if li3[i-1][j-1].isdigit() and li3[i-1][j].isdigit() and li3[i-1][j+1].isdigit() and i != 0:
                    part_numbers.append(100*int(li3[i-1][j-1])+10*int(li3[i-1][j])+int(li3[i-1][j+1]))
                # ....1...
                # ....$...
                if (not li3[i-1][j-1].isdigit()) and li3[i-1][j].isdigit() and (not li3[i-1][j+1].isdigit()) and i != 0:
                    part_numbers.append(int(li3[i-1][j]))
                # ....123.
                # ...$....
                if li3[i-1][j+1].isdigit() and (not li3[i-1][j].isdigit()) and i != 0:
                    if li3[i-1][j+2].isdigit():
                        if li3[i-1][j+3].isdigit():
                            part_numbers.append(100*int(li3[i-1][j+1])+10*int(li3[i-1][j+2])+int(li3[i-1][j+3]))
                        else:
                            part_numbers.append(10*int(li3[i-1][j+1])+int(li3[i-1][j+2]))
                    else:
                        part_numbers.append(int(li3[i-1][j+1]))
                # ....12..
                # ....$...
                if not (li3[i-1][j-1].isdigit()) and li3[i-1][j].isdigit() and li3[i-1][j+1].isdigit() and not (li3[i-1][j+2].isdigit()) and i != 0:
                    part_numbers.append(10*int(li3[i-1][j])+int(li3[i-1][j+1]))
                # ....123.
                # ....$...
                if not (li3[i-1][j-1].isdigit()) and li3[i-1][j].isdigit() and li3[i-1][j+1].isdigit() and li3[i-1][j+2].isdigit() and i != 0:
                    part_numbers.append(100*int(li3[i-1][j])+10*int(li3[i-1][j+1])+int(li3[i-1][j+2]))
                # .....$..
                # ..123...
                if li3[i+1][j-1].isdigit() and (not li3[i+1][j].isdigit()):
                    if li3[i+1][j-2].isdigit():
                        if li3[i+1][j-3].isdigit():
                            part_numbers.append(100*int(li3[i+1][j-3])+10*int(li3[i+1][j-2])+int(li3[i+1][j-1]))
                        else:
                            part_numbers.append(10*int(li3[i+1][j-2])+int(li3[i+1][j-1]))
                    else:
                        part_numbers.append(int(li3[i+1][j-1]))
                # ....$...
                # ..123...
                if li3[i+1][j-2].isdigit() and li3[i+1][j-1].isdigit() and li3[i+1][j].isdigit() and (not li3[i+1][j+1].isdigit()):
                    part_numbers.append(100*int(li3[i+1][j-2])+10*int(li3[i+1][j-1])+int(li3[i+1][j]))
                # ....$...
                # ...12...
                if (not li3[i+1][j-2].isdigit()) and li3[i+1][j-1].isdigit() and li3[i+1][j].isdigit() and (not li3[i+1][j+1].isdigit()):
                    part_numbers.append(10*int(li3[i+1][j-1])+int(li3[i+1][j]))
                # ....$...
                # ...123..
                if li3[i+1][j-1].isdigit() and li3[i+1][j].isdigit() and li3[i+1][j+1].isdigit():
                    part_numbers.append(100*int(li3[i+1][j-1])+10*int(li3[i+1][j])+int(li3[i+1][j+1]))
                # ....$...
                # ....1...
                if (not li3[i+1][j-1].isdigit()) and li3[i+1][j].isdigit() and (not li3[i+1][j+1].isdigit()):
                    part_numbers.append(int(li3[i+1][j]))
                # ...$....
                # ....123.
                if li3[i+1][j+1].isdigit() and (not li3[i+1][j].isdigit()):
                    if li3[i+1][j+2].isdigit():
                        if li3[i+1][j+3].isdigit():
                            part_numbers.append(100*int(li3[i+1][j+1])+10*int(li3[i+1][j+2])+int(li3[i+1][j+3]))
                        else:
                            part_numbers.append(10*int(li3[i+1][j+1])+int(li3[i+1][j+2]))
                    else:
                        part_numbers.append(int(li3[i+1][j+1]))
                # ....$... 
                # ....12..
                if not (li3[i+1][j-1].isdigit()) and li3[i+1][j].isdigit() and li3[i+1][j+1].isdigit() and not (li3[i+1][j+2].isdigit()):
                    part_numbers.append(10*int(li3[i+1][j])+int(li3[i+1][j+1]))
                # ....$...
                # ....123.
                if not (li3[i+1][j-1].isdigit()) and li3[i+1][j].isdigit() and li3[i+1][j+1].isdigit() and li3[i+1][j+2].isdigit():
                    part_numbers.append(100*int(li3[i+1][j])+10*int(li3[i+1][j+1])+int(li3[i+1][j+2]))
                if len(part_numbers) == 2:
                    gear_ratio.append(part_numbers[0]*part_numbers[1])
    print(sum(gear_ratio))

sum_of_gear_ratio(data)
