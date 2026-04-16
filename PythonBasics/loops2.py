
# while loop ---> is used to check a condition
# it will iterate till the condition is false

it = 10

while it>1:
    if it==9:
        it = it - 1
        continue # means skip the below executions and restart the loop
    if it==3:
        break
    print(it)
    it = it - 1

print('while loop execution is done')



