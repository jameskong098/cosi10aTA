def removeCommon(set1, set2):
    common_elements = set1.intersection(set2)
    set1.difference_update(common_elements)
    return set1

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(removeCommon(set1, set2))

main()
