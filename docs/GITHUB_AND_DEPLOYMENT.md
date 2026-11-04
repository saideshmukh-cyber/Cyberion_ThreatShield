# GitHub push and optional publishing

## 1. Install and configure Git
Install Git from the official Git website. Then run:
```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
Use the email you want associated with commits; do not put credentials here.

## 2. Initialize repository
From the project root:
```bash
git init
git status
git add README.md LICENSE .gitignore requirements.txt docs rules scripts tests reports presentation data/sample
git status
git commit -m "Initial CDL detection engineering scaffold"
```
Review `git status` before `git add`/commit. Confirm `data/raw/` and secrets are not staged.

## 3. Create a GitHub repository
On GitHub, create a new empty repository named `cyberion-detection-engineering`. For the easiest first push, do not initialize it with a README or license because those already exist locally. Copy the repository HTTPS URL shown by GitHub.

## 4. Connect and push
Replace the example URL with your own repository URL:
```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cyberion-detection-engineering.git
git push -u origin main
```
GitHub may ask you to authenticate through a browser or credential manager. Do not paste access tokens into chat or source files.

## 5. Subsequent changes
```bash
git status
git add <specific-files>
git commit -m "Describe the change"
git push
```
Prefer specific files over `git add .` until you understand what is being staged.

## 6. Optional GitHub Pages
The PRD does not require a hosted application. If you want a public portfolio, first review every file and remove confidential information. In GitHub repository settings, look for Pages and select a supported publishing source/branch according to GitHub's current UI. A Markdown-only repository may be better published using a documentation generator. Publishing the repository itself is sufficient for this deliverable; no runtime deployment is needed.

## 7. Verify push
Refresh the repository page and confirm README, rules, reports, tests, and docs appear. Clone the repository into a fresh temporary folder and rerun installation/tests to check reproducibility.
