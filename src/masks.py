def get_mask_card_number(number: str) -> str:
    """Функция принимает номер карты строкой и возвращает маску карты # 7000 79** **** 6361"""
    new_string_card = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string_card


def get_mask_account(number: str) -> str:
    """Функция принимает номер счета строкой и возвращает маску счёта # **4305"""
    new_string_account = f"**{number[-4:]}"
    return new_string_account
