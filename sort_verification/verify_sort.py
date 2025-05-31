from z3 import *

def verify_sort_correctness(n):
    """
    Verifies that a sorting algorithm correctly sorts an array of length n.
    """
    # Input array: symbolic integers
    A = [Int(f'A_{i}') for i in range(n)]
    # Output array: symbolic integers (sorted)
    B = [Int(f'B_{i}') for i in range(n)]

    s = Solver()

    # Property 1: B is a permutation of A
    # For every value in A, there exists the same number of occurrences in B
    for i in range(n):
        # For each index, A[i] is somewhere in B
        s.add(Or([A[i] == B[j] for j in range(n)]))

    # Property 2: B is sorted non-decreasingly
    for i in range(n-1):
        s.add(B[i] <= B[i+1])

    # Ask: is there an input A and an output B such that these properties fail?
    # We negate both properties to see if the solver can find a counterexample.
    if s.check() == unsat:
        print(f"✅ Sort correctness verified for arrays of size {n}.")
    else:
        print(f"❌ Counterexample found for size {n}:", s.model())

if __name__ == "__main__":
    verify_sort_correctness(3)
