def greet_user(name: str) -> str:
  return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(greet_user("Tanmay"))
    print("Sum of 5 and 3 is:", add_numbers(5, 3))
