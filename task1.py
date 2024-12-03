# In this task, we need to output each element of array [8,3,5,1] as an integer, and we will use Scientific notation to complete this task

# Code logic:
# 1. Initialize a variable 'result' to store the calculation results
# 2. Use a for loop with index to traverse the array
# 3. Calculate the number of digits of the current number through index and list length, and use it as the square of Scientific notation
# 4. Accumulate each calculated result into the 'result' variable
nums = [8, 3, 5, 1]
# Initialize a variant to keep the final result
result = 0
# Traverse the list to get each number in this list by for loop
# "len(nums)" is the length of the list "nums" = 4
# Set variant 'i' as the index in the for loop, which is in [0, len(nums)) = [0, 4)
for i in range(len(nums)):
    # '+' is addition, '-' is subtraction, '*' is multiplication, '**' is square
    # "result += ..." is means "result = result + ...", which is the self update of 'result'
    # "nums[i]" means the i-th element in the list "nums". When i = 0, num[i] = num[0] = 8
    # Due to the first number is the largest number, we should calculate the square number for the largest one.
    # However, 'i' is starting from 0, we should add 1 for 'i' to get the correct square number
    result += nums[i] * 10**(len(nums) - (i + 1))

print(result)   # print the result
