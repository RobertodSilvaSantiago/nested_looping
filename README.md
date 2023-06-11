# nested_looping

The provided code defines several functions and a main program that prompts the user for a number and a command. Here's what the code does step by step:

The print_triangle_pattern function takes an input n and prints a triangle pattern using numbers. It uses nested loops to generate the rows of the triangle and prints each row using print(" ".join(row)).

The print_multiplication_table function takes an input n and prints a multiplication table up to the given number. It also uses nested loops to generate the rows and columns of the table and prints each row using print(" ".join(f"{num:2d}" for num in row)).

The get_valid_number_input function prompts the user with a given prompt and ensures that the user enters a valid integer. It uses a while loop and a try-except block to handle invalid input by catching the ValueError and displaying an error message.

The main function is the entry point of the program. It initializes variables for the maximum number of prompts and the current number of prompts. It runs a while loop that prompts the user for a number and a command until the maximum number of prompts is reached or the user enters -1.

Inside the loop, the get_valid_number_input function is called to get a valid number input from the user. If the user enters -1, the program prints "Bye!" and breaks out of the loop.

The user is then prompted for a command ("triangle" or "mp"). Depending on the command, either the print_triangle_pattern or print_multiplication_table function is called with the user's number input.

If an invalid command is entered, the program prints "Invalid command".

If the maximum number of prompts is reached, the program prints "Maximum number of prompts reached. Exiting."

Overall, this program allows the user to enter a number and a command to either print a triangle pattern or a multiplication table. It includes input validation and a maximum prompt limit.





