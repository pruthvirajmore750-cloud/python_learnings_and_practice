Python data types determine the kind of value a variable can hold and define the operations that can be performed on that value.

There are several built-in data types in Python, including:

1. string
2. bool
3. int
4. float
5. complex
6. list
7. tuple
8. set
9. dict

---

### 1. String (`str`)
- Strings are sequences of characters enclosed in quotes: single (`'...'`), double (`"..."`), or triple (`'''...'''`/`"""..."""`).
- They are **immutable**, meaning once created, their contents cannot be changed.
- **Example:**
  ```python
  s = "Hello, world!"
  ```

### 2. Boolean (`bool`)
- Represents truth values: `True` or `False`.
- Under the hood, `True` is equal to `1` and `False` to `0`.
- **Usage:**
  ```python
  flag = True
  ```

### 3. Integer (`int`)
- Whole numbers without a fractional part.
- They can be positive, negative, or zero and have arbitrary precision.
- **Example:**
  ```python
  count = 42
  ```

### 4. Float (`float`)
- Numbers with a decimal point (floating‑point numbers).
- Used when fractional values are required.
- **Example:**
  ```python
  pi = 3.14159
  ```

### 5. Complex (`complex`)
- Numbers with a real and imaginary part, written as `a + bj`.
- Useful for scientific and engineering calculations.
- **Example:**
  ```python
  z = 2 + 3j
  ```

### 6. List (`list`)
- Ordered collection of values separated by commas and enclosed in square brackets `[]`.
- Lists are **mutable**; items can be added, removed, or modified.
- Can hold mixed data types.
- **Example:**
  ```python
  nums = [1, 2, 3, "four", True]
  ```

### 7. Tuple (`tuple`)
- Similar to lists but **immutable**.
- Defined with parentheses `()` (parentheses optional in some contexts).
- Useful for fixed collections of items.
- **Example:**
  ```python
  point = (10, 20)
  ```

### 8. Set (`set`)
- Unordered collection of **unique** elements.
- Mutable; supports operations like union, intersection, difference.
- Defined with curly braces `{}` or the `set()` constructor.
- **Example:**
  ```python
  unique_colors = {"red", "green", "blue"}
  ```

### 9. Dictionary (`dict`)
- Unordered collection of key–value pairs.
- Keys must be immutable (e.g. strings, numbers, tuples); values can be any type.
- Defined with curly braces and colons: `{key: value}`.
- **Example:**
  ```python
  person = {"name": "Alice", "age": 30}
  ```

---

> **Note:** Python is dynamically typed, so you don't need to declare a variable's data type explicitly. The interpreter infers it from the assigned value.