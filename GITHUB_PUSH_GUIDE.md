# GitHub Push Guide

## Prerequisites

1. **Install Git**
   - Download from: https://git-scm.com/download/win
   - Install with default settings

2. **Create GitHub Account**
   - Sign up at: https://github.com

3. **Create New Repository on GitHub**
   - Go to: https://github.com/new
   - Repository name: `prabhav-ai` (or your choice)
   - Description: "Advanced Conversational Analytics Powered by AI"
   - Choose: Public or Private
   - **DO NOT** initialize with README, .gitignore, or license
   - Click "Create repository"

## Method 1: Using Batch Script (Easiest)

1. **Run the script**
   ```bash
   push_to_github.bat
   ```

2. **Follow prompts**
   - Enter commit message (or press Enter for default)
   - Enter your GitHub repository URL
   - Enter credentials when prompted

3. **Done!** Your code is now on GitHub

## Method 2: Manual Commands

### Step 1: Initialize Git
```bash
cd c:\Users\gouri\OneDrive\Desktop\iitbbsr
git init
```

### Step 2: Configure Git (First time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Add Files
```bash
git add .
```

### Step 4: Commit
```bash
git commit -m "Initial commit - Prabhav AI Causal Reasoning System"
```

### Step 5: Add Remote
```bash
git remote add origin https://github.com/YOUR_USERNAME/prabhav-ai.git
```

### Step 6: Push
```bash
git branch -M main
git push -u origin main
```

## Authentication

### Option 1: Personal Access Token (Recommended)

1. **Create Token**
   - Go to: GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
   - Click "Generate new token (classic)"
   - Name: "Prabhav AI"
   - Expiration: 90 days (or your choice)
   - Scopes: Check `repo` (full control of private repositories)
   - Click "Generate token"
   - **COPY THE TOKEN** (you won't see it again!)

2. **Use Token**
   - When prompted for password, paste your token

### Option 2: GitHub CLI
```bash
# Install GitHub CLI
winget install --id GitHub.cli

# Authenticate
gh auth login

# Push
gh repo create prabhav-ai --public --source=. --remote=origin --push
```

## Handling Large Files

GitHub has a 100MB file size limit. Your model files are too large.

### Solution: Use Git LFS or Releases

#### Option A: Git LFS (Large File Storage)
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.pkl"
git lfs track "*.faiss"
git lfs track "*.zip"
git lfs track "sentence_transformer_model/*"

# Add .gitattributes
git add .gitattributes

# Commit and push
git add .
git commit -m "Add large files with LFS"
git push
```

#### Option B: GitHub Releases (Recommended)
1. Push code without large files (they're in .gitignore)
2. Go to your repository on GitHub
3. Click "Releases" > "Create a new release"
4. Tag: `v1.0.0`
5. Title: "Prabhav AI v1.0 - Model Files"
6. Upload files:
   - `sentence_transformer_model.zip`
   - `df_turns_resampled.pkl`
   - `causal_engine_index.faiss`
   - `transcripts.json`
7. Publish release
8. Update README with download links

## Updating README

After pushing, replace `GITHUB_README.md` content into `README.md`:

```bash
# On GitHub website
1. Go to your repository
2. Click on README.md
3. Click edit (pencil icon)
4. Copy content from GITHUB_README.md
5. Update download links with your release URLs
6. Commit changes
```

## Common Issues

### Issue: "fatal: not a git repository"
**Solution**: Run `git init` first

### Issue: "remote origin already exists"
**Solution**: 
```bash
git remote remove origin
git remote add origin YOUR_URL
```

### Issue: "failed to push some refs"
**Solution**:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Issue: "Authentication failed"
**Solution**: Use Personal Access Token instead of password

### Issue: "file too large"
**Solution**: Use Git LFS or upload to Releases

## Verify Success

1. Visit: `https://github.com/YOUR_USERNAME/prabhav-ai`
2. Check files are uploaded
3. Verify README displays correctly
4. Test clone: `git clone https://github.com/YOUR_USERNAME/prabhav-ai.git`

## Next Steps

1. **Add Topics** (on GitHub)
   - machine-learning
   - nlp
   - causal-reasoning
   - flask
   - python
   - ai

2. **Add Description**
   - "Advanced Conversational Analytics Powered by AI"

3. **Add Website** (if deployed)
   - Your deployment URL

4. **Enable Issues**
   - Settings > Features > Issues

5. **Add License**
   - Create LICENSE file (MIT, Apache, etc.)

6. **Add Contributors**
   - Settings > Collaborators

7. **Create Documentation**
   - Wiki or docs folder

## Sharing Your Project

Share your repository:
```
https://github.com/YOUR_USERNAME/prabhav-ai
```

Clone command for others:
```bash
git clone https://github.com/YOUR_USERNAME/prabhav-ai.git
```

## Maintenance

### Update repository:
```bash
git add .
git commit -m "Update: description of changes"
git push
```

### Create branches:
```bash
git checkout -b feature-name
# Make changes
git add .
git commit -m "Add feature"
git push -u origin feature-name
```

---

**Need Help?**
- GitHub Docs: https://docs.github.com
- Git Docs: https://git-scm.com/doc
- Stack Overflow: https://stackoverflow.com/questions/tagged/git
