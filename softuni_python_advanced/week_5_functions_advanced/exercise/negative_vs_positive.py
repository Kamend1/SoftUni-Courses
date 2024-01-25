def negative_vs_positive(*args):

    positive = sum(num for num in args if num > 0)
    negative = sum(num for num in args if num < 0)

    print(negative, positive, sep='\n')
    if positive > abs(negative):
        print('The positives are stronger than the negatives')
    else:
        print("The negatives are stronger than the positives")

nums = [int(x) for x in input().split()]
negative_vs_positive(*nums)
