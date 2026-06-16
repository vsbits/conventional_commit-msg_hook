#!/bin/bash

install -D ./commit_msg.py ~/.githooks/commit-msg
chmod +x ~/.githooks/commit-msg
git config --global core.hooksPath  ~/.githooks
