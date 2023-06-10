def print_triangle(n):
    if n == -1:
        print("Bye!")
        return False

    command = input("Please enter command (triangle/mp): ")

    if command == "mp":
        for i in range(1, n + 1):
            row = [i * j for j in range(1, n + 1)]
            print(" ".join(f"{num:2d}" for num in row))
    elif command == "triangle":
        for i in range(1, n + 1):
            row = [str(j) for j in range(1, i + 1)]
            print(" ".join(row))
        for i in range(n - 1, 0, -1):
            row = [str(j) for j in range(1, i + 1)]
            print(" ".join(row))
    else:
        print("Invalid command")

    return True


print("Enter -1 to exit.")
max_prompts = 5  # Maximum number of prompts before exiting
num_prompts = 0  # Counter for the number of prompts

while num_prompts < max_prompts:
    num = int(input("Please enter a number: "))
    num_prompts += 1
    if not print_triangle(num):
        break

    if num_prompts == max_prompts:
        print("Maximum number of prompts reached. Exiting.")
        break
