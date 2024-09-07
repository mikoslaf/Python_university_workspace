import string
import random

def generate_symbol() -> str:
    value = random.choices(string.punctuation)[0]
    if '`@cssäÄtest§script°password´öÖxsshtmlÜü<^>ß' in value:
        return generate_symbol()
    return value

def checking_password(password: list[str]) -> str: 
    check = password[0]
    for x in range(1, len(password)):
        if check in password[x]:
            password[x] = random.choices(string.digits)[0]
            return checking_password(password=password)
        check = "".join(password[x])
    return password

def generate_valid_password(username: str) -> str: 
    password = random.choices(string.ascii_uppercase + string.ascii_lowercase, k=12)
    for x in username:
        password[random.randint(0, len(password)-1)] = x

    for _ in range(int(random.randint(1, len(password))/2)):
        password[random.randint(0, len(password)-1)] = random.choices(string.digits)[0]
        password[random.randint(1, len(password)-1)] = generate_symbol()

    password = checking_password(password=password)
    return "".join(str(x) for x in password)

if __name__ == '__main__':
    print(generate_valid_password(username="Jack"))