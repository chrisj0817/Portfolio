


speed = int(input("Enter your speed: "))
birthday = input("Is it your birthday? (yes or no): ")


if birthday.lower() == "yes":
    speed -= 5

if speed <= 60:
    result = 0
    message = "No ticket! You’re driving safely."
elif 61 <= speed <= 80:
    result = 1
    message = "Small ticket. Be careful next time!"
else:
    result = 2
    message = "Big ticket! You were going way too fast!"


print(f"Your ticket code is: {result}")
print(message)
