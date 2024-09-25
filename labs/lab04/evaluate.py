import argparse

def evaluate(fname: str) -> float: 

    count = 0
    types = set([])
    with open(fname, 'r') as f:
        for line in f:
            words = line.split(' ')
            count += len(words)
            types.update(set(words))
    return len(types)/count

    
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Evaluate a tokenizer')
    parser.add_argument('--token_fname', help='path to file with space seperated words')
    arguments = parser.parse_args()

    diversity = evaluate(arguments.token_fname)
    print(f'Lexical Diversity: {round(diversity, 5)}')

if __name__ == "__main__":
    main()
