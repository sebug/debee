import argparse

def debee(letters):
    print(letters)

def main():
    parser = argparse.ArgumentParser(description="DeBee",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("letters", help="The letters to find words for")
    args = parser.parse_args()
    config = vars(args)
    debee(config['letters'])

if __name__ == '__main__':
    main()
