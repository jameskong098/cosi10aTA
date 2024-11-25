def getUnique(lst):
    set1 = set()
    for num in lst:
        set1.add(num)
    return set1
    #return set(lst)

def main():
    numbers = [1, 1, 2, 3, 3, 3, 3, 3]
    print(getUnique(numbers)) 

main()
