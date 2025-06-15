# Python Data Types and Type Casting

## 1. Getting the Data Type in Python

You can use the built-in `type()` function to find out the data type of a variable.

```python
x = 5
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>
```

---

## 2. Type Casting in Python

### ✅ Implicit Casting

Python automatically converts one data type to another when needed (usually from a smaller to a larger type).

```python
x = 5        # int  
y = 2.0      # float

result = x + y  # Python implicitly casts `x` to float
print(result)   # Output: 7.0
print(type(result))  # Output: <class 'float'>
```

### 🛠️ Explicit Casting

You can manually convert data types using constructor functions like `int()`, `float()`, `str()`, etc.

```python
num = "10"               # str  
converted = int(num)     # str -> int  
print(converted)         # Output: 10  
print(type(converted))   # Output: <class 'int'>
```

---

## 3. 🧪 Common Type Conversion Functions

| Function  | Description          | Example            |
|----------|----------------------|--------------------|
| `int()`  | Convert to integer    | `int("7") → 7`     |
| `float()`| Convert to float      | `float("3.5") → 3.5`|
| `str()`  | Convert to string     | `str(100) → "100"` |
| `bool()` | Convert to boolean    | `bool("") → False` |
