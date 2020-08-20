l=open("scrabble.txt").readlines()
p=[x.lower().rstrip() for x in l]
w=input("Enter the word you want to unscramble:\n").lower()
a=sorted([x for x in p if (x in w)or(sorted(x)==sorted(w))],key=len)
q=list(set([len(x) for x in a]))[1:]
for y in q:
    print(f"\nThe word/s of length {y} formed by '{w}' are:")
    for x in a:
        if len(x)==y:
            print(x,end="\n")
