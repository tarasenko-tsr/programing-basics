sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)
print(len(sequences),sequences[0],sequences[-1])



sequences.append("ATTA")





length=[]
i=0
while i != len(sequences):
    length.append(len(sequences[i]))
    i+=1
print(length)






max=max(length)
aver=sum(length)/len(length)
min=min(length)
print(max,aver,min)





name, chrom, start, stop=gene


print(f"{name} is on {chrom} and is {stop-start} bases long ")



#gene[0]="something"
# Traceback (most recent call last):
#   File "/home/tarasenko_tsr/Desktop/prog/w4/scripts/seq_stats.py", line 41, in <module>
#     gene[0]="something"
#     ~~~~^^^
# TypeError: 'tuple' object does not support item assignment




genes = [("BRCA1", 81188), ("TP53", 25759)]
print(genes[1][1])