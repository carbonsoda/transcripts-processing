import os
import gc
import pandas as pd
import pickle

root = r"Q:\PSY-LAB\Suanda\Rollins\9mos"


# finds and pickles resulting dict
def playtime():
    times = {}

    for path, __, __ in os.walk(root):
        if path.endswith("Data"):
            folderfiles = sorted(next(os.walk(path))[2], reverse=True)  # list of files in the folder
            for file in folderfiles:
                if "_playtime.xlsx" in file[-14:]:
                    i = pd.read_excel(os.path.join(path, file))
                    temp = i.iat[0, 1]
                    subject = file[:4].upper()
                    times[subject] = temp

    picklepath = r"P:\Suanda\UtterAnalysis\time.pkl"
    with open(picklepath, 'wb') as f:
        pickle.dump(times, f)
        f.close()
    gc.collect()


# finds and saves resulting list as txt
def txtpathfind(naming):
    folders = naming[0]
    ext = naming[2]
    master = []
    messups = []

    for path, __, __ in os.walk(root):
        if path.endswith(folders):
            # list of files in the folder, in 'A to Z' alphabetical order
            folderfiles = sorted(next(os.walk(path))[2], reverse=True)
            # sorts through the files for desired extension
            for file in folderfiles:
                if ext in file[-16:]:
                    master.append(os.path.join(path, file))
                elif " .txt" in file[-5:]:
                    messups.append(file)
                    file.replace(" ", "")
                    master.append(os.path.join(path, file))
    gc.collect()

    mastertxt = os.path.join(
        os.environ["USERPROFILE"],
        "Desktop") + os.sep + "9master" + ext
    with open(mastertxt, 'w+') as fp:
        i = 0
        for item in master:
            if i == 0:
                fp.write(item)
                i = 99
            else:
                fp.write("\n" + str(item))
        fp.close()

    # %reset -f


def initialinput():
    while True:
        tier1 = input(
            "Is the file in the media OR Data folder? \n Type 'media' for media folder and 'data' for Data folder").lower()

        if tier1 == "data":
            tier2 = input("Is the file in a subfolder of Data? \n If no, type 'no'.\n If yes, please write ").lower()
            # I will write it more user friendly later rip
            if tier2 == "no":
                break
            else:
                # will need to check if .is_file()
                tier1 = tier1 + tier2
                break
        if tier1 == "media":
            break
        else:
            print("I didn't get that, try again please!")
            continue

    ext = input("What's the file naming convention? \n Example: _trans_final.txt")

    return ()


# naming = initialinput()
naming = tuple("Transcriptions", "_trans_final.txt")
txtpathfind(naming)
playtime()
