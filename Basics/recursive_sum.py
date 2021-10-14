'''current_number = 1
accumulated_sum = 0

def recursive_sum():
    global current_number, accumulated_sum
    if current_number == 11: return accumulated_sum
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number += 1
        return recursive_sum()

print(recursive_sum())'''

def recursive_thread_sum(current_number, accumulated_sum):
    if current_number == 100: return accumulated_sum
    else:
        accumulated_sum += current_number
        current_number += 1
        return recursive_thread_sum(current_number, accumulated_sum)

print(recursive_thread_sum(15, 0))

