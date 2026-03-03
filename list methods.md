

## 1. Adding Elements

These methods allow you to grow your list dynamically.

* `append(element)`:
    Adds a single element to the **end** of the list.
* `extend(iterable)`:
    Appends all elements from another list (or any iterable) to the end.
* `insert(index, element)`:
    Inserts an element at a **specific position**.

## 2. Removing Elements

Tools for pruning your data. Note the difference between removing by value vs. removing by position.

* `pop([index])`: Removes and **returns** the element at the given index (defaults to the last item).
* `remove(element)`: Removes the **first occurrence** of a specific value. Raises `ValueError` if the value isn't there.
* `clear()`: Removes **all** elements, leaving you with an empty list `[]`.

## 3. Finding and Counting

Use these to query the contents of your list.

* `index(element)`: Returns the index of the first occurrence of a value.
* `count(element)`: Returns the total number of times a value appears in the list.

## 4. Ordering and Reversing

These methods change the sequence of your data.

* `sort(key=None, reverse=False)`: Sorts the list in place (ascending by default).
* `reverse()`: Reverses the order of the elements in place.

---

## 5. Copying and Utility

* `copy()`: Returns a **shallow copy** of the list (useful if you want to modify a list without changing the original).

### Summary Table: Modifiers vs. Accessors

| Method | Modifies Original? | Returns Value? |
| --- | --- | --- |
| `append()` | **Yes** | No (`None`) |
| `pop()` | **Yes** | **Yes** (The removed item) |
| `sort()` | **Yes** | No (`None`) |
| `index()` | No | **Yes** (The index) |
| `copy()` | No | **Yes** (A new list) |

---

### Pro-Tip: List Slicing

While not technically "methods," **slicing** is often more powerful for manipulation.

* `my_list[::-1]` (Returns a reversed copy)
* `my_list[1:4]` (Returns a sub-section of the list)
