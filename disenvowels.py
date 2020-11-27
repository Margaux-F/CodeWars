def disenvowels(string):
    return ''.join((string.split).remove(x for x in 'aeiouy'))

print(disenvowels('ererfksdjjnsgnksgzaaaaa'))