# Support QA Scorecard

[![Automated Tests](https://github.com/SoumikMallick30/support-qa-scorecard/actions/workflows/python-app.yml/badge.svg)](https://github.com/SoumikMallick30/support-qa-scorecard/actions/workflows/python-app.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Live Demo

Try the Support QA Score Calculator here:

https://soumikmallick30.github.io/support-qa-scorecard/

An open-source quality assurance scorecard for evaluating customer support interactions, identifying coaching opportunities, and improving service quality.

## Purpose

Support QA Scorecard helps customer support teams, Quality Analysts, and Team Leads evaluate customer interactions with a simple, consistent quality framework.

The project is designed to make support quality reviews easier to run, easier to explain, and reusable across different customer service teams.

## QA Categories

The scorecard evaluates customer interactions across key quality areas:

| Category | Weight |
| --- | ---: |
| Communication & Professionalism | 20% |
| Understanding the Customer's Issue | 20% |
| Resolution & Accuracy | 30% |
| Process Compliance | 15% |
| Customer Experience | 15% |
| **Total** | **100%** |

## Current Features

- 100-point QA scoring framework
- Web-based QA score calculator
- Python command-line calculator
- Reusable scoring logic with automated tests
- Critical-error tracking
- QA feedback and coaching notes
- JSON and CSV report exports
- Print-ready QA reports
- Detailed scoring guidelines
- Sample evaluated interaction
- Contribution guidelines

## Who Is This For?

This project can be useful for:

- Quality Analysts
- Customer Support Teams
- QA Leads
- Team Leaders
- Operations Managers
- Small support teams building a QA process from scratch

## Running the QA Score Calculator

The project includes a Python calculator for automatically calculating QA scores.

### Requirements

- Python 3.8 or newer
- No external packages required

### Interactive Mode

Clone this repository and run:

```bash
python src/score_calculator.py
```

The calculator will ask for scores across the five QA categories and whether a critical error was identified.

### Scripted Mode

You can also pass all scores as command-line arguments:

```bash
python src/score_calculator.py \
  --communication 18 \
  --understanding 17 \
  --resolution 24 \
  --compliance 12 \
  --experience 12 \
  --critical-error
```

The calculator displays the final score, performance rating, and critical-error status.

## Running Tests

Run the automated test suite with:

```bash
python -m unittest discover -s tests -v
```

Run the web scoring and export tests with Node.js 22 or newer:

```bash
node --test tests/test_web_calculator.js
```

## Project Status

Version 1.1 includes a usable web calculator, command-line calculator, portable report exports, documentation, examples, and automated Python and JavaScript tests.

## Roadmap

- [x] Create the first QA scorecard template
- [x] Add detailed scoring guidelines
- [x] Add sample evaluated interactions
- [x] Add critical-error rules
- [x] Add automatic score calculation
- [x] Add contribution guidelines
- [x] Add a simple web-based version
- [x] Add automated tests
- [x] Add exportable CSV or JSON report data
- [ ] Add configurable category weights
- [ ] Add saved evaluation history
- [ ] Add anonymized example datasets

## Contributing

Contributions, suggestions, bug reports, and ideas are welcome.

If you have experience in customer support, quality assurance, or software development, feel free to open an issue or contribute to the project.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and [SECURITY.md](SECURITY.md) for responsible vulnerability reporting.

## Privacy

The web calculator runs entirely in your browser and does not send evaluation data to a server. Avoid entering sensitive customer information in exported reports unless your organization has approved that use.

## License

This project is licensed under the MIT License.
