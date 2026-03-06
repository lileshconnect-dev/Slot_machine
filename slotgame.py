import random

# Slot symbols
symbols = ["🍒", "🍋", "🔔", "⭐", "7"]

balance = 1000
roll_cost = 50

print("🎰 Welcome to the Python Slot Machine 🎰")
print("Starting Balance:", balance)
print("Each roll costs:", roll_cost)
print("---------------------------------------")

while True:
    print("\nCurrent Balance:", balance)

    if balance < roll_cost:
        print("❌ Not enough balance to play. Game Over!")
        break

    choice = input("Press ENTER to roll or type 'q' to quit: ")

    if choice.lower() == 'q':
        print("👋 Thanks for playing!")
        print("Final Balance:", balance)
        break

    balance -= roll_cost

    roll = [random.choice(symbols) for _ in range(3)]

    print("\nRolling...")
    print(" | ".join(roll))

    # Check winnings
    if roll[0] == roll[1] == roll[2]:
        win = 300
        balance += win
        print("🎉 JACKPOT! You won", win)

    elif roll[0] == roll[1] or roll[1] == roll[2] or roll[0] == roll[2]:
        win = 100
        balance += win
        print("✨ Two matched! You won", win)

    else:
        print("😢 No match. Better luck next time!")

    print("Balance after roll:", balance)
