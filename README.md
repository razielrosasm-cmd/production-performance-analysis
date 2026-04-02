# Production Performance Analysis

## Overview

This project analyzes production performance using real-world operational metrics.

It evaluates:

* Efficiency (output vs expected)
* Quality (defects impact)
* Performance trends across multiple days
* Operational risk detection

The goal is to simulate how companies monitor productivity, detect issues, and make data-driven decisions.

---

## Business Problem

In production environments, managers need to:

* Detect underperforming days
* Identify quality issues
* Evaluate overall efficiency
* Prevent operational risks

This project provides a simplified analytical model to support those decisions.

---

## Features

* Efficiency calculation (%)
* Quality calculation (%)
* Daily performance tracking
* Average metrics analysis
* Detection of:

  * Days below target
  * High-risk days
  * Best and worst performance days
* Final operational status evaluation

---

## Project Structure

```id="l1w3nr"
production-performance-analysis/
│
├── src/
│   └── production_analysis.py
│
└── README.md
```

---

## Example Output

```id="b3y4n0"
===== PRODUCTION PERFORMANCE REPORT =====

Total expected: 5500
Total actual: 5450

Overall performance: 99.09%
Average efficiency: 98.75%
Average quality: 97.09%

Days below target: 0

Worst day deviation: -50
Best day deviation: 50

Final status: On Track
```

---

## Insights

* High overall efficiency indicates stable production
* No days below target → consistent performance
* Small deviations suggest minor variability
* System operating within acceptable limits

---

## Skills Demonstrated

* Python fundamentals
* Lists and loops
* Conditional logic (AND / OR)
* Data validation
* Function-based design
* Real-world data analysis

---

## Use Case

This type of analysis is used in:

* Manufacturing
* Supply chain operations
* Logistics performance tracking
* Production management

---

## Author

Raziel Rosas 

Raziel Rosas
