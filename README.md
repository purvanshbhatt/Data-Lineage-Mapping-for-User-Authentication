# Data Lineage Mapping for User Authentication

This project documents the flow of user authentication data across multiple systems to understand data dependencies and facilitate impact analysis for security upgrades.

## Methodology

* **Data Sources:** Web server logs, authentication database, system logs.
* **Tools:** SQL queries, [visualization tool name - e.g., Lucidchart, draw.io].
* **Analysis:** Traced the movement and transformation of user authentication data (usernames, passwords, authentication tokens) from initial input to storage and logging.

## Results

* Created a comprehensive data lineage map (see below) visualizing data dependencies.
* Identified critical data paths vulnerable to potential attacks.
* Discovered potential data quality issues related to inconsistent logging practices.

## Impact

* The data lineage map facilitated impact analysis for proposed security upgrades, reducing the risk of unintended consequences.
* Improved understanding of data quality issues, enabling faster resolution of user login problems.
* Connected data lineage insights with cybersecurity risk assessments to identify and mitigate potential threats to sensitive authentication data flows.

## Files

* `documentation/data-lineage-map.pdf`: The data lineage map.
* `documentation/data-dictionary.md`: Explanation of data fields and terms.
* `sql/queries.sql`: SQL queries used for data extraction and analysis.

## Data Lineage Map

![Data Lineage Map](documentation/data-lineage-map.pdf)
