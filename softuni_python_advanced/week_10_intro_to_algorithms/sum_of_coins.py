def choose_coins(coins, target):
    coins.sort(reverse=True)
    index = 0
    coins_used = {}

    while target > 0  and index < len(coins):
        count_current_coins = target // coins[index]
        target = target % coins[index]

        if count_current_coins > 0:
            coins_used[coins[index]] = coins_used.get(coins[index], 0) + count_current_coins

        index += 1

        if target != 0:
            result = "Error"
        else:
            result = f"Number of coins to take: {sum(coins_used.values())}"
            for k, v in coins_used.items():
                result += f"\n{v} coin(s) with value {k}"

    return result

coins = [int(x) for x in input().split(', ')]
target = int(input())
print(choose_coins(coins, target))
