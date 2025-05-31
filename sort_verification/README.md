---

##  Algorithm Verification

This project also includes a **sorting correctness verifier** using Z3 SMT Solver. It demonstrates how to verify that:

 The sorted output is a permutation of the input.  
 The output is ordered non-decreasingly.

Run the verifier:
```bash
python verify_sort.py
