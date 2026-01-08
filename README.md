# Age Classification (Modular)

This workspace provides a simple, modular Python program to read a user's age and print whether the user is a Teen, Adult, or Senior Citizen. A small utility module encapsulates parsing and classification logic.

## Files
- `age_utils.py`: Parsing (`parse_age`) and classification (`classify_age`) functions.
- `Age_Validation.py`: Main script that prompts for age and prints the category.
- `demo.py`: Quick demonstration of `classify_age` with sample ages.

## Categories
- Teen: 13–19
- Adult: 20–59
- Senior Citizen: 60+
- Child: <13 (handled for completeness)

## Run

With your virtual environment activated:

```powershell
python Age_Validation.py
```

To run the demo:

```powershell
python demo.py
```
