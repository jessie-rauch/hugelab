# Hugelab Command Line Cheat Sheet

A reference for the commands most useful in the beacon workflow.
Copy-paste friendly. No memorization required.

---

## Navigation

```bash
cd ~/Documents/hugelab                  # go to hugelab root
cd ~/Documents/hugelab/pet-insurance    # go into a client folder
cd ..                                   # go up one level
ls                                      # list what's in the current folder
```

---

## Find & Replace Inside a File

```bash
sed -i '' 's|old text|new text|g' filename.html
```

- `s` = substitute
- `|old|new|` = find this, replace with that (use `|` so you can have `/` in URLs)
- `g` = do it everywhere in the file, not just the first match

**Real examples from this project:**

```bash
# Fix image paths after renaming the repo
sed -i '' 's|jessie-rauch/beacons-pet_insurance/main|jessie-rauch/hugelab/main/pet-insurance|g' index.html

# Change the password
sed -i '' 's|huge123|pets123|g' beacons/index.html journey/index.html

# Fix the page title
sed -i '' 's|Trupanion · Three Journey Narratives|New Pet Insurance Brand — Journey Narratives|g' journey/index.html
```

---

## Crop Screenshots (the Python script)

```bash
cd /path/to/your/screenshots
python3 crop_mobile.py .
```

- Finds every file ending in `_mobile.png` in the folder and all subfolders
- Crops each one to 1284×2915 from the top
- Skips anything shorter than 2915px and tells you
- Overwrites in place

---

## Git — Saving & Publishing

The basic loop every time you make changes:

```bash
git add .                               # stage all changed files
git status                              # check what's about to be committed
git commit -m "describe what you did"  # save a snapshot
git push                                # send to GitHub (Netlify auto-deploys)
```

**Useful variations:**

```bash
git add beacons/index.html             # stage just one file
git reset                              # unstage everything (nothing is lost)
git log --oneline                      # see recent commit history
```

---

## Git — Setup (first time for a new project)

```bash
cd ~/Documents/hugelab/[client-folder]
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/jessie-rauch/hugelab.git
git branch -M main
git push -u origin main --force
```

---

## Git — Fix the Remote URL

If git is pushing to the wrong repo:

```bash
git remote set-url origin https://github.com/jessie-rauch/hugelab.git
```

---

## Find Text Inside a File

```bash
grep -n "thing to find" filename.html
```

- `-n` shows the line number alongside the result
- Useful for checking if a replacement worked, or finding where something lives

```bash
# Check a password change worked
grep -n "pets123" index.html

# Find all image URLs
grep -n "raw.githubusercontent" index.html | head -5
```

---

## .gitignore — Keep Junk Out of the Repo

If you ever need to recreate the `.gitignore` file:

```bash
echo "node_modules/" > .gitignore
echo ".DS_Store" >> .gitignore
```

- `>` creates the file (overwrites if it exists)
- `>>` adds a new line to an existing file

---

## Hugelab Repo Structure (for reference)

```
jessie-rauch/hugelab (GitHub)
  │
  ├── pet-insurance/
  │   ├── beacons/
  │   │   ├── index.html
  │   │   └── [category]/[site]/screenshots...
  │   └── journey/
  │       └── index.html
  │
  └── [next-client]/
      └── beacons/
          └── index.html
```

**Live URLs:**
- `hugelab.netlify.app/pet-insurance/beacons/`
- `hugelab.netlify.app/pet-insurance/journey/`

**Image path pattern for new projects:**
```
https://raw.githubusercontent.com/jessie-rauch/hugelab/main/[client]/[category]/[site]/filename.png
```

**Password:** `pets123` (pet insurance project)

---

## Quick Fixes Cheat Sheet

| Problem | Command |
|---|---|
| Images broken after repo rename | `sed -i '' 's\|old-repo/main\|hugelab/main/client\|g' index.html` |
| Wrong password in file | `sed -i '' 's\|oldpass\|newpass\|g' index.html` |
| Push going to wrong repo | `git remote set-url origin https://github.com/jessie-rauch/hugelab.git` |
| node_modules in git | `git rm -r --cached node_modules` then add to `.gitignore` |
| Unstage everything | `git reset` |
