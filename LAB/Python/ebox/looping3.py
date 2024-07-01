"""
The Event Organizing Company "Buzzcraft" focuses event management in a way 
that creates a win-win situation for all involved stakeholders.
Buzzcraft don't look at building one time associations with clients, instead, 
aim at creating long-lasting collaborations that will span years to come. 
This goal of the company has helped them evolve and expand big with organizing many events till date.
The number of events that the company organizes every month is recorded sensibly 
and is seemed to have followed a specific series like: 30, 35, 38, 41, 54, 53 ...

Write a program which takes an integer N as the input and will output the series till the Nth term.
"""
n = int(input("Enter the number of terms: "))
count = 30
newlist = []

for x in range(n):
    newlist.append(count)
    
    # Cycle through the pattern every 10 terms
    cycle_position = x % 10
    
    if cycle_position == 0:
        count += 5
    elif cycle_position == 1:
        count += 3
    elif cycle_position == 2:
        count += 3
    elif cycle_position == 3:
        count += 13
    elif cycle_position == 4:
        count -= 1
    elif cycle_position == 5:
        count += 25
    elif cycle_position == 6:
        count -= 7
    elif cycle_position == 7:
        count += 39
    elif cycle_position == 8:
        count -= 15
    elif cycle_position == 9:
        count += 0  # No change, just to complete the cycle

# Simplified print statement
print(*newlist)
