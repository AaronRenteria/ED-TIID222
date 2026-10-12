import random
random.seed(1276)
nums = [3,5,1,2,4]
tries = 0
while nums != sorted(nums):
    random.shuffle(nums)
    tries += 1
    print(nums,tries)