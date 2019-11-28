from time import process_time

tree = {}

def insert(word):
    curr_node = tree
    for letter in word:
        if letter not in curr_node:
            curr_node[letter] = {}

        curr_node = curr_node[letter]

def complete(word):
    matching_pref = ''
    curr_node = tree
    found = False
    for letter in word:
        if letter in curr_node:
            curr_node = curr_node[letter]
            matching_pref += letter
            found = True
    if found:
        matching_words(curr_node, matching_pref)


def matching_words(ptree, matching_pref):
    for node in ptree:
        matching_words(ptree[node], matching_pref + node)
    if len(ptree) == 0:
        print(matching_pref)

def read_file(path):
    f = open(path, 'r')
    x = f.readlines()
    f.close()
    return x

all_words = read_file('resources/all_words.txt')

t1_start = process_time()

for word in all_words : insert(word)

#insert('nest')
#insert('nested')
#insert('leg')
#insert('nag')
#insert('need')

complete('need')

t1_stop = process_time()

elapsed_time = round((t1_stop - t1_start),2)
print("time : " + str(elapsed_time) + " s")