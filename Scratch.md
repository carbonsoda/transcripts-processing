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
    - &#35; utterances
    - avg &#35; words per each utterance *(for organization/ease, will be calculated elsewhere?)*
    
    - &#35; words in transcript
    - &#35; unique words *(can leave skeleton initially, maybs thing for task 2? or task 2 = optimized)*
    
    - &#35; different tokens
    - &#35; different word types
 5. 
    
 
