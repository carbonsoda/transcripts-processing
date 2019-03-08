> "We have a number of transcripts that need to get processed for various linguistic data

# Goals:
## 1. Create workflow to process transcripts into usable data
## 2. Create workflow for non-tech savy person to analyze those transcripts/data




__Format of transcript files:__
    - `SUBJECT_trans_final.txt`
    - It's a txt but best to open in excel to achieve columns/organized view
    - File path: `Q:\PSY-LAB\Suanda\Rollins\Nmos\SUBJECT\Data\Transcriptions`
    

## Needed Data:
  ### 1. # of utterances in transcript
  ### 2. # of words in transcript
  ### 3. # of word-types in transcripts:
      - aka # of different words
      - "types and tokens"
      - DO include if it's a verb, noun, etc. as a property as well. (helps for task 2)
  ### 4. Timestamps of each type
  ### 5. Also it should create list of subjects (`sublist_9mos`):
      - List could be in another file, and the data is structured like a node (hash kinda I guess?), such that `subject` has:
          1. Identifier (`Sub`) (Also number? it's labeled as "No")
          2. Age (`Folder`)
          3. transcript data (another node, contains points 1, 2, and 3)
 
## For Goal 1:
    Order of priorities (what to design/create):
        1. Take in the file and return duplicate of it (make sure can just input file at all)
        2. 
### For Goal 2:
  Feature: can type in subject + filters as needed
      > exports the processed data to a log file (perhaps csv? need to think of exact details)

---
# _Brainstorming_
Having an application would be best to go with goal 2, however it would be good to just focus on something modular working like goal 1 that can run in terminal, before creating the user-end stuff.
When it comes to sorting through 

## When it comes time to user-end:
- First-Time Setup area
    - Directions
    - Error message directions
- Regular area:
  - Text boxes + 
### Back-end/User-end mixed 
- Where will I export the sorted info?
- **1st time setup:**
    1. IF 
        1. HomeDirect = None 
        2. OR HomeDirect inaccessible (returns invalid/false existence)
        3. then request
            - Should probably create way that checks if given directory is correct
            - CHECKS syntax, and corrects as needed
                - wrong direction slashes, spaces in any part
            - IF inaccessible even if correcting, return error message
    2. Save the inputted info in setup settings (txt file or as variable setting smth?, optimize later)
    3. Asking for home directory for purpose if this data is ever moved off Q drive and onto like lab dedicated local server
    4. Base Analysis:
      - Ask if OK to run full analysis right now on ALL
      - Regardless, collect # of subjects per age group
- **Regular:**
    1. Ask for Age (`N`mos)
        - Ask want average of each age
        - If no existing logs, confirm if OK and warn that may take a while!!
    2. Ask IF subject ID:
        1. IF no, ask if want ALL
           1. Check if existing log file exists
              - if not, ask if OK with taking while to compile (also show # of subject? From "No" count)
        2. Run through analysis functions
 - **Analysis:**
    - IF (`run on ALL`):
        - IF (`no_specified_age`): *ie first time run or want overall average* (`check_all_existing`) = False: 
            > *check_all_existing sees if all parts have files, if not 
    - IF 
    
 ## Back-end:
 > *KEY: `[S]` = a structure `[F]` = work `[G]` = GUI*
 
 1. Interface `[G]`
 2. Processing `[F]`
    - Import File
    - Removes all rows with `[speechx]` + `[vocplayx]`
        - need to clarify what these indicators mean
            - seems like `[vocplayx]` = space, as in pause or like vocalizing w/o meaning? like `uhhhhhhh`
    - 
 3. Subject Node `[S]`
    - ID (ie AF09)
    - NO (Number, such as in the sublist *(is this needed though?)*
    - Age (`N`mos)
    - TRANS `[S]`
 4. Subject's Transcript Node `[S]`
    No work is done for this! Just storage for right now
    - # utterances
    - avg # words per each utterance *(for organization/ease, will be calculated elsewhere?)*
    
    - # words in transcript
    - # unique words *(can leave skeleton initially, maybs thing for task 2? or task 2 = optimized)*
    
    - # different tokens
    - # different word types
 5. 
    
 
# Task 2:
> Related to the above, task 2 is to create a dictionary of words in all transcripts. The lab will use this document to create documentation of the property of each word. There will be a seperate document for each age of aquisition.

1. First create a modular one for 9mos. 
2. The first time around will have ie "dog" and "dogs" seperate
    - 2nd time some care will be needed to swap words with root types
        - This will need the use the word's tag (ie `[v] [n] [adj]` *verb noun adjective*) to determine
        - Some care and maybe human word will be needed to generate base words, such as `fish` used as a noun vs verb
*NOTE:* You do not need to do an age of acquisition function sorting thing (threshold etc), that will be done with RA's with existing theories but it's an idea for smth to include in future!

## Task 2.5:
> This is a third task that ties in with the 2nd, "create a program that you can enter a word and the output is a detailed documentation of who said the word and when/timestamp.
