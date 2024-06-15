import argparse

# Get the power set of list
def possible_sublists(list):
    if len(list) == 0:
        return [[]]
    else:
        result = []
        first_element = list[0]
        rest = list[1:]
        sublists = possible_sublists(rest)
        for sublist in sublists:
            with_element = sublist.copy()
            with_element.append(first_element)
            without_element = sublist.copy()
            result.append(without_element)
            result.append(with_element)
        return sorted([sorted(l) for l in result], key = lambda l: -len(l))
    
def string_set(sublists):
    return set([''.join(l) for l in sublists])
    
def sorted_unique_list(letter_string):
    letters = list(letter_string)
    letters = set(letters)
    letters = sorted(list(letters))
    return letters

def debee(letter_string):
    letters = sorted_unique_list(letter_string)
    sublists = possible_sublists(letters)
    stringset = string_set([l for l in sublists if len(l) > 0])
    print(stringset)

def main():
    parser = argparse.ArgumentParser(description="DeBee",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("letters", help="The letters to find words for")
    args = parser.parse_args()
    config = vars(args)
    debee(config['letters'])

if __name__ == '__main__':
    main()
