low = 0
high = 100

secret = int(input("0-100 arası gizli ədəd daxil edin: "))

while low <= high:
    guess = (low + high) // 2
    print(f"Sistem təxmin edir: {guess}")

    if guess == secret:
        print("✅ Sistem ədədi tapdı!")
        break
    elif guess < secret:
        low = guess + 1
    else:
        high = guess - 16
