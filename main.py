import random

def generate_answers_and_prizes():
    answers = ["Answer A", "Answer B", "Answer C", "Answer D", "Answer E", "Answer F"]
    prizes = [f"${random.randint(10, 100)}" for _ in range(6)]
    return list(zip(answers, prizes))

def process_sms(user_input):
    try:
        number = int(user_input)
        if 1 <= number <= 6:
            results = generate_answers_and_prizes()
            response = f"You selected {number}. Here are 6 answers with prizes:\n\n"
            for i, (answer, prize) in enumerate(results, 1):
                response += f"{i}. {answer}: {prize}\n"
            return response
        else:
            return "Please send a number between 1 and 6."
    except ValueError:
        return "Invalid input. Please send a number between 1 and 6."

# Simulate SMS interaction
user_sms = input("Enter a number between 1 and 6: ")
response = process_sms(user_sms)
print("\nSMS Response:")
print(response)