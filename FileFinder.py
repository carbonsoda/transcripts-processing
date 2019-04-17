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
def txtpathfind():
    master = []
    messups = []

    for path, __, __ in os.walk(root):
        if path.endswith("Transcriptions"):
            # list of files in the folder
            folderfiles = sorted(next(os.walk(path))[2], reverse=True)

            for file in folderfiles:
                if "_trans_final.txt" in file[-16:]:
                    master.append(os.path.join(path, file))
                elif " .txt" in file[-5:]:
                    messups.append(file)
                    file.replace(" ", "")
                    master.append(os.path.join(path, file))
    gc.collect()

    mastertxt = os.path.join(
        os.environ["USERPROFILE"],
        "Desktop") + os.sep + "9master.txt"
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


txtpathfind()
playtime()
