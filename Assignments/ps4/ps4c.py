# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    is_word(word_list, 'bat') returns
    True
    is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

l = []
def get_permutations(sequence, answer=""):
    '''
    Enumerate all permutations of a given string
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.
    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.
    Returns: a list of all permutations of sequence
    Example:
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if (len(sequence) == 0):
        l.append(answer)
        return
    for i in range(len(sequence)):
        ch = sequence[i]
        left_substr = sequence[0:i]
        right_substr = sequence[i + 1:]
        rest = left_substr + right_substr
        get_permutations(rest, answer + ch)
    return l

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
world_list=load_words(WORDLIST_FILENAME)
# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=world_list
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict={}
        leng=len(vowels_permutation)
        for i in range(0,leng):
            transpose_dict[vowels_permutation[i].lower()] = VOWELS_LOWER[i]
            transpose_dict[VOWELS_LOWER[i]]=vowels_permutation[i].lower()
            transpose_dict[vowels_permutation[i].upper()] = VOWELS_UPPER[i]
            transpose_dict[VOWELS_UPPER[i]]=vowels_permutation[i].upper()
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        s=''
        for i in self.get_message_text():
            if i in VOWELS_UPPER or i in VOWELS_LOWER:
                s+=transpose_dict[i]
            else:
                s+=i
        return s
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self,text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        max_s=''
        s=''
        max_=0
        l = (self.message_text).split(' ')
        if len(l)>1:
            for i in get_permutations(VOWELS_LOWER):
                dic = self.build_transpose_dict(i)
                s = ''
                t = ''
                tt = ''
                count = 0
                for i1 in self.message_text:
                    if i1 == ' ':
                        tt = ''
                        for i2 in t:
                            if i2.isalpha():
                                tt += i2.lower()
                        if tt in world_list:
                            count += 1
                        tt = ''
                    if i1 in VOWELS_LOWER or i1 in VOWELS_UPPER:
                        s += dic[i1]
                        t += dic[i1]
                    else:
                        s += i1
                        t += i1
                if count > max_:
                    max_ = count
                    max_s = s
        else:
            for i in get_permutations(VOWELS_LOWER):
                s=''
                dic = self.build_transpose_dict(i)
                for i1 in self.message_text:
                    if i1 in dic:
                        s+=dic[i1]
                    else:
                        s+=i1
                s=s.lower()
                if s in world_list:
                    max_s=s
                    break
        return max_s


    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    enc_message = EncryptedSubMessage("Hallu")
    print("Decrypted message:", enc_message.decrypt_message())
