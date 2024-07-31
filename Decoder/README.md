
# S Language Instruction Translator

## Overview

This program translates a series of natural numbers from input into instructions in the S language. Each input number corresponds to a specific S language instruction.

## Input Format

The input consists of a single line of natural numbers separated by spaces.

### Example Input

```
21 46
```

## Output Format

For each input number, the program prints a corresponding S language instruction.

### Example Output

```
[A1] X1 <- X1 + 1
IF X1 != 0 GOTO A1
```

## Usage

To use this program, provide the natural numbers as described in the input format. The program will then translate each number into an S language instruction and print the result.

### Running the Program

You can run the program by executing the following command and providing the input:

```bash
python Decoder.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
