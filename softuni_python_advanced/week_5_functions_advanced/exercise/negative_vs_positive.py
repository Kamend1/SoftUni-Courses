def negative_vs_positive(*args):
    positive = []
    negative = []

    for num in args:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)
    print(sum(negative), sum(positive), sep='\n')
    if sum(positive) > abs(sum(negative)):
        print('The positives are stronger than the negatives')
    else:
        print("The negatives are stronger than the positives")

nums = [int(x) for x in input().split()]
negative_vs_positive(*nums)
