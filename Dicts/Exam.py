#The teacher gave Petya homework - to place stresses in words in the given text, after which she instructed Vasya to check this homework. Vasya is very new to this topic, so he found a dictionary that indicates how words are stressed. Unfortunately, not all words are present in this dictionary. Vasya decided that in words that are not in the dictionary, he will consider that Petya put the stresses correctly if Petya put exactly one stress in this word.

#It turned out that some words can be stressed in more than one way. Vasya decided that in this case, if the way Petya put the stress corresponds to one of the options given in the dictionary, he will count it as the correct placement of the stress, and if it does not match, then as a mistake.

#You are given a dictionary that Vasya used and a homework submitted by Petya. Your task is to determine the number of mistakes that Vasya counts in this task.

#The number N is entered first — the number of words in the dictionary.

#Next comes N lines with words from the dictionary. Each word consists of no more than 30 characters. All words consist of small and capital Latin letters. In each word, there is exactly one capital letter - the one on which the stress falls. The words in the dictionary are in alphabetical order. If there are several possibilities for placing stress in the same word, then these options in the dictionary go in random order.

#Next comes the exercise performed by Petya. The exercise is a line of text with a total volume of no more than 300,000 characters. A string consists of words separated by exactly one space. The length of each word does not exceed 30 characters. All words consist of small and capital Latin letters (capitalized are those letters over which Petya put stress). Petya could mistakenly put more than one stress in a word or not put stress at all.
#Print the number of errors in Petya's text that Vasya will find.

#Notes on Test Examples

#1. In the word cannot, according to the dictionary, there are two options for placing stress. These options in the dictionary can be listed in any order (i.e. first cAnnot, and then cannOt, and vice versa). Two mistakes made by Petya are the words be (the emphasis is not placed at all) and fouNd (the emphasis is incorrect). The word thE is not in the dictionary, but since Petya put exactly one stress in it, it is recognized as correct.

#2. Incorrectly placed stresses in all words, except for The (it is not in the dictionary, it has exactly one stress). In other words, either all letters are stressed (in the word PAGE), or not a single stress is put.

n = int(input())
accents = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in accents:
        accents[base_form] = set()
    accents[base_form].add(word)
 
errors = 0
sent = input().split()
for word in sent:
    base_form = word.lower()
    if (base_form in accents and word not in accents[base_form]
            or len([l for l in word if l.isupper()]) != 1):
        errors += 1
print(errors)
