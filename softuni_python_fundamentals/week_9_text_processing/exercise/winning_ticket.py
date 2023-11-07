tickets = input().split(",")
winning_combinations = ["$$$$$$", "$$$$$$$", "$$$$$$$$", "$$$$$$$$$", "$$$$$$$$$$",
                        "@@@@@@", "@@@@@@@", "@@@@@@@@", "@@@@@@@@@", "@@@@@@@@@@",
                        "######", "#######", "########", "#########", "##########",
                        "^^^^^^", "^^^^^^^", "^^^^^^^^", "^^^^^^^^^", "^^^^^^^^^^"]

for index in range(len(tickets)):
    ticket = tickets[index]
    tickets[index] = ticket.strip()


for ticket in tickets:
    has_twenty_characters = False
    has_symbols_in_first_half = False
    has_symbols_in_second_half = False
    is_valid = False
    combination_symbol = ""
    combination_length = 0
    if len(ticket) == 20:
        has_twenty_characters = True
        for combination in winning_combinations:
            if combination in ticket[:10]:
                has_symbols_in_first_half = True
                if combination in ticket[10:]:
                    has_symbols_in_second_half = True
                    is_valid = True
                    combination_symbol = combination[0]
                    combination_length = len(combination)
                else:
                    has_symbols_in_first_half = False

    if not has_twenty_characters:
        print("invalid ticket")
    if is_valid:
        if combination_length < 10:
            print(f'ticket "{ticket}" - {combination_length}{combination_symbol}')
        else:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
    if has_twenty_characters and not is_valid:
        print(f'ticket "{ticket}" - no match')
