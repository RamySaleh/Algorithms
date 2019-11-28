from Helpers import profiler as prof


class node:
    def __init__(self, letter, isEnd=False):
        self.letter = letter
        self.isEnd = isEnd
        self.children = {}

    def add_child(self, letter, isEnd=False):
        self.children[letter] = node(letter, isEnd)


tree = node('')


def insert(word):
    curr_node = tree
    idx = 0
    for letter in word:
        idx += 1
        # if letter not found
        if letter not in curr_node.children:
            # add the letter node
            curr_node.add_child(letter, len(word) == idx)

        # go down into the correct letter node
        curr_node = curr_node.children[letter]


def complete(word):
    matching_pref = ''
    curr_node = tree
    found = False

    for letter in word:
        # if letter node is found
        if letter in curr_node.children:
            curr_node = curr_node.children[letter]
            matching_pref += letter
            found = True
    if found:
        # print all words (branches( under this node
        matching_words(curr_node, matching_pref)


def matching_words(ptree, matching_pref):
    for letter in ptree.children:
        matching_words(ptree.children[letter], matching_pref + letter)

    # if end of a word
    if ptree.isEnd:
        print(matching_pref)


def read_file(path):
    f = open(path, 'r')
    x = f.readlines()
    f.close()
    return x


all_words = read_file('resources/all_words.txt')

for word in all_words : insert(word.replace("\n", ""))

def run(parms):
    #words = parms[0]
    #for word in words : insert(word)
    complete('ne')

prof.profile(run, all_words)
prof.size_of(tree)
