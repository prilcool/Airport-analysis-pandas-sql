### TUTORIALSPOINT ##

## Tuples @@ Enclosed in parenthe
   ## read only LiSTS -- CANT BE UPDATED

tuple = ('abcd', '12344', 'elephant')
tinytuple = ('abcdef', 'temp', 'ghost')

## Lists --- enclosed in brackets -- sizes can be changed

temp_list = ['abcd', '12344', 'elephant']

## Python Dictionaries
#  Like hash tables -- consist of key value pairs
#    Keys are usually numbers or string    ##

dict = {}
dict['one'] = "This is number one"

dict[2] = "This is two"

#Elements are unordered in dictionaries.. No concept of order among elements#

def combinations2(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield list(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

temp = list(combinations2('ABCD', 2))

for i in temp:
    print(temp)