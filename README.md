# Conventional commit hook

Python commit-msg hook based on [Conventional Commits](https://www.conventionalcommits.org).

## Features

Current script only checks if the *subject* part of the commit message respects the structure `<type>[optional scope]: <description>`.

## Installation

Clone the repository and run the [`install.sh`](install.sh).

```
git clone https://github.com/vsbits/conventional_commit-msg_hook && \
  cd conventional_commit-msg_hook && \
  bash install.sh
```

It will copy the script file to user directory, make it executable and define
`~/.githooks` as a global path for git hooks scripts.

### Dependencies

Script requires [git](https://git-scm.com/) and [python](https://www.python.org/) installed.
