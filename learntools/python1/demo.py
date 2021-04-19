from learntools.core import *



class Q1(EqualityCheckProblem):
    _vars = ['a', 'b', 'c']
    _expected = [2, 4, 8]
    _hint = "This is an optional hint. If you can solve the exercise without a hint, you don't have to use it. " \
            "However, if you are stuck with an exercise, you might find helpful tips by calling the hint."
    _solution = CS("""a = 2
b = 4
c = a * b
""")


qvars = bind_exercises(globals(), [
    Q1,
])
__all__ = list(qvars)
