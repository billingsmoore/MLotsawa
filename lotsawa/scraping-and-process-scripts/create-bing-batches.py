entries = []
line_count = 0
batch_count = 0

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/eng.txt', 'r') as f:
    for line in f:
        entries.append(line)
        line_count += 1
        if batch_count == 119:
            if line_count >= 342:
                batch_path = 'lotsawa/data/ankhi/bing-batches/batch' + str(batch_count) + '.txt'
                with open(batch_path, 'w') as g:
                    g.write(''.join(entries))
        if line_count >= 1000:
            batch_path = 'lotsawa/data/ankhi/bing-batches/batch' + str(batch_count) + '.txt'
            with open(batch_path, 'w') as g:
                g.write(''.join(entries))
            entries = []
            line_count = 0
            batch_count += 1