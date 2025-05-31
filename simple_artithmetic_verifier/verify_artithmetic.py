from z3 import *

def verify_commutativity():
    a, b = Ints('a b')
    s = Solver()
    s.add(a + b != b + a)
    if s.check() == unsat:
        print("✅ Commutativity holds universally.")
    else:
        print("❌ Counterexample found:", s.model())

def verify_associativity():
    a, b, c = Ints('a b c')
    s = Solver()
    s.add((a + b) + c != a + (b + c))
    if s.check() == unsat:
        print("✅ Associativity holds universally.")
    else:
        print("❌ Counterexample found:", s.model())

def verify_distributivity():
    a, b, c = Ints('a b c')
    s = Solver()
    s.add(a * (b + c) != a * b + a * c)
    if s.check() == unsat:
        print("✅ Distributivity holds universally.")
    else:
        print("❌ Counterexample found:", s.model())

if __name__ == "__main__":
    verify_commutativity()
    verify_associativity()
    verify_distributivity()
