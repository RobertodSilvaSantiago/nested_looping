# nested_looping

This code defines a function called print_triangle that takes an integer n as input. The function prompts the user for a command and then performs different actions based on the command.

Here's a breakdown of what the code does:

The function starts by checking if the input n is equal to -1. If it is, the function prints "Bye!" and returns False to indicate that the program should exit.

If n is not -1, the function prompts the user to enter a command by using the input function and assigns the input to the variable command.

If the command is "mp", the function enters a loop that iterates from 1 to n. In each iteration, it creates a list called row where each element is the product of i and j, where i is the current iteration value and j ranges from 1 to n. Then, it prints the elements of row separated by spaces.

If the command is "triangle", the function enters a loop that iterates from 1 to n. In each iteration, it creates a list called row where each element is a string representation of j, where j ranges from 1 to i. Then, it prints the elements of row separated by spaces. This loop prints an upward triangle.

After printing the upward triangle, the function enters another loop that iterates from n-1 down to 1. In each iteration, it creates a list called row where each element is a string representation of j, where j ranges from 1 to i. Then, it prints the elements of row separated by spaces. This loop prints a downward triangle.

If the command is neither "mp" nor "triangle", the function prints "Invalid command".

The function returns True to indicate that the program should continue.

Outside the function, there is a loop that allows the user to enter a number and execute the print_triangle function. The loop continues until either the user enters -1 or the maximum number of prompts (max_prompts) is reached. If the maximum number of prompts is reached, the program prints "Maximum number of prompts reached. Exiting." and breaks out of the loop.
