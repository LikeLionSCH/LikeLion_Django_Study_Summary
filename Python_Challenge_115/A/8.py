'''
Statement
One day, going through old books in the attic, a student Bob found an English-Latin dictionary. By that time he spoke English fluently, and his dream was to learn Latin. So finding the dictionary was just in time.

Unfortunately, full-fledged language studying process requires also another type of dictionary: Latin-English. For lack of a better way he decided to make a second dictionary using the first one.

As you know, the dictionary consists of words, each of which contains multiple translations. For each Latin word that appears anywhere in the dictionary, Bob has to find all its translations (that is, all English words, for which our Latin word is among its translations), and take them and only them as the translations of this Latin word.

Help him to create a Latin-English.

The first line contains a single integer N — the number of English words in the dictionary - followed by N dictionary entries. Each entry is contained on a separate line, which contains first the English word, then a hyphen surrounded by spaces and then comma-separated list with the translations of this English word in Latin. All the words consist only of lowercase English letters. The translations are sorted in lexicographical order. The order of English words in the dictionary is also lexicographic.

Print the corresponding Latin-English dictionary in the same format. In particular, the first word line should be the lexicographically minimal translation of the Latin word, then second in that order, etc. The English words inside each line should also be sorted lexicographically.

Example input
3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa

Example output
7
baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit
'''
from collections import defaultdict

latin_to_english = defaultdict(list)

for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')

    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)

print(len(latin_to_english))

for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))
