n_terms = int(input("Enter a number: "))

n1 = 0
n2 = 1
count = 0

if n_terms <= 0:
    print("Invalid, Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence upto {n_terms}:")
    print(n1)
else:
    print(f"Fibonnaci series upto {n_terms}:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1