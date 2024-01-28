import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"(\b([A-Za-z0-9][A-Za-z0-9\.\-\_]+)(@)([A-Za-z]+[\-]?[A-Za-z]+)(\.[\.a-z]+)*\b)"
pattern_at_symbol = r"@"

while True:
    email_address = input()

    matches_at_symbol = re.findall(pattern_at_symbol, email_address, flags=re.IGNORECASE)
    matches = re.findall(pattern, email_address, flags=re.IGNORECASE)

    if not matches_at_symbol:
        raise MustContainAtSymbolError("Email must contain @")

    name = matches[0][1]
    domain = matches[0][4]

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in ['.com', '.bg', '.org', '.net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
