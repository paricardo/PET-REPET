import re


def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def format_phone(phone):
    numbers = re.sub(r'\D', '', phone)

    if len(numbers) == 11:
        return f"({numbers[:2]}) {numbers[2:7]}-{numbers[7:]}"
    
    return phone


def format_cpf(cpf):
    numbers = re.sub(r'\D', '', cpf)

    if len(numbers) == 11:
        return (
            f"{numbers[:3]}."
            f"{numbers[3:6]}."
            f"{numbers[6:9]}-"
            f"{numbers[9:]}"
        )