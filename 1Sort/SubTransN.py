""" 
No work is done for this! Just storage for right now
"""
class SubTransN:
    
    # Everything will be a number
    def __init__(self, subjectID):
        self._ID = subjectID # Is this needed?
        self.utter = 0
        
        self.tokens = 0
        self.tokensavg = 0
        
        self.types = 0
        self.typesavg = 0
    
    
    # TYPE:
    # 0 = utterance
    # 1 = tokens
    # 11 = tokens avg/utterance
    # 2 = types
    # 22 = types avg/utterance
    def getter(self, type):
        return self.utter
    def setutterances(self, utterances, wordscount):
        pass

    # Not sure if I want this as a calculation or not, considering this is just storage...
    # I could calculate it in a process file? but hmm
    def getutteranceaverage(self):
        pass
    def setutteranceaverage(self, utterances):
        pass

    def gettokenscount(self):
        return self.tokens
    def settokenscount(self, tokens):
        self.tokens = tokens
    
    def gettokenanceaverage(self):
        pass
    def settokenaverage(self, utterances):
        pass

    def gettypecount(self):
        return self.types
    def settypecount(self, typecount):
        self.types = typecount
    
    def gettypeanceaverage(self):
        pass
    def settypeaverage(self, utterances):
        pass
    

