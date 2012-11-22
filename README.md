dota2-summary-viewer
====================
nodejs webapp and high level output generation scripts

#Setup
make sure the folder structure is there:
run data/createFolders.sh
data/replays
data/output

#producing summaries the easy way
scripts/produceSummary.py path/to/replay.dem

#getting the viewer up and running (viewer dir)
##install dependencies locally using node packet manager
npm install
node app

#installing snappy:
CFLAGS=-I$VIRTUAL_ENV/include LDFLAGS=-L$VIRTUAL_ENV/lib pip install python-snappy

