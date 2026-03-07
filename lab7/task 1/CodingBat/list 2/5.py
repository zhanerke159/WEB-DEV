def sum67(nums):
    total = 0
    skip = False
    
    for n in nums:
        if n == 6:
            skip = True
        elif n == 7 and skip:
            skip = False
        elif not skip:
            total += n
            
    return total
