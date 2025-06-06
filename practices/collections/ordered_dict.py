from collections import OrderedDict
if __name__ == '__main__': 
    od = OrderedDict()
    for _ in range(int(input())):
        item_data = input().split()
        item_key = item_data[0:len(item_data)-1]
        item_name = " ".join(item_key)
        item_price = int(item_data[-1])
        if item_name in od:
            od[item_name] += item_price
        else:
            od[item_name] = item_price
    for key, value in od.items():
        print(key, value) 