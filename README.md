# figuring-out

a shared repo where we dump practice code while learning git and github. first year cs stuff — c programs, python scripts, dsa practice. each person has their own folder.

---

## what's in here

```
figuring-out/
├── vishal/
│   ├── c/            # C programs — prime check, string swap, Kaprekar's visualizer
│   ├── py/            # python scripts — Collatz/Kaprekar, sieve of eratosthenes,
│   │   ├── DSA/       #   sorting (bubble, insertion), searching (binary), bit manipulation
│   │   └── oops/      #   OOP practice
│   └── leet/          # leetcode solutions (43, 54, 74, 168, 171, 172, 1154 ...)
└── sarvesh/           # just getting started
```

each person's folder is their own space — structure inside it is up to you.

---

## how to contribute

make your own folder with your name and put your code there. don't touch anyone else's folder.

```bash
git clone https://github.com/Proxyprisoner/figuring-out.git
cd figuring-out
mkdir yourname
```

then just add your files, commit and push:
```bash
git add .
git commit -m "what you added"
git push
```

---

## git stuff worth knowing

basic flow:
```bash
git add .
git commit -m "message"
git push
```

commit saves locally, push sends it to github. not the same thing.

**checking things:**
```bash
git status
git log --oneline
git log --oneline --graph --decorate -15
git diff                # unstaged changes
git diff --cached       # staged changes
git remote -v           # check remote connection
```

**config / identity:**
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global --list
```
if commits aren't showing up on github, this is the first thing to check — see below.

**branches:**
```bash
git branch
git branch -vv
git switch main
git switch -c new-branch
```

**undoing stuff:**
```bash
git restore filename                   # undo changes before staging
git restore .                          # undo all unstaged changes
git checkout origin/main -- filename   # pull a specific file from remote
git clean -fd                          # remove untracked files/folders
```

**stash (save changes without committing):**
```bash
git stash -u        # -u also grabs untracked files
git stash pop
git stash list
```

**pulling with rebase (keeps history clean, avoids merge commits):**

if `git status` shows modified or untracked files, git will block a rebase until they're committed, restored, or stashed.

keep your changes:
```bash
git stash -u
git pull --rebase origin main
git push origin main
git stash pop
```

discard your changes instead:
```bash
git restore .
git pull --rebase origin main
git push origin main
```

**removing old commits (interactive rebase):**
```bash
git rebase -i HEAD~5
```
change `pick` to `drop` next to the commit you want gone, save and close, then:
```bash
git push --force-with-lease origin main
```
`--force-with-lease` is safer than `--force` — it won't overwrite work if someone else pushed in the meantime.

**resetting (be careful, this rewrites history):**
```bash
git reset --soft HEAD~4    # undo commits, keep changes staged
git reset --mixed HEAD~4   # undo commits, keep changes unstaged
git reset --hard HEAD~4    # undo commits AND discard changes — permanent
```

**GitHub CLI:**
```bash
gh auth status
gh --version
git --version
```

---

## running the code

**C:**
```bash
gcc vishal/c/prime.c -o prime
./prime
```

**Python:**
```bash
python vishal/py/DSA/sorting/bubble.py
```

filenames with spaces or apostrophes (like `Kaprekar's Constant visualizer.py`) need quotes:
```bash
python "vishal/py/Kaprekar's Constant visualizer.py"
```

leetcode solutions run the same way — they're plain scripts, not judge submissions:
```bash
python vishal/leet/74.py
```

---

## things that went wrong (so you don't repeat them)

- commits weren't showing on github — email in git config didn't match the github account. check this first (`git config --global user.email`)
- pushing under the wrong github account on windows — open Credential Manager → Windows Credentials → remove the `git:https://github.com` entry → `git push` again and sign in as the right account
- vs code runs c in debug mode by default, gdb output looks like errors but isn't. use `Ctrl + F5` or just run from terminal
- didn't add `.gitignore` before first commit so `.exe` and `.vscode/` got tracked. had to use `git rm --cached` to fix it

---

## notes

- add a `.gitignore` — don't commit `.exe`, `.vscode/`, `__pycache__/`
- write a decent commit message, not just "update"
- keep your folder clean

---
