# ---------- Task 1: Leap Year ----------
# a simple function that checks if a year is leap or not .
def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


# ---------- Task 2: CM to Inches ----------
# a simple function that converts CM TO INCHES  
def cm_to_inches(cm: float) -> float:
    return cm / 2.54


# ---------- Task 3: Split Full Name ----------
# a function which divides the first and last names by a space 
def split_full_name(full_name: str) -> tuple[str, str]:
    parts = full_name.strip().split()
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], " ".join(parts[1:])


# ---------- Task 4: Count Vowels ----------
# a simple function that counts the number of vowels in a given string 
def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in "aeiou")


# ---------- Task 5: Count Lines in File ----------
# a simple function that counts no.of lines in a given file path ....  
def count_lines_in_file(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        return sum(1 for _ in f)


# ---------- Main Testing Area ----------

if __name__ == "__main__":

    # Test leap year
    examples = [1900, 2000, 2004, 2001]
    for y in examples:
        print(f"{y}: {'leap' if is_leap_year(y) else 'not leap'}")

    # Test cm to inches
    print("170 cm =", cm_to_inches(170), "inches")

    # Test name split
    first, last = split_full_name("Ram Charan")
    print("First:", first)
    print("Last:", last)

    # Test vowel count
    print("Vowels in 'Computer Science':", count_vowels("Computer Science"))

    # Test file line count (give valid file path)
    print("Lines:", count_lines_in_file("file.txt"))
