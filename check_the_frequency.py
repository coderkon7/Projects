test_dict = {'fries':4,
             'carbonated_drink':5,
             'burger':8,
             'ice_cream':8,
             'coffee':5
}

price = 8
frequency = 0

for item in test_dict:
    if test_dict[item] == price:
        frequency += 1

print("Frequency of price 8$ is: ", frequency)