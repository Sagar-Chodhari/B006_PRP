def parse_age(text: str) -> int:
    """Parse and validate an age from user input.

    Accepts integers. Raises ValueError for invalid or negative values.
    """
    s = text.strip()
    if not s:
        raise ValueError("Age cannot be empty.")
    try:
        age = int(s)
    except ValueError as e:
        raise ValueError("Please enter a whole number for age.") from e
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age


def classify_age(age: int) -> str:
    """Classify age into a category.

    Categories:
    - Teen: 13-19
    - Adult: 20-59
    - Senior Citizen: 60+
    - Child: <13 (returned for completeness)
    """
    if age < 13:
        return "Child"
    if 13 <= age <= 19:
        return "Teen"
    if 20 <= age <= 59:
        return "Adult"
    return "Senior Citizen"
