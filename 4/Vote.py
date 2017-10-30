

example = { "x" : ["3","d", "a", "c", "b"],
            "y" : ["4", "a", "b", "c", "d"],
            "z" : ["4", "b", "c", "d", "a"]}

lstN = ["a", "b", "c", "d"]

#Относ большиснтво

lst = {}

for x in example:
    try:
        lst[example[x][1]] += int(example[x][0])
    except:
        lst[example[x][1]] = int(example[x][0])
print(lst)
#Кондорсе


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

minV = min(lst3.values())
lst4 = {}
key = ""
for k, v in lst3.items():
    if v == minV:
        key = k

for x in example:
    lst4[x] = [h for h in example[x] if h != key]
alt = {}
for x in lst4:
    #print(lst5[x])
    try:
        alt[lst4[x][1]] += int(lst4[x][0])
    except:
        alt[lst4[x][1]] = int(lst4[x][0])
print(alt)
