import os
import sys
import glob
import prettyprinter
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--test", help="Test mode", action="store_true")
parser.add_argument("-o", "--type",    help="file ext", default=".mp3")
args = parser.parse_args()

FILES = glob.glob("./*.%s" % args.type)
FILES.sort()
if args.test:
    prettyprinter.pprint(FILES)


# Step 1 - make new copies
for F in FILES:
    print ("make new %s" % F)
    shutil.copyfile(F, "%s.new" % F)
#step 2 - remove old files
for F in FILES:
    print ("remove old %s" % F)
    os.remove(F)
#step 3 rename backurl
for F in FILES:
    print ("rename new to original name for %s" % F)
    os.rename("%s.new" % F, F)
