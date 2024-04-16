# Q.1 Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(f'In Feb, {exp[1] - exp[0]} dollars you spent extra compare to January')

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f'your total expense in first quarter is: {exp[0] + exp[1] + exp[2]}')

# 3. Find out if you spent exactly 2000 dollars in any month
print(f'Did you spent exactly 2000 dollars in any month? {2000 in exp}')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print(f'expense at the end of june is {exp[5]}')

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] -= 200
print(f'The corrected expense of April is {exp[3]}')

# Q2. You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(f'Length of the list is {len(heros)}')

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(f'The updated list is {heros}')

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(f'The updated list after insert black panter in the correct location {heros}')

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)

# 5. Sort the list in alphabetical order
heros.sort()
print(f'Sorted array is {heros}')

# Q3. Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

max_num = int(input('Please enter Max Number: '))
odd_num = [num for num in range(1, max_num) if num % 2 ==1]
print(odd_num)