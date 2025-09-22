import time
time_set=30

while time_set>0:
    print(time_set)
    # time.sleep(1)
    time_set -= 1

print("done")


for number in range(1, 11):
    print(f'7 x {number}= {number*7}')

for n in range(1, 11):
    for m in range(1, 11):
        print(f'{n} x {m}= {n*m}')
