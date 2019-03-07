# Goals:
## 1. Create workflow to process transcripts into usable data
## 2. Create workflow for non-tech savy person to analyze those transcripts/data

> "We have a number of transcripts that need to get processed for various linguistic data

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

### When it comes time to user-end:
- First-Time Setup area
    - Directions
    - Error message directions
- Regular area:
  - Text boxes + 

## Back-end:
- Where will I export the sorted info?
- **1st time setup:**
    1. IF 
        1-1. HomeDirect = None 
        1-2. OR HomeDirect inaccessible (returns invalid/false existence)
        1-3. then request
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
