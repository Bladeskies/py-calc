# Creates add function

def add(num1, num2):
    ans = int(num1) + int(num2)
    answer = str(ans)

    print("The answer is " + answer + "!")


# Collects first number

print("What's your first number?")
fn = input()

# Collects second number

print("What's your second number?")
sn = input()

# Gives answer

add(fn, sn)
