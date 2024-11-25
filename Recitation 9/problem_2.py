def removeCommon(set1, set2):
    return set1 - set2

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(removeCommon(set1, set2))

main()
