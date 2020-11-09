l=open("scrabble.txt").readlines();p=[x.lower().rstrip() for x in l];w=input("Enter the word you want to unscramble:\n").lower()
for y in list(set([len(x) for x in sorted([x for x in p if (x in w)or(sorted(x)==sorted(w))],key=len)]))[2:]:
    print(f"\nThe word/s of length {y} formed by '{w}' are:")
    for x in sorted([x for x in p if (x in w)or(sorted(x)==sorted(w))],key=len):
        if len(x)==y:print(x,end="\n")
