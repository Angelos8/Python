def ace_card(card_list:list):
    if sum(card_list) > 21:
        index = card_list.index(11)
        card_list[index] = 1
    return card_list

            
