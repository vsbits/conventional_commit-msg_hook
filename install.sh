#!/usr/bin/env bash

echo "Copying file"
install -D ./commit_msg.py ~/.githooks/commit-msg

echo "Making it executable"
chmod +x ~/.githooks/commit-msg

echo "Adding global git hooks path"
git config --global core.hooksPath  ~/.githooks

if git hook list commit-msg >/dev/null 2>&1; then
    echo "Done"
else
    echo "Failed to create hook"
    echo Aborting
    exit 1
fi
