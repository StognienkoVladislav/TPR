

example = { "x" : ["3","d", "a", "c", "b"],
            "y" : ["4", "a", "b", "c", "d"],
            "z" : ["4", "b", "c", "d", "a"]}
#Относ большиснтво

lst = {}

for x in example:

    lst[example[x][1]] = example[x][0]

print(lst)
#Кондорсе

lstN = ["a", "b", "c", "d"]

def condors(lstN):
    lstCheck = []
    for s in lstN:
        for s2 in lstN:
            lstCheck.append(s)
            count1 = 0
            count2 = 0
            if s2 not in lstCheck:
                for x in example:
                    if example[x].index(s) < example[x].index(s2):
                        count1 += int(example[x][0])
                    else:
                        count2 += int(example[x][0])
                    lst2["{} : {}".format(s, s2)] = str("{} : {}".format(count1, count2))
            else:
                continue
    return lst2
lst2 = {}
condors(lstN)

for k, v in lst2.items():
    print(k + " = " + v)

#Альт голоса

lst3 = {}

for x in example:

    lst3[example[x][1]] = example[x][0]

maxV = max(lst3.values())
lst4 = {}

for k, v in lst3.items():

    if v == maxV:
        lst4[k] = v
print(lst4)
