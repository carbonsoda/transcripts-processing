> "We have a number of transcripts that need to get processed for various linguistic data

# Goals:
### 1. Create workflow to process transcripts into usable data ✔
### 2. Create workflow for non-tech savy person to analyze those transcripts/data

Raw transcript files are __all__ `SUBJECT_trans_final.txt`.

### Needed Data:
  1. Subject ID
  2. &#35; of total utterances in transcript
  2. &#35; of words in transcript (tokens)
  3. &#35; of diffrent words in transcripts: (types)
  4. Avg tokens per utterance
    - DO include if it's a verb, noun, etc. as a property as well. (once made avaliable to me)
  5. Timing Analysis
    - Will elaborate this when have the chance to

---

# Task 2:
> Related to the above, task 2 is to create a dictionary of words in all transcripts. The lab will use this document to create documentation of the property of each word. There will be a seperate document for each age of aquisition.

1. First create a modular one for 9mos. 
2. The first time around will have ie "dog" and "dogs" seperate
    - 2nd time some care will be needed to swap words with root types
        - This will need the use the word's tag (ie `[v] [n] [adj]` *verb noun adjective*) to determine
        - Some care and maybe human word will be needed to generate base words, such as `fish` used as a noun vs verb
*NOTE:* You do not need to do an age of acquisition function sorting thing (threshold etc), that will be done with RA's with existing theories but it's an idea for smth to include in future!

## Task 3:
> This is a third task that ties in with the 2nd, "create a program that you can enter a word and the output is a detailed documentation of who said the word and when/timestamp.
Created as `WordSearch.py`, currently no GUI at this time.
