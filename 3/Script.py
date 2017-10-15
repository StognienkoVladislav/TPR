import pandas as pd

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

def FFA(data):
    ultra_checker = 0
    b = 1
    cases_count = {1: [0]}
    for i in data:
        count = sum(cases_count[b])

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

    print(ultra_checker)
    return cases_count

def BFA(data):
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

            test_val = test.values()

            sorted(test_val)
            #print(v)
            for x in test_val:                  #КОстыль, сильно много фор
                ultra_checker += 1
                if i + x < CASE:
                    for k2, v2 in cases_count.items():
                        check_v = sum(v2)
                        ultra_checker += 1
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

if __name__ == "__main__":
    global CASE
    CASE = 100

    dataFrame = pd.read_json('data.json')

    print(dataFrame)

    sort1 = sorted(dataFrame["d1"])
    # print(sort1)
    sort2 = sorted(dataFrame["d2"])
    sort3 = sorted(dataFrame["d3"])

    valerchick = [52, 21, 93, 90, 89, 9, 31, 73, 64, 35, 48, 95, 77, 13, 33, 98, 49, 55, 55, 93]

    comb = []

    for j in dataFrame:
        for v in dataFrame[j]:
            comb.append(v)

    sorted(comb)

    print("\nNFA for 1 set")
    print(NFA(sorted(comb)))
    print("\nFFA for 1 set")
    print(FFA(sorted(comb)))
    print("\nWFA for 1 set")
    print(WFA(sorted(comb)))
    print("\nBFA for 1 set")
    print(BFA(sorted(comb)))