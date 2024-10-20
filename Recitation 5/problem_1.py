def process_number(n):
    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
        else:
            n = n * 5 + 1
        print(n, end=' ')

def main():
    run = 'y'
    while run == 'y':
        n = int(input("enter n: "))
        process_number(n)
        run = input("more? (y or n): ")
    if run != 'n':
        print("invalid input")

main()
