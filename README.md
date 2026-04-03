# figuring-out

a shared repo where we dump practice code while learning git and github. first year cs stuff — c programs, python scripts, dsa practice. each person has their own folder.

---

## what's in here

```
├── vishal/
│   ├── c/
│   │   ├── c.c            # hello world
│   │   ├── prime.c        # prime number check
│   │   └── stringswap.c   # splits a string into words
│   ├── py/
│   │   ├── DSA/
│   │   │   ├── sorting/
│   │   │   │   ├── bubble.py
│   │   │   │   └── insertion.py
│   │   │   └── searching/
│   │   │       └── binary search.py
│   │   ├── oops/
│   │   │   └── main.py
│   │   └── multiplication_nbn.py
│   └── leet/
│       └── 43.py
└── sarvesh/
    └── test.txt
```

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

other commands that are useful:
```bash
git status
git log --oneline
git restore filename                   # undo changes before staging
git remote -v                          # check remote connection
git clone <url>                        # copy a repo locally
git checkout origin/main -- filename   # pull a specific file
```

commit saves locally, push sends it to github. not the same thing.

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

---

## things that went wrong (so you don't repeat them)

- commits weren't showing on github — email in git config didn't match the github account. check this first
- vs code runs c in debug mode by default, gdb output looks like errors but isn't. use `Ctrl + F5` or just run from terminal
- didn't add `.gitignore` before first commit so `.exe` and `.vscode/` got tracked. had to use `git rm --cached` to fix it

---

## notes

- add a `.gitignore` — don't commit `.exe`, `.vscode/`, `__pycache__/`
- write a decent commit message, not just "update"
- keep your folder clean

---
