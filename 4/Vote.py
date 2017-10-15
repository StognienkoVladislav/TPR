

example = { "x" : ["3","d", "a", "c", "b"],
            "y" : ["4", "a", "b", "c", "d"],
            "z" : ["4", "b", "c", "d", "a"]}
#Относ большиснтво

lst = {}

for x in example:

    lst[example[x][1]] = example[x][0]

print(lst)
#Кондорсе

def condors(s, y):

    count1 = 0
    count2 = 0

    for x in example:
        if example[x].index(s) < example[x].index(y):
            count1 += int(example[x][0])
        else:
            count2 += int(example[x][0])
    lst2["{} : {}".format(s, y)] = str("{} : {}".format(count1, count2))

lst2 = {}

condForA = ["b", "c", "d"]
for y in condForA:
    condors("a", y)

condForB = ["c", "d"]

for x in condForB:
    condors("b", x)

condors("c", "d")

print()

for x, y in lst2.items():

    print(x + " = " + y)

#Альт голоса

lst3 = {}

for x in example:

    lst3[example[x][1]] = example[x][0]

minV = min(lst3.values())
lst4 = {}

for k, v in lst3.items():

    if v != minV:
        lst4[k] = v

print()
print(lst4)