def media(*nums):
    total = 0
    for num in nums:
        total += num
    total /= len(nums)
    return total

media(10,10,20)

print(media(10,10,20,15))