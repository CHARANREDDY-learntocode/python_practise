

import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#
from itertools import combinations

def filledOrders(order, k):
    # Write your code here
    orders_fulfilled = []
    order = sorted(order)
    for orders in range(len(order)):
        total = order[orders]
        count = 0
        for i in range(len(order)):
            if i != orders:
                total = total + order[i]
                count += 1
            if total == k:
                orders_fulfilled.append(count)
                total = 0
                count = 0
                break
            
    print(orders_fulfilled)
    return orders_fulfilled
                
            
    return orders_fulfilled
        
                    
            
        

if __name__ == '__main__':
    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)