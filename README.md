# The One True Path (of which there are many)

Linting isn't about making people do things the Right Way, it's about everyone doing it the same way.
 * Python doesn't care if we wrap a string in apostrophies `'` or quotes `"` so why should we?
 * Consistancy is the most beneficial result of automated linting

# example PR with consistant linting:
https://github.com/ahonnecke/linting-talk/pull/1

![image](https://user-images.githubusercontent.com/419355/74870912-c99bb700-5317-11ea-9543-218994d119ac.png)

# example PR with inconsistant linting:
https://github.com/ahonnecke/linting-talk/pull/2

![image](https://user-images.githubusercontent.com/419355/74870841-a53fda80-5317-11ea-80e2-a5e4129d6aef.png)

# Git Hooks (are powerful)
 * Has anyone here written git hooks for linting multiple different file types?
 * Out of the box, git supports one pre-commit hook (lots of overhead, in dev time or in commit time)

# Pre-commit hooks (are powerful and easy)
 * Has almost everything that you'd want (and the ability to add custom repos)
 * Setup takes less than a minute

# Pip package installation

``` bash
ahonnecke@autoantonym:~/src/linting-talk$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

# Pip package configuration

``` bash
ahonnecke@autoantonym:~/src/linting-talk$ cat .pre-commit-config.yaml
# See http://pre-commit.com for more information
# See http://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.5.0
    hooks:
    - id: check-ast
    - id: flake8
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: mixed-line-ending
    - id: check-json
    - id: check-symlinks
    - id: check-yaml
    - id: check-added-large-files
-   repo: https://github.com/psf/black
    rev: 19.10b0
    hooks:
    - id: black
-   repo: https://github.com/timothycrosley/isort
    rev: 4.3.21
    hooks:
    - id: isort
-   repo: https://github.com/asottile/pyupgrade
    rev: v1.26.2
    hooks:
    -   id: pyupgrade
```

# Hook installation

``` bash
ahonnecke@autoantonym:~/src/linting-talk$ pre-commit autoupdate
Updating https://github.com/pre-commit/pre-commit-hooks ... already up to date.
Updating https://github.com/psf/black ... already up to date.
Updating https://github.com/timothycrosley/isort ... already up to date.
Updating https://github.com/asottile/pyupgrade ... already up to date.
```

# Hook execution

``` bash
ahonnecke@autoantonym:~/src/linting-talk$ pre-commit
Check python ast.....................................(no files to check)Skipped
Flake8 (deprecated, use gitlab.com/pycqa/flake8).....(no files to check)Skipped
Trim Trailing Whitespace.............................(no files to check)Skipped
Fix End of Files.....................................(no files to check)Skipped
Mixed line ending....................................(no files to check)Skipped
Check JSON...........................................(no files to check)Skipped
Check for broken symlinks............................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Check for added large files..........................(no files to check)Skipped
black................................................(no files to check)Skipped
isort................................................(no files to check)Skipped
pyupgrade............................................(no files to check)Skipped
```
