def process():
    entries = []
    line_count = 0
    batch_count = 0
    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/all-pairs.txt', 'r') as f:
        for line in f:
            line_count += 1
            batch_count = line_count // 500000
            batch_path = '/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/training-batches/training-batch-' + str(batch_count) + '.txt'
            with open(batch_path, 'a') as g:
                g.write(line)
                

process()