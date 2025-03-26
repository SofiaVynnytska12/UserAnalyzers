import os
import numpy as np
import requests


def main():
    test_var = os.getenv("TEST_VARIABLE", "no environment variable set")
    print(f"You are inside the container! The TEST_VARIABLE is: {test_var}")

    try:
        response = requests.get("https://api.github.com", timeout=5)
        response.raise_for_status()
        print(f"\nChecking requests! Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"\nRequest failed: {e}")

    random_array = np.random.random(5)
    print(f"\nChecking numpy! Random array: {random_array}")


if __name__ == "__main__":
    main()
