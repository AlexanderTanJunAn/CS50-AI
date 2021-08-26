from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

basicKnowledge = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    basicKnowledge,
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    basicKnowledge,

    #If A is telling the truth
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    basicKnowledge,

    #If A is telling the truth, assuming A is knight
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    #If B is telling the truth, assuming B is knight
    Biconditional(BKnight, Or(And(BKnave, AKnight), And(BKnight, AKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    basicKnowledge,

    #A is a knight iff (AKnight V AKnave) is true
    Biconditional(AKnight, Or(AKnight, AKnave)),
    #B is a knight iff A is telling the truth. A is telling the truth iff its a knave
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    #If B & C is knight
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
