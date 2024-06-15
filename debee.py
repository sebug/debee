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

def debee(letter_string, center_letter):
    letters = sorted_unique_list(letter_string)
    sublists = possible_sublists(letters)
    stringset = string_set([l for l in sublists if len(l) > 0])
    result = []
    with open('words.txt') as file:
        for line in file:
            word = line.rstrip().lower()
            if len(word) > 3:
                key = ''.join(sorted_unique_list(word))
                if key in stringset and center_letter in word:
                    result.append(word)
    result = sorted(result, key=lambda w: len(w))
    for word in result:
        print(word)
    print(len(result))

def main():
    parser = argparse.ArgumentParser(description="DeBee",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("letters", help="The letters to find words for")
    parser.add_argument("center_letter", help="The center letter that has to be in the word")
    args = parser.parse_args()
    config = vars(args)
    debee(config['letters'], config['center_letter'])

if __name__ == '__main__':
    main()
