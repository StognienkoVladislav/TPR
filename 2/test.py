weights = [0.5,4,2,0.5,1,0.5,1,2,3,0.5,1,0.5,0.5,1.5,2,1,0.5]
prices = [6,48,24,6,12,6,12,24,36,6,12,6,6,18,24,12,6]
sets = [[15,1,9,2,14],
        [15,8,9,4,14],
        [5,7,4,13],
        [10,4,6],
        [0,11,4,6],
        [0,12,16,3]]
set_weights = [9.5, 7.5, 5, 3, 3, 2]
month_sets = [0, 0, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1]
probabilities = [0, 0, 0, 0, 0, 1/3, 1/3, 1/3, 0, 0, 0, 0]
price_per_kg = 10
set_prices = []

for set in sets:
    print ("Set", sets.index(set))
    set_weight_price = set_weights[sets.index(set)] * price_per_kg
    print ("Weight price", set_weight_price)
    set_full_price = set_weight_price
    for month in month_sets:
        add_price = 0
        add_weight = 0
        print (" month with set", month)
        for item in sets[month]:
            if item not in set:
                print ("\t", item, "with price", prices[item])
                add_price += prices[item] + 2
                add_weight += weights[item]
#print "\tadditional weight", add_weight
#print "\tadditional price", add_price

        set_full_price += (add_price + add_weight * price_per_kg) *probabilities[month_sets.index(month)]
    print("full set price", set_full_price)
    set_prices.append(set_full_price)
    print()
min_set_price = min(set_prices)
print(set_prices)
print("set", set_prices.index(min_set_price), "has minimal price of", min_set_price)