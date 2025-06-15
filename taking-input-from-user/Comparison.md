# 🧍 Taking Input from a User: Python vs Java vs C#

## Similarities
✅ All three languages use built-in functions to read user input from the console.  
✅ Each requires a way to **parse or convert input** from string to number types (like `int`).  
✅ All support formatted output to include variables in print statements.

---

## Differences

| Feature                  | Python                          | Java                                  | C#                                      |
|--------------------------|----------------------------------|----------------------------------------|------------------------------------------|
| Input Function           | `input()`                       | `Scanner.nextLine()`, `nextInt()`     | `Console.ReadLine()`                    |
| Type Conversion          | `int(input())`                  | Manual parsing using `nextInt()`      | `Convert.ToInt32()`                     |
| Simplicity               | Most concise                    | More boilerplate                      | Balanced                                |
| Requires Import?         | No                              | Yes (`import java.util.Scanner;`)     | No                                       |
| String Interpolation     | `f"Hello {name}"`               | `"Hello " + name`                     | `$"Hello {name}"`                       |

---

## Notes
- Java requires more setup (Scanner, imports).
- Python is the fastest to prototype with.
- C# balances simplicity and structure well for typed applications.
