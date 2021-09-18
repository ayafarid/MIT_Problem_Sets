# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random


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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
#wordlist = load_words()
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
#word_computer = choose_word(wordlist)
wordlist = load_words()

from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
def pset2p1():
    chek2=1
    while chek2==1:
        word_computer = choose_word(wordlist)
        values = int(input("Enter any number of guesses : "))
        print('Your number of guesses is equal ',values)
        chek=0
        chek1=0
        print(word_computer)
        print(len(word_computer))
        for i in range(values) :
            print('guess number ',values)
            word_guess = input('Enter the word you guess : ')
            if word_computer == word_guess :
                chek=1
                print('Rigth guess ^_^')
                print(list(word_guess))
                print('Congratulations \nDo you want to play again ? (yes or no)')
                chek9 = input()
                if chek9 == 'yes':
                    chek2=1
                else:
                    chek2=0
                break
            elif values>1 :
                s=""
                chek0=0
                for i1 in word_computer :
                    for i2 in word_guess :
                        if i1==i2 :
                            s+=i1
                            chek0=1
                            break
                    if chek0==0:
                        s+='_ '
                    chek0=0
                print(s)
                if values==1 :
                    print('Game over \nDo you want to play again ? (yes or no)')
                    chek9 = input()
                    if chek9 == 'yes':
                        chek2=1
                    else:
                        chek2=0
                    break
                values-=1
def pset2p21a(word_computer,word_guess):
    c=0
    for i1 in word_computer:
        for i2 in word_guess:
            if i1==i2:
                c+=1
                break
    if c==len(word_computer):
        return True
    else:
        return False
word_computer = choose_word(wordlist)
print('secret_word = ',word_computer)
word_guess = input('Enter the word you guess : ')
print('letters_guessed = ',list(word_guess))
print(pset2p21a(word_computer,word_guess))
def pset2p21b(word_computer,word_guess):
    s=""
    chek0=0
    for i1 in word_computer :
        for i2 in word_guess :
            if i1==i2 :
                s+=i1
                chek0=1
                break
        if chek0==0:
            s+='_ '
        chek0=0
    print(s)
word_computer = choose_word(wordlist)
print('secret_word = ',word_computer)
word_guess = input('Enter the word you guess : ')
print('letters_guessed = ',list(word_guess))
pset2p21b(word_computer,word_guess)


def pset2p21c(word_guess):
    s="abcdefghijklmnopqrstuvwxyz"
    t=""
    chek=0
    for i1 in s:
        for i2 in word_guess:
            if i1==i2:
                chek=1
                break
        if chek==0:
            t+=i1
        chek=0
    return t

word_guess = input('Enter the word you guess : ')
print('letters_guessed = ',list(word_guess))
print(pset2p21c(word_guess))

def pset2p3A():
    print("Welcome to the game Hangman!")
    word_computer = choose_word(wordlist)
    print("I am thinking of a word that is ",len(word_computer)," letters long.")
    print("-------------")
    print("You have 6 guesses left.")
    t="abcdefghijklmnopqrstuvwxyz"
    print("Available letters: ",t)

def pset2p3B():
    word_computer = choose_word(wordlist)
    ll=""
    s=""
    chek0=0
    chek=0
    print(word_computer)
    t="abcdefghijklmnopqrstuvwxyz"
    for j in range(1,7):
        print("You have",7-j,"guesses left.")
        t=list(t)
        print("Available letters:",''.join(t))
        guess_letter=input('Please guess a letter: ')
        t.remove(guess_letter)
        ll+=guess_letter
        for i1 in word_computer :
            for i2 in ll :
                if i1==i2:
                    s+=i1
                    chek0=1
                    break
            if chek0==0:
                s+='_ '
            chek0=0
        for i1 in word_computer :
            if i1==guess_letter:
                chek=1
                break
        if chek==1:
            print("Good guess: ",s)
        else:
            print('Oops! That letter is not in my word: ',s)
        chek=0
        if s==word_computer:
            print('good game^_^')
            break
        s=""

#pset2p3B()
def match_with_gaps(guess_word,instance_word):
    s=""
    for i1 in guess_word:
        if i1==' ':
            continue
        else:
            s+=i1
    if len(s)==len(instance_word):
        for i in range(len(s)):
            if s[i]=='_':
                continue
            elif s[i]!=instance_word[i]:
                return False
    else:
        return False
    return True
def show_possible_matches(guess_word):
    s=""
    c=0
    for i1 in guess_word:
        if i1==' ':
            continue
        else:
            s+=i1
    for word in wordlist:
        if match_with_gaps(s,word)==True:
            c+=1
            print(word,end=' ') #trick
    if c==0:
        print('No matches found')
word_computer = 'apple'#choose_word(wordlist)
print(word_computer)
print("Welcome to the game Hangman!")
print("I am thinking of a word that is ",len(word_computer)," letters long.")
print('You have 3 warnings left.')
print('-----------')
def pset2p3B3C3D3E():
    c=0
    ll=""
    s=""
    chek0=0
    chek=0
    num_war=2
    i=6
    t="abcdefghijklmnopqrstuvwxyz"
    while(i>0):
        print("You have",i,"guesses left.")
        t=list(t)
        print("Available letters:",''.join(t))
        guess_letter=input('Please guess a letter: ')
        if guess_letter=='*':
            print('Possible word matches are:')
            show_possible_matches(s)
            print('\n-----------')
            continue
        chek=0
        if guess_letter.isalpha()==False and num_war>=0:
            print('Oops! That is not a valid letter.','You have ',num_war,' warnings left: ',s)
            num_war-=1
            print('-----------')
            continue
        elif guess_letter.isalpha()==False and num_war<0:
            print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ',s)
            print('-----------')
            i-=1
            continue
        else:
            for i1 in ll:
                if i1==guess_letter:
                    chek=1
                    if num_war>=0:
                        print('Oops! You\'ve already guessed that letter.','You have ',num_war,' warnings left: ',s)
                        num_war-=1
                        print('-----------')
                    else:
                        print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ',s)
                        print('-----------')
                        i-=1
                    break
            if chek==1:
                continue
        t=list(t)
        t.remove(guess_letter)
        ll+=guess_letter
        s=""
        for i1 in word_computer :
            for i2 in ll :
                if i1==i2:
                    s+=i1
                    chek0=1
                    break
            if chek0==0:
                s+='_ '
            chek0=0
        for i1 in word_computer :
            if i1==guess_letter:
                chek=1
                break
        if chek==1:
            print("Good guess: ",s)
            print('-----------')
            c+=1
        else:
            print('Oops! That letter is not in my word: ',s)
            print('-----------')
            i-=1
        chek=0
        if s==word_computer:
            print('good game^_^\nCongratulations, you won!\nYour total score for this game is: ',i*c)
            break
    if i==0 and word_computer!=s:
        print('Sorry, you ran out of guesses. The word was ',word_computer,'.')
pset2p3B3C3D3E()
#print(match_with_gaps("te_ t","tact"))
#show_possible_matches("a_ pl_")
# -----------------------------------