yr = input()


def is_beautifull(yr):
    while True:
        yr = str(int(yr) + 1)
        if len(set(yr)) == 4:
            return yr
print(is_beautifull(yr))