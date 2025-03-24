import os


def main():
    test_var = os.getenv("TEST_VARIABLE", "no environment variable set")
    print(f"You are inside the container and it's test! The TEST_VARIABLE is: {test_var}")


if __name__ == "__main__":
    main()
