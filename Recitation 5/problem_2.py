def calculate_savings(years):
    balance = 1000
    interest_rate = 0.0415
    print(f"Year\tCurr Balance\tInterest\tNew Deposit\tNew Balance")
    for i in range(years):
        print(f"{i}\t{balance:.2f} \t{balance * interest_rate:.2f} \t\t100.0 \t\t{balance + balance * interest_rate + 100:.2f}")
        balance += balance * interest_rate + 100

def main():
    years = int(input("For how many years do you want to save? "))
    calculate_savings(years)

main()