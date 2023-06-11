def print_triangle_pattern(n):
    for i in range(1, n + 1):
        row = [str(j) for j in range(1, i + 1)]
        print(" ".join(row))
    for i in range(n - 1, 0, -1):
        row = [str(j) for j in range(1, i + 1)]
        print(" ".join(row))


def print_multiplication_table(n):
    for i in range(1, n + 1):
        row = [i * j for j in range(1, n + 1)]
        print(" ".join(f"{num:2d}" for num in row))


def get_valid_number_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Enter -1 to exit.")
    max_prompts = 5  # Maximum number of prompts before exiting
    num_prompts = 0  # Counter for the number of prompts

    while num_prompts < max_prompts:
        num = get_valid_number_input("Please enter a number: ")
        num_prompts += 1

        if num == -1:
            print("Bye!")
            break

        command = input("Please enter command (triangle/mp): ")

        if command == "triangle":
            print_triangle_pattern(num)
        elif command == "mp":
            print_multiplication_table(num)
        else:
            print("Invalid command")

        if num_prompts == max_prompts:
            print("Maximum number of prompts reached. Exiting.")
            break


if __name__ == "__main__":
    main()
