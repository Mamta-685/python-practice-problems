# find_max.py

# if list empty -> print message
# set first element as largest
# loop through numbers
# update largest if number is bigger
# print largest

def find_max(nums):
    if not nums:
        return None
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest


if __name__ == "__main__":
    print(find_max([1, 5, 3]))   
    print(find_max([10, -2, 7]))  
    print(find_max([4]))         
    print(find_max([]))           

