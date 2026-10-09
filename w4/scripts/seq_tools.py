seq = "AATTCTGTAGCTGGTACCTATATATGCCCGTA"
gc=(seq.count("G")+seq.count("C"))/len(seq)*100
print(str(len(seq)) + " <len  |  gc content> " +str(gc))

print(seq[0:3]+" "+seq[-3:])

# T-> a

print(seq.replace("A","t").replace("T","a").replace("C","g").replace("G","c"))


