#  Sudoku Solution Verifier Using Z3

This project uses the **Z3 SMT Solver** to **formally verify** that a given Sudoku puzzle solution is valid. It checks that each row, column, and 3×3 subgrid contains all digits 1–9 exactly once.

---

##  What Does This Project Do?

Takes a 9×9 Sudoku solution as input  
 Verifies:
- Each **row** contains digits 1–9 exactly once
- Each **column** contains digits 1–9 exactly once
- Each **3×3 subgrid** contains digits 1–9 exactly once  
 Uses **Z3** to model and solve these constraints  
 Prints whether the solution is **valid** or **invalid**

---

##  Tech Stack

- **Python** — scripting language
- **Z3 SMT Solver** — constraint solver for verification

---

##  Installation

Make sure you have Python and pip installed. Then:

```bash
pip install z3-solver
