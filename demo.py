from age_utils import classify_age


def greet() -> None:
    print("Hello, welcome to the age demo!")


def showcase_examples() -> None:
    samples = [12, 13, 18, 25, 60]
    for age in samples:
        print(f"Age {age} -> {classify_age(age)}")


def main() -> None:
    greet()
    showcase_examples()


if __name__ == "__main__":
    main()