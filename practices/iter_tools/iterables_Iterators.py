from itertools import combinations
if __name__ == "__main__":
    N = int(input())
    S = input().split()
    K = int(input())
    all_combs = list([x for x in sorted(list(combinations(S, K)))])
    combs_with_a = []
    for comb in all_combs:
        if 'a' in comb:
            combs_with_a.append(comb)
    print(round(len(combs_with_a) / len(all_combs), 4))