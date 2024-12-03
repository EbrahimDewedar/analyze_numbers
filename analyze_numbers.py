listing= [1,2,5,-4,-8,7,-20]

def analysis_numbers(nums):
    pos=0
    neg= 0
    for num in nums:
        if num> 0:
            print(f'{num} is positives')
            pos+=num
        else:
            print(f'{num} is negative')
            neg+=num
    
    print(f'total of positive is {pos}')
    print(f'total of negative is {neg}')

analysis_numbers(listing)