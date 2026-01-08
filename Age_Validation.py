from age_utils import parse_age, classify_age


def prompt_for_age() -> int:
	"""Prompt user for age until a valid integer is entered."""
	while True:
		raw = input("Enter your age: ")
		try:
			return parse_age(raw)
		except ValueError as e:
			print(f"Invalid input: {e}")


def print_age_category(age: int) -> None:
	"""Compute and print the age category."""
	category = classify_age(age)
	# If you only want Teen/Adult/Senior, you can branch here.
	print(f"You are a {category}.")


def main() -> None:
	age = prompt_for_age()
	print_age_category(age)


if __name__ == "__main__":
	main()
