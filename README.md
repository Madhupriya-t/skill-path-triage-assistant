# Skill Path Triage Assistant

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/28j278p6fw/badge.svg)](https://ask.thili.ai/b/28j278p6fw)

The Skill Path Triage Assistant is an HR & Hiring tool designed to help HR managers understand employee career progression. By analyzing sequences of acquired skills or job roles, it can predict the next likely skill an employee might need or role they might pursue, aiding in career development and training identification.

## What you are building

**Goal.** You will build a Skill Path Triage Assistant that helps HR managers analyze employee skill acquisition sequences to suggest relevant next courses or identify common skill gaps for team training.

**Done when.** The model's ability to suggest relevant next steps in career development has been evaluated, demonstrating the application of frequent itemset mining and language model continued pretraining to skill sequences.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Define employee skill sets or job roles as sequences over time.**  
      Hint: Define employee skill sets or job roles as sequences over time.
- [ ] **2. Mine frequent skill/role transition patterns using `thilimarketbasket`.**  
      Hint: Mine frequent skill/role transition patterns using `thilimarketbasket` from the 'Teach a Language Model What Sells Together' drill.
- [ ] **3. Train an LM on these sequences to predict the next skill or role.**  
      Hint: Train an LM on these sequences to predict the next skill or role, applying techniques from the 'Teach a Language Model What Sells Together' drill.
- [ ] **4. Evaluate the model's ability to suggest relevant next steps in career development.**  
      Hint: Evaluate the model's ability to suggest relevant next steps in career development.
- [ ] **5. Provide a CLI to input current skills/role and get suggestions for next steps.**  
      Hint: Provide a CLI to input current skills/role and get suggestions for next steps.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- (none)
