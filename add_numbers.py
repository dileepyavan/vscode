def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


if __name__ == '__main__':
    result = add(3, 5)
    assert result == 8, f"Expected 8, got {result}"
    print(f"add(3, 5) = {result}")

    result2 = add(1.5, 2.5)
    assert result2 == 4.0, f"Expected 4.0, got {result2}"
    print(f"add(1.5, 2.5) = {result2}")
