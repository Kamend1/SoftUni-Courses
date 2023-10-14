qty_food = float(input()) * 1000
qty_hay = float(input()) * 1000
qty_cover = float(input()) * 1000
guinea_pig_wgt = float(input()) * 1000

for day in range(1, 31):
    qty_food -= 300
    if qty_food < 0:
        print("Merry must go to the pet store!")
        break
    if day % 2 == 0:
        qty_hay -= 0.05 * qty_food
        if qty_hay < 0:
            print("Merry must go to the pet store!")
            break
    if day % 3 == 0:
        qty_cover -= guinea_pig_wgt / 3
        if qty_cover < 0:
            print("Merry must go to the pet store!")
            break

if qty_food >=0 and qty_hay >=0 and qty_cover >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {round(qty_food/1000, 2):.2f}, Hay: {round(qty_hay/1000, 2):.2f}, "
          f"Cover: {round(qty_cover/1000, 2):.2f}.")
