#! /bin/sh
# runs the toolchain on a file of choice, for quick testing purposes
TEST_REPLAY_FILE=63270488
TEST_REPLAY_PATH=data/replays/averageGames/${TEST_REPLAY_FILE}.dem

./scripts/processDem.py $TEST_REPLAY_PATH
#less data/output/${TEST_REPLAY_FILE}/extract.demson
less data/output/${TEST_REPLAY_FILE}/factionConflict.json
