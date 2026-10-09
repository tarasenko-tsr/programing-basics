sequence = "TGACGTTCGCATGCATCGATA"
print(len(sequence))
g=sequence.count("G")
c=sequence.count("C")
gc=(g+c)/len(sequence)*100
print("GC:", gc, "%")


a=input("another seq:")
print("rounded: ",round(gc,2))
print(a)

