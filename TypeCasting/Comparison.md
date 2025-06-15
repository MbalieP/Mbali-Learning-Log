# 🔍 Type Casting: Python vs Java vs C#

## 🧩 Similarities

✅ All three languages support both **implicit (widening)** and **explicit (narrowing)** type casting.  
✅ Java and C# use `(type)` syntax for manual/explicit conversions.  
✅ Python’s built-in functions like `int()`, `float()` are conceptually similar to `Convert.ToInt32()` in C#.  

---

## 🧬 Differences

| Feature                         | Python                              | Java                                        | C#                                               |
|----------------------------------|--------------------------------------|---------------------------------------------|--------------------------------------------------|
| **Typing**                      | Dynamically typed                   | Statically typed                            | Statically typed                                  |
| **Implicit Casting**            | Flexible and automatic              | Allowed only for widening conversions       | Allowed for widening conversions                 |
| **Explicit Casting**            | Done via functions: `int()`, `float()` | Done via `(type)` syntax                    | Done via `(type)` or methods in `Convert` class  |
| **String to Number Conversion** | `int("123")`, `float("3.14")`       | `Integer.parseInt("123")`                   | `int.Parse("123")`, `Convert.ToInt32("123")`     |
| **Safe Conversion**             | Use `try-except`                    | Use `try-catch` with parsing                | Use `TryParse()` to avoid exceptions             |
| **Truncation on Casting**       | Yes (`int(5.99)` → `5`)             | Yes (`(int)5.99` → `5`)                     | Yes (`(int)5.99` → `5`)                           |

---

## 🔒 Notable Language Behavior

- **Python**: Prioritizes ease of use, automatically handles many conversions.  
- **Java**: Strict and verbose with conversions; prevents accidental data loss.  
- **C#**: Balanced — strict like Java, but offers helper methods like `TryParse()` for safety.

---

## 🧠 Tip

Use **safe casting** methods when dealing with **user input** or **external data** to avoid runtime errors, especially in **Java** and **C#**.

