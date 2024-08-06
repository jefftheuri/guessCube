import random
from datetime import datetime

# Simulating a database with a dictionary
users = {}


def generate_answers_and_prizes():
    answers = ["Answer A", "Answer B", "Answer C", "Answer D", "Answer E", "Answer F"]
    prizes = [random.randint(10, 100) for _ in range(6)]
    return list(zip(answers, prizes))


def deposit(phone_number, amount):
    if phone_number not in users:
        users[phone_number] = {"balance": 0, "last_played": None}
    users[phone_number]["balance"] += amount
    return f"Deposit successful. Your new balance is {users[phone_number]['balance']} KSH."


def process_sms(phone_number, user_input):
    if phone_number not in users:
        return "Please deposit money first. Send 'DEPOSIT [amount]' to add funds."

    if user_input.lower().startswith("deposit"):
        try:
            amount = int(user_input.split()[1])
            return deposit(phone_number, amount)
        except (IndexError, ValueError):
            return "Invalid deposit format. Use 'DEPOSIT [amount]'."

    if users[phone_number]["balance"] < 20:
        return f"Insufficient balance. Your current balance is {users[phone_number]['balance']} KSH. Minimum bet is 20 KSH."

    try:
        number = int(user_input)
        if 1 <= number <= 6:
            users[phone_number]["balance"] -= 20
            results = generate_answers_and_prizes()
            response = f"You selected {number}. Cost: 20 KSH. Your new balance: {users[phone_number]['balance']} KSH.\n\nHere are 6 answers with prizes:\n\n"
            for i, (answer, prize) in enumerate(results, 1):
                response += f"{i}. {answer}: {prize} KSH\n"

            # Check if user won
            if number <= len(results):
                won_prize = results[number - 1][1]
                users[phone_number]["balance"] += won_prize
                response += f"\nCongratulations! You won {won_prize} KSH. Your new balance: {users[phone_number]['balance']} KSH."

            users[phone_number]["last_played"] = datetime.now()
            return response
        else:
            return "Please send a number between 1 and 6."
    except ValueError:
        return "Invalid input. Please send a number between 1 and 6 or 'DEPOSIT [amount]' to add funds."


# Simulate SMS interaction
def simulate_sms():
    phone_number = input("Enter your phone number: ")
    while True:
        user_sms = input("Enter your message (or 'quit' to exit): ")
        if user_sms.lower() == 'quit':
            break
        response = process_sms(phone_number, user_sms)
        print("\nSMS Response:")
        print(response)
        print("\nCurrent balance:", users.get(phone_number, {}).get("balance", 0), "KSH")


simulate_sms()