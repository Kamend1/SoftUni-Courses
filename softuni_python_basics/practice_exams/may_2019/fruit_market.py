price_strawberries_bgn = float(input())
number_bananas_kg = float(input())
number_oranges_kg = float(input())
number_redberries_kg = float(input())
number_strawberries_kg = float(input())
price_redberries_bgn = 0.50 * price_strawberries_bgn
price_oranges_bgn = 0.60 * price_redberries_bgn
price_bananas_bgn = 0.20 * price_redberries_bgn

amount_needed = price_strawberries_bgn * number_strawberries_kg \
                + price_bananas_bgn * number_bananas_kg \
                + price_oranges_bgn * number_oranges_kg \
                + price_redberries_bgn * number_redberries_kg

print(f"{amount_needed:.2f}")
