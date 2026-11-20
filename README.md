# Skill Path Triage Assistant

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/28j278p6fw/badge.svg)](https://ask.thili.ai/b/28j278p6fw)

The **Skill Path Triage Assistant** is an HR and Hiring tool designed to help HR managers understand employee career progression. It analyzes employee skill acquisition sequences, identifies frequent skill transition patterns, and uses a language model to recommend relevant next skills for career development and training.

## Project Objectives

- Represent employee skills as sequences over time.
- Identify frequent skill transition patterns using thilimarketbasket.
- Generate AI-powered next-skill recommendations.
- Evaluate recommendation performance against actual employee skill sequences.
- Provide a command-line interface (CLI) for HR managers.

## Technologies Used

- Python 3.12
- Groq API
- OpenAI-compatible Chat Completions API
- thilimarketbasket
- Pytest
- Git and GitHub

## Milestones

- [x] **1. Define employee skill sets or job roles as sequences over time.**

  Created five sample employee skill sequences containing Python, SQL, Machine Learning, Deep Learning, NLP, Data Analytics, and Power BI.

- [x] **2. Mine frequent skill/role transition patterns using thilimarketbasket.**

  Used frequent itemset mining and association rule generation to identify common consecutive skill transitions among employees.

- [ ] **3. Train a language model on these sequences to predict the next skill.**

  Integrated the Groq API with the `openai/gpt-oss-20b` model to generate next-skill recommendations based on employee skills and available skill sequences.

  **Implementation note:** API-based inference with an existing pretrained language model has been implemented. However, continued pretraining or fine-tuning on the employee skill sequences has not been performed.

- [x] **4. Evaluate the model's ability to suggest relevant next steps in career development.**

  Evaluated recommendations using five employee skill sequences by comparing the actual final skill with the generated model responses.

- [x] **5. Provide a CLI to input current skills/role and get suggestions for next steps.**

  Implemented commands for checking application status and generating AI-powered skill recommendations.

## Evaluation Results

The assistant was evaluated using five employee skill sequences.

| Evaluation Metric | Result |
|---|---:|
| Total predictions | 5 |
| Correct predictions | 4 |
| Incorrect predictions | 1 |
| Preliminary match rate | 80% |

Accuracy calculation:

    Match Rate = (Correct Matches / Total Predictions) × 100
    Match Rate = (4 / 5) × 100 = 80%

**Evaluation limitation:** The evaluation uses a small synthetic dataset of five employee sequences. A prediction is counted as correct if the actual next skill appears anywhere in the model's response. Therefore, the 80% result is a preliminary text-match rate, not a reliable Top-1 recommendation accuracy measure or evidence of general model performance.

## Project Structure

    skill-path-triage-assistant/
    |
    |-- app/
    |   |-- __init__.py
    |   |-- cli.py
    |   |-- core.py
    |   |-- llm.py
    |   |-- storage.py
    |
    |-- tests/
    |   |-- test_core.py
    |   |-- test_smoke.py
    |
    |-- .github/
    |   |-- workflows/
    |       |-- ci.yml
    |
    |-- .env.example
    |-- .gitignore
    |-- evaluate.py
    |-- pytest.ini
    |-- requirements.txt
    |-- README.md

## Setup Instructions

### 1. Clone the Repository

    git clone <your-github-repository-url>
    cd skill-path-triage-assistant

### 2. Create a Virtual Environment

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Configure the Language Model

Create a `.env` file using `.env.example` as a reference.

Configure the following settings:

    LLM_BASE_URL=https://api.groq.com/openai/v1
    LLM_API_KEY=your_groq_api_key
    LLM_MODEL=openai/gpt-oss-20b

    DATA_PATH=data/app.json

Replace `your_groq_api_key` with your own Groq API key.

**Security:** Never commit `.env` or expose your API key in source code or public repositories.

## CLI Usage

### Check Application Status

    python -m app.cli hello

### Generate a Next-Skill Recommendation

    python -m app.cli recommend --skills Python SQL

Example output:

    Current skills: Python, SQL

    Generating recommendation...

    AI Recommendation:
    Recommended next skill: Machine Learning

### Display Available Commands

    python -m app.cli --help

## Running the Evaluation

Run the evaluation script:

    python evaluate.py

The script evaluates all five employee sequences and displays the actual next skill, prediction correctness, and overall match rate.

## Running Tests

Execute the automated test suite:

    pytest -v

The project currently passes all seven automated tests.

## Security and Configuration

- API credentials are stored locally in `.env`.
- `.env` is excluded through `.gitignore`.
- Virtual environments and generated local data are excluded from version control.
- `.env.example` provides a configuration template without exposing credentials.

## Future Improvements

- Perform actual language model fine-tuning or continued pretraining on employee skill sequences.
- Expand the employee dataset with real-world career progression data.
- Improve recommendation evaluation using larger test datasets and ranking metrics.
- Incorporate employee roles, experience levels, and career goals.
- Develop a graphical interface for HR managers.

## Conclusion

The Skill Path Triage Assistant demonstrates frequent skill transition mining, AI-powered next-skill recommendation, preliminary recommendation evaluation, and CLI-based interaction.

It provides a foundation for identifying employee skill development opportunities and supporting data-driven career development decisions.