import random

num = random.randint(0, 10)
print('Number:',num)
attempt = 4
msg = 'You Lost!'

while attempt > 0:
    user_input = int(input('Enter Number: '))

    if user_input == num:
        msg = 'You Won!'
        break
    else:
        print(f'Try again! {attempt} attempt left.')
        attempt -= 1
        continue

print(msg)