# Number Sequence Analyzer

# Step 1: Get input from user
num = int(input("Enter a number: "))

# Step 2: Initialize sum
total_sum = 0

# Step 3: Loop from 1 to num
for i in range(1, num + 1):
    # Add to sum
    total_sum += i
    
    # Check even or odd
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")

# Step 4: Display total sum
print(f"\nTotal sum from 1 to {num} is: {total_sum}")