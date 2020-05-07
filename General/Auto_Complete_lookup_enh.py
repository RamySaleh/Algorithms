from Helpers import profiler as prof

lookup = {}

def insert(word, idx):
    prefix = ''
    for letter in word:
        prefix += letter
        if prefix not in lookup:
            lookup[prefix] = [idx]
        else:
            lookup[prefix].append(idx)

def complete(prefix, words):
    for idx in lookup[prefix]:
        print(words[idx])

def complete2(prefix, words):
    for word in words:
        if str.startswith(word, prefix):
            print(word)

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


all_words = read_file('../resources/all_words.txt')

small_words = ['nest', 'nested' , 'need']

def fill_lookup(parms):
    words = parms[0]
    for idx in range(len(words)): insert(words[idx], idx)

def run_complete(parms):


    #insert('leg')
    #insert('nag')
    complete(parms[0], parms[1])
    #complete('ne', words)
    #prof.size_of(words)

print('creation')
prof.profile(fill_lookup, all_words)

print('runtime')
prof.profile(run_complete, 'ne', all_words)
print(len(all_words))
prof.size_of(lookup)


