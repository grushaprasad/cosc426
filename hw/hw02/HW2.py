def split_data(fpath):
    """
    Splits data into train, validation and test split
    """
    with open(fpath, 'r') as f:
        dat = f.readlines()

    dat = dat[1:]
    random.shuffle(dat)

    ind1 = int(len(dat)*0.8)
    ind2 = int(len(dat)*0.9)
    train = dat[:ind1] #first line is column
    val = dat[ind1 : ind2]
    test = dat[ind2 : ]

    prefix = fpath[:-4]
    write_file(f'{prefix}_train.txt', train)
    write_file(f'{prefix}_val.txt', val)
    write_file(f'{prefix}_test.txt', test)