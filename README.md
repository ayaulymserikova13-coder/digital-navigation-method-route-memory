# The Effect of Digital Navigation Method on Route Memory in Young People

## Authors

- Ayaulym Serikova
- Gulnar Khabibullayeva

## Full Research Title

The Effect of Digital Navigation Method on Route Memory in Young People: A Comparison of Turn-by-Turn Directions and Prior Study of a Digital Map

## Overview

This project investigates how two digital navigation methods influence route memory in young people. The study compares turn-by-turn digital guidance with prior study of a digital map.

The study uses a quantitative preliminary randomized between-group design. Route memory is measured using direction recall accuracy and landmark recognition accuracy. Navigation habits during the previous 30 days are recorded using a structured questionnaire.

The planned sample consists of 20 young adult volunteers, with 10 participants assigned to each experimental condition.

## Research Questions

1. How frequently do participants report using turn-by-turn navigation and prior digital map study for unfamiliar-route walking trips during the past 30 days?
2. Does navigation method affect direction recall accuracy after one traversal of an unfamiliar walking route?
3. Does navigation method affect landmark recognition accuracy after one traversal of an unfamiliar walking route?

## Project Structure

.
├── README.md
├── .gitignore
├── LICENSE
├── Dockerfile
├── requirements.txt
├── configs/
│   └── config.yaml
├── src/
│   └── benchmark.py
├── data/
│   └── sample/
│       └── sample_results.csv
└── docs/
    └── methodology_card.md

## Planned Benchmarks

| Metric | Role | Comparison |
|---|---|---|
| Direction recall accuracy (%) | Primary Metric | TBT vs Map Study |
| Landmark recognition accuracy (%) | Secondary Metric | TBT vs Map Study |
| Navigation frequency over 30 days | RQ1 Metric | TBT use vs prior map-study use |
| Mean accuracy difference | Comparative Summary | Map Study mean − TBT mean |

The TBT group is used as the active baseline condition.

## Sample Data

The file data/sample/sample_results.csv contains synthetic test data created only to verify that the benchmark pipeline works correctly.

The sample file does not contain real participant data.

## System Requirements

- Python 3.11
- pandas 2.2.3
- PyYAML 6.0.2

Docker can also be used to reproduce the environment.

## Quickstart

Install the required dependencies:

python -m pip install -r requirements.txt

Run the benchmark:

python src/benchmark.py

The script reads the configuration and synthetic sample data, calculates the planned benchmark summaries, prints the results, and generates:

benchmark_results.csv

## Docker

Build the Docker image:

docker build -t route-memory-benchmark .

Run the benchmark:

docker run --rm route-memory-benchmark

## Methodology

The full Methodology Passport Card is available in:

docs/methodology_card.md

## Citation

Serikova, A., & Khabibullayeva, G. (2026). *The Effect of Digital Navigation Method on Route Memory in Young People: A Comparison of Turn-by-Turn Directions and Prior Study of a Digital Map.* GitHub research repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.