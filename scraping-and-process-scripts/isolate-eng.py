eng = []
with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/spa.txt', 'r') as file:
    for line in file:
        l=line.split('\t')
        if l[0] not in eng:
            eng.append(l[0])

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/eng.txt', 'w') as f:
    f.writelines('\n'.join(eng))