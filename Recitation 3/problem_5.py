
def calcPayment(P, r, t, n):
    monthlyRate = r / 100
    return (monthlyRate * P) / (n * (1 - (1 + monthlyRate / n)**(-n * t)))

print("Amortization Calculator")

principal = int(input("Principal, P = "))
rate = float(input("Annual Interest rate (10%), r = "))
years = int(input("Number of years, t = "))
payments = int(input("Number of payments per year, n = "))

monthlyPay = round(calcPayment(principal, rate, years, payments), 2)

print(f"The monthly payment will be p = {monthlyPay}")