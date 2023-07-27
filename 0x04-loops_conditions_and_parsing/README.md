# Loops, conditions and parsing

Loops, conditions, and parsing are fundamental concepts in programming that allow you to control the flow of your code and process data efficiently.


[Overview of each concept:]()

1. [Loops:]()
Loops are used to repeat a block of code multiple times until a specific condition is met.

There are mainly three types of loops in most programming languages:

a) [While loop:]()
It is a loop which continue executing the code block as long as the condition remains True.

b) [For loop (or For Each loop in some languages):]()
The loop iterates over a sequence (e.g., a list, array, or range) and executes the code block for each item in the sequence.

c) [Do-While loop (or Repeat-Until loop in some languages):]()
The loop first executes the code block and then checks the condition. If the condition is True, the loop continues; otherwise, it breaks out of the loop.


2. [Conditions (if-else, elif, and switch/case):]()
Conditions are used to make decisions in your code based on certain conditions being True or False.

a. [If-else statement:]()
In this condition, the else block is optional and will be executed only if the condition in the if statement is False.

b. [Elif statement (else if):]()
In this condition, the elif block is used to check additional conditions if the preceding conditions are False.

c. [Switch/Case statement (in some languages, but not in Python):]()
In this condition, the switch/case statement allows you to test the value of a variable against multiple cases and execute code based on the matching case. However, in Python, you typically use if-elif-else statements for the same purpose.


3. [Parsing:]()
Parsing refers to the process of extracting meaningful data from a given input, such as a file, user input, or a string. It involves breaking the input into smaller components or tokens and analyzing them.

For example, parsing a CSV file involves splitting the lines into fields using a delimiter (e.g., comma), which allows you to work with the individual values in each column.

In many programming languages, you can use built-in functions or libraries to perform parsing tasks effectively.

[Note That:]() These concepts are essential for controlling program flow, making decisions, and processing data in various programming languages. Depending on the language you're using, there may be some differences in syntax and available functionalities, but the core concepts remain the same across most languages.


## Why this concept?

1. [How to create SSH keys:]()

SSH keys are used for secure authentication between a client and a server. To create SSH keys on a Unix-like system (e.g., Linux or macOS), you can use the `ssh-keygen` command.

In a terminal and follow these steps:

a. [Generate an SSH key pair:]()
```
ssh-keygen -t rsa -b 4096
```
or `ssh-keygen -t rsa`

This command will generate a new RSA key pair (public and private keys) with 4096 bits. It will prompt you to choose the file location for the keys, and you can press Enter to accept the default location (`~/.ssh/id_rsa` for the private key and `~/.ssh/id_rsa.pub` for the public key).

b. [Optionally](), you can add a passphrase for added security, but it is not mandatory.


2. [Advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`:]()

The shebang line at the beginning of a script (`#!/bin/bash` or `#!/usr/bin/env bash`) specifies the interpreter to be used for executing the script.

The advantage of using `#!/usr/bin/env bash` is that it allows for better portability. When you use `#!/usr/bin/env bash`, the system searches for the `bash` executable in the user's PATH environment variable, which means the script will work regardless of its absolute path on the system. This is helpful in scenarios where the path to bash might vary between different systems.


3. [How to use while, until, and for loops:]()

a. [While loop:]()
```
while condition
do
    # Code to be executed while the condition is true
done
```

b. [Until loop:]()
```
until condition
do
    # Code to be executed until the condition becomes true
done
```

c. [For loop (to iterate over a list or sequence of values):]()
```
for variable in value1 value2 value3 ...
do
    # Code to be executed for each value in the list
done
```


4. [How to use if, else, elif, and case condition statements:]()

a. [If statement:]()
```
if condition
then
    # Code to be executed if the condition is true
fi
```

b. [If-else statement:]()
```
if condition
then
    # Code to be executed if the condition is true
else
    # Code to be executed if the condition is false
fi
```

c. [If-elif-else statement:]()
```
if condition1
then
    # Code to be executed if condition1 is true
elif condition2
then
    # Code to be executed if condition1 is false and condition2 is true
else
    # Code to be executed if both condition1 and condition2 are false
fi
```

d. [Case statement (to handle multiple conditions):]()

```
case $variable in
    pattern1)
        # Code to be executed if $variable matches pattern1
        ;;
    pattern2)
        # Code to be executed if $variable matches pattern2
        ;;
    *)
        # Code to be executed if $variable doesn't match any pattern
        ;;
esac
```


5. [How to use the cut command:]()

The `cut` command is used to extract specific columns or fields from a file or input stream.

[Synthax:]()
```
cut -d DELIMITER -f FIELDS FILE
```

[Example:]()
```
# Extract the first and third fields from the 'data.csv' file, where ',' is the delimiter
cut -d ',' -f 1,3 data.csv
```


6. [Files and other comparison operators and how to use them:]()

In bash scripting, you can use various comparison operators to compare strings and numeric values.

Here are some common ones:

=> Numeric comparison operators:

`-eq`: Equal to
`-ne`: Not equal to
`-gt`: Greater than
`-lt`: Less than
`-ge`: Greater than or equal to
`-le`: Less than or equal to

=> String comparison operators:

`=`: Equal to (for strings)
`!=`: Not equal to
`-z`: Empty string (checks if a variable is empty)
`-n`: Non-empty string (checks if a variable is not empty)

[Examples:]()
```
# Numeric comparison
if [ $num1 -eq $num2 ]; then
    echo "Numbers are equal"
fi

# String comparison
if [ "$str1" = "$str2" ]; then
    echo "Strings are equal"
fi
```

These operators can be used within if statements or in other control structures to conditionally execute code based on the comparison results.

[Reference](https://chat.openai.com/)
