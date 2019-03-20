import os
import gc

master = []


def duplicates(stuff):
    for s in stuff:
        if "_trans_final.xlsx" in s:
            if "~$" in s:
                return s.replace("~$", "")
            else:
                return s
    for s in stuff:
        if "_trans_final.txt" in s:
            return s
        elif "_trans_final .txt" in s:
            return s.replace(" ", "")
    return None


def txtpathfind(root):    
    print("beginning search")

    for path, __, __ in os.walk(root):
        if path.endswith("Transcriptions"):
            stuff = sorted(next(os.walk(path))[2], reverse=True)
            s = duplicates(stuff)
            if s is not None:
                e = os.path.join(path, s)
                master.append(e)
    print(master)
    gc.collect()
    # %reset -f

def txtpathwrite(mastertxt):
    
    with open(mastertxt, 'w+') as fp:
        i = 0
        for item in master:
            if i == 0:
                print("first master")
                print(item)
                fp.write(item)
                i = 99
            else:
                fp.write("\n" + str(item))
        print("finished master")
        fp.close()
    print(master)
    gc.collect()


root = r"Q:\PSY-LAB\Suanda\Rollins\6mos"
txtpathfind(root)
print("found all files")

mastertxt = os.path.join(
        os.environ["USERPROFILE"], "Desktop") + os.sep + "6master.txt"
txtpathwrite(mastertxt)

#_transcription.xlsx
