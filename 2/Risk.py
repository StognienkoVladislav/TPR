
import pandas as pd
import numpy as np

if __name__ == '__main__':

    sets = [["Шапка", "Бушлат", "Рукавички", "Ватные штаны", "Ботинки"],
        ["Шапка", "Пальто", "Рукавички", "Джинси", "Ботинки"],
        ["Кепка", "Куртка", "Джинси", "Туфли"],
        ["Свитр", "Джинси", "Кросовки"],
        ["Блайзер", "Рубашка", "Джинси", "Кросовки"],
        ["Блайзер", "Футболка", "Шорты", "Вьетнамки"]
    ]
    weight = [9.5, 7.5, 5, 3, 3 ,2]

    month_sets = [0, 0, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1]

    #Example1

    dataFrame = pd.read_json('data.json')
    #print(dataFrame)

    #prob_month = [31/365, 28/365, 31/365, 30/365, 31/365, 30/365, 31/365, 31/365, 30/365, 31/365, 30/365, 31/365]
    prob_month = [1/12] * 12
    price = 10
    set_prices = []

    i = 1
    for set in sets:
        set_weight_price = weight[sets.index(set)] * price
        print("{} Набор с ценой".format(i), set_weight_price)
        set_full_price = set_weight_price


        k = 0
        for month in month_sets:

            add_price = 0
            add_weight = 0
            #print("набор месяца", month)

            for item in sets[month]:
                if item not in set:
                    #print("\t", item, "с ценой", dataFrame["clothes"][item][1])

                    add_price += dataFrame["clothes"][item][1] + 2
                    add_weight += dataFrame["clothes"][item][0]

            set_full_price += (add_price + add_weight * price) * prob_month[k]
            k+=1



        print("Полная цена набора", set_full_price)
        set_prices.append(set_full_price)
        i += 1
    min_set_price = min(set_prices)

    print("Набор", set_prices.index(min_set_price) + 1, "имеет минимальную цену", min_set_price)