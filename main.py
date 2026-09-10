import math
import secrets
import string


def calculate_entropy(length: int, pool_size: int) -> float:
    if length <= 0 or pool_size <= 0:
        return 0.0
    return length * math.log2(pool_size)


def generate_secure_password(length: int) -> str:
    char_pool = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(char_pool) for _ in range(length))


def main():
    print("=" * 50)
    print("  Enterprise Random Password Generator")
    print("=" * 50)

    while True:
        user_input = input(
            "\nEnter desired password length (min 15 recommended): "
        ).strip()

        try:
            length = int(user_input)
            if length < 8:
                print("Error: Length must be at least 8 characters.")
                continue
            if length < 15:
                print(
                    "Warning: NIST SP 800-63-4 recommends at least 15 characters for high security."
                )
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    password = generate_secure_password(length)
    pool_size = len(string.ascii_letters + string.digits + string.punctuation)
    entropy = calculate_entropy(length, pool_size)

    print("\n" + "-" * 50)
    print(f"Generated Password : {password}")
    print(f"Character Pool (R) : {pool_size}")
    print(f"Entropy Strength   : {entropy:.2f} bits")

    if entropy >= 80:
        print("Security Status    : Highly Secure (Enterprise Grade)")
    else:
        print("Security Status    : Moderate / Weak")
    print("-" * 50)


if __name__ == "__main__":
    main()