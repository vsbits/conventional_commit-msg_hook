#!/usr/bin/env bash

DEST=~/.githooks/commit-msg

if [ -f $DEST ]; then
    echo "commit-msg hook already exists."
    echo "Creating backup"
    cp $DEST $DEST.backup
fi
install -D ./commit_msg.py ~/.githooks/commit-msg

echo "Making it executable"
chmod +x ~/.githooks/commit-msg

echo "Adding global git hooks path"
git config --global core.hooksPath  ~/.githooks

if git hook list commit-msg >/dev/null 2>&1; then
    echo "Done"
else
    echo "Failed to create hook"
    echo "---Aborting"
    exit 1
fi
