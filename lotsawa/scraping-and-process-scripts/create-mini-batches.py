def process(num):
    entries = []
    line_count = 0
    batch_count = 0
    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/bing-batches/batch'+str(num)+'.txt', 'r') as f:
        for line in f:
            entries.append(line)
            line_count += 1
            if line_count >= 100:
                batch_path = '/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/bing-batches/mini-batches/'+str(num)+'/' + str(batch_count) + '.txt'
                with open(batch_path, 'w') as g:
                    g.write(''.join(entries))
                entries = []
                line_count = 0
                batch_count += 1

for i in range(109,119):
    process(i)