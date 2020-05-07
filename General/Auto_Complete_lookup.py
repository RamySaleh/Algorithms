from time import process_time
import sys

lookup = {}

def insert(word):

    prefix = ''
    for letter in word:
        prefix += letter
        if prefix not in lookup:
            lookup[prefix] = [word]
        else:
            lookup[prefix].append(word)


def complete(prefix):
    for word in lookup[prefix]:
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

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'bytes'

lookup_size = format_bytes(sys.getsizeof(lookup))
print("lookup size = " + str(lookup_size))