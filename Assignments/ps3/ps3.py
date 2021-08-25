# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Aya farid abdalkarim>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import random
from random import seed
from random import randint

seed(1)
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


word_list = load_words()


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# print(get_frequency_dict('hello'))

def get_word_score(word, n):
    word = word.lower()
    sum_of_points = 0
    for i in word:
        if i == '*':
            continue
        sum_of_points += SCRABBLE_LETTER_VALUES[i]
    score = 0
    second_comp = 0
    p = ((7 * len(word)) - (3 * (n - len(word))))
    if p > 0:
        second_comp = p
    else:
        second_comp = 1
    score = sum_of_points * second_comp
    return score


# print(get_word_score("f*x",4)+90)

def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


# display_hand(get_frequency_dict('aqlmuil'))

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))  # هو هنا عايز يكون عدد الحروف المتحركه مش اقل من ثلث العدد الكلي بس بالتقريب
    x = 0
    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = hand.get('*', 0) + 1
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand


def update_hand(hand, word):
    word = word.lower()
    new_hand = hand.copy()  # ^_^
    new_hand1 = {}
    chek = 0
    chek1 = 0
    for letter in word:
        if new_hand.get(letter, 0) != 0:
            new_hand[letter] -= 1
        else:
            chek = 0
    for key in new_hand.keys():
        if new_hand[key] != 0:
            new_hand1[key] = new_hand[key]
    if chek == 0:
        hand = new_hand.copy()
    return new_hand1


hand = {'j': 2, 'o': 1, 'l': 1, 'w': 1, 'n': 2}
# display_hand(hand)
new_hand = update_hand(hand, 'jolly')


# print(new_hand)
# display_hand(new_hand)
# display_hand(hand)


def is_valid_word(word, hand, word_list):
    word = word.lower()
    chek = 0
    chek1 = 0
    chek2 = 0
    temp = word
    word = list(word)
    v = list(VOWELS)
    if '*' in word:
        as_position = word.index('*')
        for i in v:
            word[as_position] = i
            for i1 in word_list:
                i2 = list(i1)
                if i2 == word:
                    chek = 1
                    break
            if chek == 1:
                break
        for letter in temp:
            if hand.get(letter, 0) < temp.count(letter):
                chek2 = 1
                break
        if chek2 == 0 and (chek == 1 or chek1 == 1):
            return True
        else:
            return False
    else:
        word = ''.join(word)
        for word_in in word_list:
            if word_in == word:
                chek1 = 1
                break
        for letter in temp:
            if hand.get(letter, 0) < word.count(letter):
                chek2 = 1
                break
        if chek2 == 0 and chek1 == 1:
            return True
        else:
            return False


hand = {'c': 1, 'i': 1, '*': 1}
# print(is_valid_word('ic*',hand,word_list))
"""
hand= {'c': 1, 'o': 1, 'w': 1, 's': 1, '*': 1, 'z': 1}
word_list=load_words()
print(is_valid_word('cows',hand,word_list))
word_list=load_words()
#print(is_valid_word('quail',hand,word_list))
"""


def Wildcardsp5():
    word_list = load_words()
    total = 0
    score = 0
    inp = ''
    chek = 0
    hand = {'a': 1, 'j': 1, 'e': 1, 'f': 1, '*': 1, 'r': 1, 'x': 1}
    hand2 = hand.copy()
    while True:
        if len(hand2) == 0:
            print('Ran out of letters. Total score: ', total, 'points')
            break
        # n=randint(1,10)
        # hand=deal_hand(n)
        n = len(hand2)
        print('Current Hand: ', end=' ')
        display_hand(hand)
        inp = input('Enter word, or "!!" to indicate that you are finished: ')
        if inp == '!!':
            print('Total score: ', total, 'points')
            break
        count = 0
        as_po = 0
        chek1 = 0
        chek = 0
        temp = inp
        for i in inp:
            if i == '*':
                chek1 = 1
        if chek1 == 1:
            for i in inp:
                if i == '*':
                    for i1 in VOWELS:
                        inp = inp.replace(i, i1, 1)
                        for i2 in word_list:
                            if i2 == inp:
                                chek = 1
                                break
                        if chek == 1:
                            break
                    break
        if chek == 1 or is_valid_word(inp, hand, word_list) == True:
            score = get_word_score(temp, n)
            total += score
            print('\"', temp, '\" earned ', score, ' points. Total: ', total, 'points\n')
            for i in hand:
                for i1 in temp:
                    if i == i1:
                        hand[i] -= 1
            hand2 = {}
            for i in hand:
                if hand[i] == 0:
                    continue
                else:
                    hand2[i] = hand[i]
        else:
            for i in hand:
                for i1 in temp:
                    if i == i1:
                        hand[i] -= 1
            hand2 = {}
            for i in hand:
                if hand[i] == 0:
                    continue
                else:
                    hand2[i] = hand[i]
            print('That is not a valid word. Please choose another word.\n')


# Wildcards_p5()
def Wildcards():
    word_list = load_words()
    total = 0
    score = 0
    inp = ''
    chek = 0
    hand = {'c': 1, 'o': 1, 'w': 1, 's': 1, '*': 1, 'z': 1}
    while True:
        # n=randint(1,10)
        # hand=deal_hand(n)
        n = len(hand)
        print('Current Hand: ', end=' ')
        display_hand(hand)
        inp = input('Enter word, or "!!" to indicate that you are finished: ')
        if inp == '!!':
            print('Total score: ', total, 'points')
            break
        count = 0
        as_po = 0
        chek1 = 0
        chek = 0
        temp = inp
        for i in inp:
            if i == '*':
                chek1 = 1
        if chek1 == 1:
            for i in inp:
                if i == '*':
                    for i1 in VOWELS:
                        inp = inp.replace(i, i1, 1)
                        print(inp)
                        for i2 in word_list:
                            if i2 == inp:
                                chek = 1
                                break
                        if chek == 1:
                            break
                    break
        if chek == 1 or is_valid_word(inp, hand, word_list) == True:
            score = get_word_score(temp, n)
            total += score
            print('\"', temp, '\" earned ', score, ' points. Total: ', total, 'points\n')
            hand = {'o': 1, 'z': 1}
        else:
            print('That is not a valid word. Please choose another word.\n')


# Wildcards()
def calculate_handlen(hand):
    sum = 0
    for i in hand:
        sum += hand[i]
    return sum


hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}


# print(calculate_handlen(hand))

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.

    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is two exclamation points:

    # End the game (break out of the loop)

    # Otherwise (the input is not two exclamation points):

    # If the word is valid:

    # Tell the user how many points the word earned,
    # and the updated total score

    # Otherwise (the word is not valid):
    # Reject invalid word (print a message)

    # update the user's hand by removing the letters of their inputted word

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function
    total = 0
    score = 0
    inp = ''
    chek = 0
    hand2 = hand.copy()
    while True:
        if len(hand2) == 0:
            print('Ran out of letters.\nTotal score for this hand: ', total, 'points\n------------------')
            break
        # n=randint(1,10)
        # hand=deal_hand(n)
        n = len(hand2)
        print('Current Hand: ', end=' ')
        display_hand(hand)
        inp = input('Enter word, or "!!" to indicate that you are finished: ')
        if inp == '!!':
            print('Total score for this hand: ', total, 'points\n------------------')
            break
        temp = inp
        if is_valid_word(inp, hand, word_list) == True:
            score = get_word_score(temp, calculate_handlen(hand))
            total += score
            print('\"', temp, '\" earned ', score, ' points. Total: ', total, 'points\n')
            for i in hand:
                for i1 in temp:
                    if i == i1:
                        hand[i] -= 1
            hand2 = {}
            for i in hand:
                if hand[i] == 0:
                    continue
                else:
                    hand2[i] = hand[i]
        else:
            for i in hand:
                for i1 in temp:
                    if i == i1:
                        hand[i] -= 1
            hand2 = {}
            for i in hand:
                if hand[i] == 0:
                    continue
                else:
                    hand2[i] = hand[i]
            print('That is not a valid word. Please choose another word.\n')
    return total


# word_list = load_words()
# play_hand({'a':1,'c':1,'i':1,'*':1,'p':1,'r':1,'t':1},word_list)

#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.
    If user provide a letter not in the hand, the hand should be the same.
    Has no side effects: does not mutate hand.
    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    l = 'abcdefghijklmnopqrstuvwxyz'
    l = list(l)
    for i in hand:
        if i in l:
            l.remove(i)
    if hand.get(letter, 0) == 0:
        return hand
    else:
        n = hand[letter]
        hand['a'] = n
        del (hand[letter])
    return hand


# print(substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l'))


def play_game(word_list):
    """
    Allow the user to play a series of hands
    * Asks the user to input a total number of hands
    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.
    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.
            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands
    word_list: list of lowercase strings
    """
    total_hands = 0
    num_hands = int(input('Enter total number of hands: '))
    chek = 1
    hand_t = {}
    total = 0
    while num_hands > 0:
        # n = randint(1,10)
        # hand=deal_hand(n)
        if chek == 1:
            n = randint(1, 20)
            hand = deal_hand(n)
            hand_t = hand.copy()
            print('Current hand:', end=' ')
            display_hand(hand)
            chek1 = input('Would you like to substitute a letter? ')
            if chek1 == 'yes':
                letter = input('Which letter would you like to replace: ')
                substitute_hand(hand, letter)
                print()
            else:
                print()
                total = play_hand(hand_t, word_list)
                total_hands += total
            chek = 0
            num_hands -= 1
        elif chek == 0:
            inp = input('Would you like to replay the hand? ')
            if inp == 'yes':
                total = play_hand(hand_t, word_list)
                total_hands += total
            else:
                num_hands -= 1
                n = randint(1, 20)
                hand = deal_hand(n)
                hand_t = hand.copy()
                print('Current hand:', end=' ')
                display_hand(hand)
                print()
                chek1 = input('Would you like to substitute a letter? ')
                if chek1 == 'yes':
                    letter = input('Which letter would you like to replace: ')
                    substitute_hand(hand, letter)
                    hand_t = hand.copy()
                    print()
                    total = play_hand(hand_t, word_list)
                    total_hands += total
                else:
                    total = play_hand(hand_t, word_list)
                    total_hands += total
    return total_hands


play_game('Total score over all hands: ', word_list)


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
# if __name__ == '__main__':
# word_list = load_words()
# play_game(word_list)

def play_game(word_list):
    total_hands = 0
    num_hands = int(input('Enter total number of hands: '))
    chek = 1
    hand_t = {}
    total = 0
    while True:
        # n = randint(1,10)
        # hand=deal_hand(n)
        if chek == 1:
            n = 7
            hand = {'a': 1, 'c': 1, 'i': 1, '*': 1, 'p': 1, 'r': 1, 't': 1}
            hand_t = hand.copy()
            print('Current hand:', end=' ')
            display_hand(hand)
            chek1 = input('Would you like to substitute a letter? ')
            if chek1 == 'yes':
                letter = input('Which letter would you like to replace: ')
                substitute_hand(hand, letter)
                print()
            else:
                print()
                total = play_hand(hand_t, word_list)
                total_hands += total
            chek = 0
        elif chek == 0:
            inp = input('Would you like to replay the hand? ')
            if inp == 'yes':
                total = play_hand(hand_t, word_list)
                total_hands += total
            else:
                hand = {'d': 2, '*': 1, 'l': 1, 'o': 1, 'u': 1, 't': 1}
                hand_t = hand.copy()
                print('Current hand:', end=' ')
                display_hand(hand)
                print()
                chek1 = input('Would you like to substitute a letter? ')
                if chek1 == 'yes':
                    letter = input('Which letter would you like to replace: ')
                    substitute_hand(hand, letter)
                    hand_t = hand.copy()
                    print()
                    total = play_hand(hand_t, word_list)
                    total_hands += total
                else:
                    total = play_hand(hand_t, word_list)
                    total_hands += total
            chek = 2
        elif chek == 2:
            inp = input('Would you like to replay the hand? ')
            if inp == 'yes':
                total_hands -= total
                total_hands += play_hand(hand, word_list)
            else:
                hand = {'d': 2, '*': 1, 'l': 1, 'o': 1, 'u': 1, 't': 1}
                hand_t = hand.copy()
                print('Current hand:', end=' ')
                display_hand(hand)
                print()
                chek1 = input('Would you like to substitute a letter? ')
                if chek1 == 'yes':
                    letter = input('Which letter would you like to replace: ')
                    substitute_hand(hand, letter)
                    print()
                    total = play_hand(hand_t, word_list)
                    total_hands += total
                else:
                    total = play_hand(hand_t, word_list)
                    total_hands += total
            chek = 8
        else:
            print('Total score over all hands: ', total_hands)
            break
        num_hands -= 1
    return total_hands


play_game(word_list)