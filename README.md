# Support QA Scorecard

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
- Print/download support for QA reports
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

## Project Status

This project is actively developed and has a usable web calculator, command-line calculator, documentation, examples, and automated tests.

## Roadmap

- [x] Create the first QA scorecard template
- [x] Add detailed scoring guidelines
- [x] Add sample evaluated interactions
- [x] Add critical-error rules
- [x] Add automatic score calculation
- [x] Add contribution guidelines
- [x] Add a simple web-based version
- [x] Add automated tests
- [ ] Add exportable CSV or JSON report data
- [ ] Add configurable category weights

## Contributing

Contributions, suggestions, bug reports, and ideas are welcome.

If you have experience in customer support, quality assurance, or software development, feel free to open an issue or contribute to the project.

## License

This project is licensed under the MIT License.
