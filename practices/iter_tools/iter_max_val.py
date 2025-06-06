import math
from itertools import product
if __name__ == "__main__":
    K, M = map(int, input().split())
    lists = [] 
    max_val = 0
    # grp = None
    for _ in range(K):
        lists.append(list(map(str, input().split()))[1:])
    all_combinations = list([x for x in product(*lists)])
    for comb in all_combinations:
        product_square_sum = 0
        for num in comb:
            product_square_sum += (int(num)**2)
        if product_square_sum % M > max_val:
            max_val = product_square_sum % M
            # grp = comb
    print(max_val)