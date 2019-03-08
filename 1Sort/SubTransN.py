""" 
No work is done for this! Just storage for right now
    - # utterances
    - avg # words per each utterance 
    - # words in transcript
    - # unique words *(can leave skeleton initially, maybs thing for task 2? or task 2 = optimized)*
    - # different tokens
    - # different word types
"""
class SubTransN(ID):
        
    def __init__(self, subjectID):
        self._ID = subjectID # Is this needed?
        self.utter = None
        self.utteravg = None

        self.wordcount = None
        self.wordcountunique = None
        
        self.tokens = None
        self.types = None

    # I think everything will be a number?
    def getutterances(self):
        return self.utter
    def setutterances(self, utterances, wordscount):
        pass

    # Not sure if I want this as a calculation or not, considering this is just storage...
    # I could calculate it in a process file? but hmm
    def getutteranceaverage(self):
        pass
    def setutteranceaverage(self, utterances):
        pass

    def getwordcount(self):
        return self.wordcount
    def setwordcount(self, wordcount):
        self.wordcount = wordcount
    def getwordunique(self):
        return self.wordcountunique
    def setwordsunique(self, uniquewords):
        self.wordcountunique = uniquewords

    def gettokenscount(self):
        return self.tokens
    def settokenscount(self, tokens):
        self.tokens = tokens

    def gettypecount(self):
        return self.types
    def settypecount(self, typecount):
        self.types = typecount

