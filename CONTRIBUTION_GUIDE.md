


---

 AlgoForge Contribution Guide

Welcome to Algoforge — a VS Code–powered DSA analyzer and recommender built in Python.
This guide ensures all team members follow a consistent structure so the whole system runs smoothly.


---

 Project Folder Structure

algoforge/
 ┣ 📄 main.py                 ← main backend controller
 ┣ 📁 modules/                ← all DSA modules here
 ┃ ┣ 📄 arrays.py
 ┃ ┣ 📄 linked_list.py
 ┃ ┣ 📄 stacks_queues.py
 ┃ ┣ 📄 hashing.py
 ┃ ┣ 📄 trees.py
 ┃ ┣ 📄 graphs.py
 ┃ ┣ 📄 sorting.py
 ┃ ┣ 📄 divide_conquer.py
 ┃ ┣ 📄 dynamic_programming.py
 ┃ ┗ 📄 greedy.py
 ┣ 📁 utils/
 ┃ ┣ 📄 benchmark.py
 ┃ ┗ 📄 parser.py
 ┗ 📄 CONTRIBUTION_GUIDE.md


---

 10 Coding Rules for Contributors

1️⃣ Follow the folder structure exactly

All modules must stay inside algoforge/modules/.

File names must match the topic (e.g., arrays.py, trees.py, etc.).

Do not rename or relocate files.



---

2️⃣ One file = one DSA domain

Each file represents a single concept:

File	Focus

arrays.py	Array-based ops
trees.py	Tree-based ops
graphs.py	Graph algorithms
dynamic_programming.py	DP problems
greedy.py	Greedy algorithms


Keep your logic isolated to that DSA only.


---

3️⃣ Mandatory standard functions

Each DSA file must include these functions (even if some just return “Not Supported”):

def insert(data): ...
def delete(value): ...
def search(value): ...
def range_query(start, end): ...

This ensures main.py can call every module in a uniform way.


---

4️⃣ Consistent input & output format

Accept simple inputs (ints, lists, strings).

Return structured data, not printed text.
✅ Example:


def search(value):
    start = time.time()
    # logic
    end = time.time()
    return {"operation": "search", "time": end - start, "result": True}


---

5️⃣ Avoid global variables

Keep variables local inside functions.
Only use minimal top-level data structures if necessary (like data_structure = []).


---

6️⃣ Add docstrings and comments

Each function must have a short docstring:

def insert(data):
    """Insert data into the array and return time taken"""

Add inline comments for clarity — helps both contributors debug.


---

7️⃣ Use only built-in Python modules

Allowed: time, math, heapq, collections, itertools, etc.
❌ Not allowed: external installs (like NumPy, pandas, networkx).


---

8️⃣ Handle exceptions gracefully

Your code should never crash.
Wrap risky parts in try/except:

try:
    ...
except Exception as e:
    return {"error": str(e)}


---

9️⃣ Use descriptive variable names

✅ Examples: data_list, search_key, time_taken
❌ Avoid: a, b, temp, unless for loops or indices.


---

🔟 Always return results (don’t print)

Every function must return its output (time, result, etc.).
main.py collects and compares performance metrics — printed output won’t be captured.


---

Rule (for debugging)

At the end of each file, add a quick test block:

example:
if __name__ == "__main__":
    print(insert([1, 2, 3]))
    print(search(2))

This lets you run the file directly before pushing changes.


---
 Collaboration Tips

Commit regularly with meaningful messages:

git add .
git commit -m "Added array insert and search benchmarks"

Push your branch after testing.

Keep your functions modular and independent.

Communicate changes clearly before modifying shared files.



---

> You can write your code however you want —
but follow these 10 rules so our system stays perfectly synchronized



