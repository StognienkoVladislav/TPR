import pandas as pd

CASE = 100

dataFrame = pd.read_json('data.json')

print(dataFrame)

sort1 = sorted(dataFrame["d1"])
#print(sort1)
sort2 = sorted(dataFrame["d2"])
sort3 = sorted(dataFrame["d3"])

valerchick = [52, 21, 93, 90, 89, 9, 31, 73, 64, 35, 48, 95, 77, 13, 33, 98, 49, 55, 55, 93]


testtt = [51, 51, 51]

def NFA(data):
    ultra_checker = 0
    b = 1
    cases_count = {1: [0]}
    for i in data:
        count = sum(cases_count[b])
        ultra_checker += 1
        if i + count < CASE:
            cases_count[b].append(i)
        else:
            b+=1
            cases_count[b] = [i]

    print(ultra_checker)

    return cases_count

#print(NFA(dataFrame["d1"]))
#print(NFA(sort1))
#print(NFA(valerchick))
print(NFA(testtt))
##################################

def FFA(data):
    ultra_checker = 0
    b = 1
    cases_count = {1: [0]}
    for i in data:
        count = 0
        for j in cases_count[b]:
            count += j

        ultra_checker += 1

        if i + count < CASE:
            cases_count[b].append(i)

        else:
            global check
            check = False
            for k, v in cases_count.items():

                ccount = sum(v)
                ultra_checker += 1

                if i + ccount < CASE:
                    cases_count[k].append(i)
                    check = True
                    break
            if check == False:
                b += 1
                cases_count[b] = [i]

    print(ultra_checker)

    return cases_count

#print(FFA(dataFrame["d1"]))
#print(FFA(sort1))
print(FFA(testtt))
#print(FFA(valerchick))

def WFA(data):
    ultra_checker = 0
    b = 1
    cases_count = {1: [0]}
    for i in data:
        count = sum(cases_count[b])
        ultra_checker += 1

        if i + count < CASE:
            cases_count[b].append(i)

        else:
            test = {}
            global check
            check = False
            for k, v in cases_count.items():

                ccount = sum(v)
                test[k] = ccount

            for k, v in test.items():

                global v_min
                v_min = 100
                k_check = 1

                if v_min > v:
                    v_min = v
                    k_check = k

                ultra_checker += 1
                if i + v_min < CASE:
                    cases_count[k_check].append(i)
                    check = True
                    break

            if check == False:
                b += 1
                cases_count[b] = [i]


    return cases_count

#print(WFA(dataFrame["d1"]))
#print(WFA(sort1))
print(WFA(testtt))
#print(WFA(valerchick))


def BFA(data):
    ultra_checker = 0
    b = 1
    cases_count = {1: [0]}
    for i in data:
        count = 0
        for j in cases_count[b]:
            count += j

        ultra_checker += 1

        if i + count < CASE:
            cases_count[b].append(i)

        else:
            test = {}
            global check
            check = False
            for k, v in cases_count.items():
                ccount = sum(v)
                test[k] = ccount

            test_val = test.values()

            sorted(test_val)
            #print(v)
            for x in test_val:                  #КОстыль, сильно много фор
                ultra_checker += 1
                if i + x < CASE:
                    for k2, v2 in cases_count.items():
                        check_v = sum(v2)
                        if x == check_v:
                            cases_count[k2].append(i)
                            check = True
                            #print("KAVABANGAA")
                            break
            if check == False:
                b += 1
                cases_count[b] = [i]

    print(ultra_checker)

    return cases_count

#print(BFA(dataFrame["d1"]))
print(BFA(sort1))
#print(BFA(valerchick))
