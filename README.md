# Conventional commit hook

Python commit-msg hook based on
[Conventional Commits](https://www.conventionalcommits.org).

## Features

Current script only checks if the *subject* part of the commit message respects
the structure `<type>[optional scope]: <description>`.

## Installation

Copy the file [`commit_msg.py`](commit_msg.py) to the
[git hooks directory](https://git-scm.com/book/pt-br/v2/Customizing-Git-Git-Hooks#_installing_a_hook),
rename it to `commit-msg`, and make it executable.

### Auto install globally

To install the hook globally to the current user, clone the repository and run
the [`global_install.sh`](global_install.sh):

```
git clone https://github.com/vsbits/conventional_commit-msg_hook && \
  cd conventional_commit-msg_hook && \
  bash global_install.sh
```

It will copy the script file to user directory, make it executable and define
`~/.githooks` as a global path for git hooks scripts.

### Dependencies

Script requires [git](https://git-scm.com/) and [python](https://www.python.org/) installed.
