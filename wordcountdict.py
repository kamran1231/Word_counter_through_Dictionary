
#Word counter Dictionry:

def word_counter(s):
    count = []
    for i in s:
        count[i] = s.count(i)
    return count

print(word_counter('kamran khan is the best'))