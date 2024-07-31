
# Program Execution Simulator

## Overview

This program simulates the execution of a given program based on a set of instructions and inputs. The simulator reads the instructions and inputs from standard input, executes the instructions step-by-step, and outputs snapshots of each execution step.

## Input Format

The input consists of two parts:

1. **Program Instructions**: A list of natural numbers representing the program's instructions, followed by a newline character.
2. **Program Inputs**: Another list of natural numbers representing the program's inputs.

Each number in the lists is separated by a single space. The inputs are assigned to variables in order. Variable `Y`, all local variables, and any unused input variables are initialized to the default value of 0. Undefined labels default to `[E]`.

### Example Input

```
45 34 350 2 46
2 1
```

## Output Format

The program outputs snapshots of each step of execution. Each snapshot includes:
- The current step number `i`.
- The values of all input variables (from `X1` to the highest indexed input variable used in the program).
- The values of all local variables (from `Z1` to the highest indexed local variable used in the program).
- The value of variable `Y`.

Each snapshot is printed on a new line, with values separated by a single space.

### Example Output

```
1 2 1 0 0 0 0
2 1 1 0 0 0 0
3 1 1 0 0 1 0
4 1 1 0 0 1 0
5 1 1 0 0 1 1
1 1 1 0 0 1 1
2 0 1 0 0 1 1
3 0 1 0 0 2 1
4 0 1 0 0 2 1
5 0 1 0 0 2 2
```

## Example Explanation

Given the input:
```
45 34 350 2 46
2 1
```

This translates to the following program:

```
[A1] X1 <- X1 - 1
Z2 <- Z2 + 1
IF X3 !=0 GOTO B1
Y <- Y + 1
IF X1 != 0 GOTO A1
```

The output shows the snapshots of each step of the program execution.

## Usage

To use this program, provide the instructions and inputs as described in the input format. The program will then simulate the execution and print the snapshots of each step.

### Running the Program

You can run the program by executing the following command and providing the input:

```bash
python Universal Program.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
