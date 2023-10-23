with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/all-ankhi-pairs.txt', 'r') as f:
    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/all-pairs.txt', 'a') as g:
        for line in f:
            g.write(line)