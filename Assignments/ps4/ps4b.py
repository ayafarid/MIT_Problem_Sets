# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import copy
import string


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


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
word_list = load_words(WORDLIST_FILENAME)


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        for word in word_list:
            is_word(word_list, word)
        self.valid_words = word_list

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return copy.deepcopy(self.message_text)

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return copy.deepcopy(self.valid_words)

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        dic = {}
        al = list(string.ascii_lowercase)
        au = list(string.ascii_uppercase)
        for i in al:
            if al.index(i) + shift >= 26:
                dic[i] = al[(al.index(i) + shift) - 26]
            else:
                dic[i] = al[al.index(i) + shift]
        for i in au:
            if au.index(i) + shift >= 26:
                dic[i] = au[(au.index(i) + shift) - 26]
            else:
                dic[i] = au[au.index(i) + shift]

        '''
        st='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        st=list(st)
        for i in range(0,52):
            dic[st[i]]=ord(st[i])
        for i in dic:
            if dic[i]+shift>90 and ord(i)<=90 and ord(i)>=65:
                dic_shift[i]=chr(64+((dic[i]+shift)-90))
            elif dic[i]+shift>122 and ord(i)<=122 and ord(i)>=97:
                dic_shift[i] = chr(96 + ((dic[i] + shift) - 122))
            else:
                dic_shift[i]=chr(dic[i]+shift)
        '''
        return copy.deepcopy(dic)

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        EM = ""
        dicshift = self.build_shift_dict(shift)
        for i in self.get_message_text():
            if i.isalpha():
                EM += dicshift[i]
            else:
                EM += i
        return copy.deepcopy(EM)


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return copy.deepcopy(self.shift)

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return copy.deepcopy(self.encryption_dict)

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return copy.deepcopy(self.message_text_encrypted)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        self.shift = shift[:]
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.
        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        l = ()
        tt = ""
        count = 0
        lll = self.message_text
        lll = lll.split(' ')
        ss = ""
        max_=0
        if len(lll)>1:
            for i in range(1, 26):
                dic = self.build_shift_dict(i)
                tt = ""
                ss = ""
                count_t = 0
                sss = ''
                countt = 0
                for i1 in self.message_text:
                    if i1 == ' ':
                        countt += 1
                        for i4 in ss:
                            if i4.isalpha():
                                sss += i4
                        sss.lower()
                        # print('\'',sss, '\'')
                        if sss in word_list:
                            count_t += 1
                        ss = ""
                        sss = ''
                    if i1.isalpha():
                        ss += dic[i1]
                        tt += dic[i1]
                    else:
                        ss += i1
                        tt += i1
                # print(i,' ',tt,' ',count_t)
                if max_ <= count_t:
                    max_ = count_t
                    # print(countt, max_)
                    max_i = i
                    # print(max_i,' ',i)
                    sstt = tt
                    # print(sstt,' ',tt)
            l = (max_i, sstt)
            # print(max_i,' ',sstt)
            return l
        else:
            for i in range(1, 26):
                dic = self.build_shift_dict(i)
                tt = ""
                for i1 in self.message_text:
                    tt += dic[i1]
                if tt in word_list:
                    l = (i, tt)
            return l


if __name__ == '__main__':
    '''
    M1 = Message("")
    print(M1.get_message_text())
    CvaildWords=M1.get_valid_words()
    print(M1.apply_shift(4))
    '''
    #    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    #    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage(get_story_string())
    print('Actual Output:', ciphertext.decrypt_message())
