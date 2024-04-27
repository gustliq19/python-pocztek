import random


def generate_id():
    new_id = random.randint(1, 999)
    return str(new_id).zfill(5)


def run():
    random_id = generate_id()
    print(f"Wygenerowano ID: {random_id}")


if __name__ == "__main__":
    run()
