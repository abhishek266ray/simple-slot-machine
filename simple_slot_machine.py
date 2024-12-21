
import random

def get_random_slot():
    symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]
    return random.choice(symbols)

def display_slots(slots):
    print("|".join(slots))

def check_win(slots):
    return all(slot == slots[0] for slot in slots)

def calculate_winnings(bet, slots):
    if check_win(slots):
        return bet * 5  
    return 0

def main():
    balance = 100  
    print("Welcome to the Slot Machine!")

    while balance > 0:
        print(f"Current balance: {balance} coins")
        try:
            bet = int(input("Enter your bet amount (or '0' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if bet == 0:
            break
        if bet > balance:
            print("Insufficient balance. Try a smaller amount.")
            continue
        
        balance -= bet
        slots = [get_random_slot() for _ in range(3)]
        display_slots(slots)

        winnings = calculate_winnings(bet, slots)
        balance += winnings

        if winnings > 0:
            print(f"Congratulations! You won {winnings} coins!")
        else:
            print("Better luck next time.")
        
        print()

    print("Thanks for playing! Your final balance is", balance)

if __name__ == "__main__":
    main()
