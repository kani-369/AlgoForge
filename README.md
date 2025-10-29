
 AlgoLens

 A Smart DSA Analyzer and Recommender for Developers

**AlgoLens** is an AI-assisted **VS Code extension** built in **Python**, designed to help programmers and learners choose the *most efficient data structure or algorithm* for their use case.
It analyzes the given operations (like insertions, deletions, searches, and range queries) and automatically tests performance across multiple DSA modules — such as arrays, stacks, queues, trees, graphs, dynamic programming, and more.

---

## Key Features

 **Intelligent DSA Benchmarking:**
  Compares different data structures and algorithms based on speed and memory usage for your operations.

  **10 Core DSA Modules:**
  Includes Arrays, Linked Lists, Stacks & Queues, Hashing, Trees, Graphs, Sorting, Divide & Conquer, Dynamic Programming, and Greedy algorithms.

 **Natural Input Style:**
  Accepts human-like inputs such as:

  ```
  insert 100 elements
  search 200 elements
  delete 10 elements
  range query 5
  ```

  — and automatically interprets them.

 **Smart Recommendation Engine:**
  Suggests which data structure or algorithm performs best for your use case.

 **Built-in Benchmark System:**
  Uses execution time and memory analysis to give accurate performance comparisons.

---

##  Project Structure

```
algolens/
 ┣ 📄 main.py                 ← Main backend controller
 ┣ 📁 modules/                ← DSA modules (arrays, trees, etc.)
 ┣ 📁 utils/                  ← Benchmarking + text parser tools
 ┗ 📄 CONTRIBUTION_GUIDE.md   ← Developer coding standards
```

---

## Tech Stack

* **Language:** Python
* **Extension Target:** Visual Studio Code
* **Modules:** Custom-built DSA implementations
* **Utilities:** Benchmarking & Parser for performance metrics

---

## How It Works

1. User gives a natural prompt describing operations.
2. The parser extracts operations and parameters.
3. The system runs benchmarks across all DSA modules.
4. It returns a ranked recommendation based on speed and efficiency.

---

## Vision

> To make data structure learning and selection intuitive, measurable, and AI-powered —
> bridging the gap between *theory* and *practical implementation.*

---

## Future Scope

* Integration with AI copilots for real-time code insights.
* Visualization of benchmark results (graphs/charts).
* Support for more complex hybrid algorithms.
* Plugin publishing on the VS Code Marketplace.

---

## License

This project is open-source and available under the **MIT License**.

---


