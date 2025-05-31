#  Simple Arithmetic Verifier Using Z3

This small project uses the **Z3 SMT solver** to formally verify simple arithmetic properties like **commutativity, associativity, and distributivity**.

---

##  What Does This Project Do?

Uses Z3 to check that:
- \( a + b = b + a \) (commutativity)
- \( (a + b) + c = a + (b + c) \) (associativity)
- \( a \times (b + c) = a \times b + a \times c \) (distributivity)

 Demonstrates how to encode and verify **mathematical logic** using formal methods.

 Provides a foundation to expand to **algorithm correctness proofs** in the future.

---

##  Tech Stack

- **Python** — for scripting
- **Z3 SMT Solver** — to encode and check formulas

---

##  Installation

```bash
pip install z3-solver
