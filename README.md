# Text-to-Brainfuck

A Text to Brainfuck converter, useful to try this language.

## What is Brainfuck?

Brainfuck is a minimalist esoteric programming language created by Urban Müller in 1993. It consists of only **eight commands** and operates on an array of memory cells, each initially set to zero. The language is known for its **extreme simplicity and difficulty to read**, making it a challenge for programmers.

### Brainfuck Commands:

| Command | Meaning |
|---------|---------|
| `>` | Move the memory pointer to the right |
| `<` | Move the memory pointer to the left |
| `+` | Increment the value at the current memory cell |
| `-` | Decrement the value at the current memory cell |
| `.` | Output the ASCII character at the current memory cell |
| `,` | Input a character and store it in the current cell |
| `[` | Jump past matching `]` if the current cell is 0 |
| `]` | Jump back to matching `[` if the current cell is nonzero |

## How to Use

### Install dependencies

```bash
$> apt install python3
```

### Run

#### Write & Translate

```bash
$> python3 src/converter.py
```

Write your **sentence** in the **shell** started by the script. The program should **automatically translate it**.

Example:
```bash
$> Hello, World!
```

#### Input File

```bash
$> python3 src/converter.py [FilePath]
```

Write your **file path** as an **argument** of the the script. If the file does exists, then the script should **find**, **open** and **read** the file and **translate** it.

Example:
```bash
$> echo Hi! > hi.txt
$> python3 src/converter.py hi.txt
```
This script should translate **"Hi!"** to Brainfuck.


