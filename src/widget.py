from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция получает строку и маскирует счет/карту"""
    if len(number.split( )[-1]) == 16:
        new_number = get_mask_card_number(number.split( )[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split( )[-1]) == 20:
        new_number = get_mask_account(number.split( )[-1])
        result = f"{number[:-20]}{new_number}"
        return result

# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Счет 73654108430135874305"))

def get_new_data(old_data: str) ->str:
    """Функция принимает строку с датой
     и выводит в формате dd.mm.yyyy"""
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])



