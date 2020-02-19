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
 * Out of the box, git supports one pre-commit-hook (lots of overhead, in dev time or in commit time)

# Pre-commit hooks (are powerful and easy)
 * Has almost everything that you'd want (and the ability to add custom repos)
 * Setup takes less than a minute
