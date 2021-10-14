sequence = input('Enter the weights sequence:')
weights = [int(weight) for weight in sequence.split()]

max_weight = max(weights)

total_weight = 0

for weight in weights:
    total_weight += weight
    if max_weight == total_weight:
        print(max_weight)
