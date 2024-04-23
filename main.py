from Luhn import Luhn
import random, time, threading

bins = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

file = open('bins.txt', 'r+')
data = file.readlines()
for bin in data:
    bins.append(bin.strip())  # Remove newline characters
file.close()

def main():
    cc_number = ""
    bin = random.choice(bins)
    cc_number += bin
    for _ in range(10):
        l = str(random.choice(numbers))
        cc_number += l

    result= Luhn.check(cc_number)
    if result:
        digit = str(cc_number)
        if digit[0] == '4':
            brand = 'Visa'
        elif digit[:2] == '34' or digit[:2] == '37':
            brand = 'American Express'
        elif digit[:4] == '6011' or digit[:2] == '65' or (digit[:6] >= '622126' and digit[:6] <= '622925') or (digit[:3] >=  '644' and digit[:3] <= '649'):
            brand = 'Discover Card'
        elif digit[:2] >= '51' and digit[:2] <= '55':
            brand = 'Mastercard'
        else:
            brand = 'Unknown Brand'
        print(f"[+]: Valid Credit Card Number ({cc_number})")
        with open("valid.txt", 'a+') as f:
            f.write(f"{cc_number} : {brand}\n")
    else:
        print(f"[-]: Invalid Credit Card Number ({cc_number})")
    time.sleep(random.uniform(0.1, 0.2))
    return main()

if __name__ == "__main__":
    for _ in range(int(input("Enter amount of threads: "))):
        threading.Thread(target=main).start()
