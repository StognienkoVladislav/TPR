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
                ultra_checker += 1
                ccount = sum(v)
                test[k] = ccount

            for k, v in test.items():
                global v_min
                v_min = 100
                k_check = 1
                ultra_checker += 1
                if v_min > v:
                    v_min = v
                    k_check = k

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
                ultra_checker += 1
                ccount = sum(v)
                test[k] = ccount

            test_val = test.values()

            sorted(test_val)
            #print(v)
            for x in test_val:                  #
                ultra_checker += 1
                if i + x < CASE:
                    for k2, v2 in cases_count.items():
                        check_v = sum(v2)
                        ultra_checker += 1
                        if x == check_v:
                            cases_count[k2].append(i)
                            check = True
                            break
                if check == True:
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
    sort1 = sorted(dataFrame["d1"])
    sort1.reverse()

    sort2 = sorted(dataFrame["d2"])
    sort2.reverse()

    sort3 = sorted(dataFrame["d3"])
    sort3.reverse()

    comb = []

    for j in dataFrame:
        for v in dataFrame[j]:
            comb.append(v)
    lst = []
    lst.append(dataFrame["d1"])
    lst.append(dataFrame["d2"])
    lst.append(dataFrame["d3"])
    lst.append(comb)
    lst.append(sort1)
    lst.append(sort2)
    lst.append(sort3)
    sorted(comb)
    comb.reverse()
    lst.append(comb)
    k = 0

    for x in lst:
        print("\nNFA for {} set".format(k))
        print(NFA(x))
        print("\nFFA for {} set".format(k))
        print(FFA(x))
        print("\nWFA for {} set".format(k))
        print(WFA(x))
        print("\nBFA for {} set".format(k))
        print(BFA(x))
        k+=1