# Data Lineage Mapping for User Authentication

This project documents the flow of user authentication data across multiple systems to understand data dependencies and facilitate impact analysis for security upgrades.

## Methodology

* **Data Sources:** Web server logs, authentication database, system logs.
* **Tools:** 
    *  Data analysis and visualization: Python with `pandas`, SQL queries.
    *  Interactive visualization: Java with Swing.
    *  Advanced 3D visualization (optional): C++ with a graphics library (e.g., SFML, OpenGL).
* **Analysis:** Traced the movement and transformation of user authentication data (usernames, passwords, authentication tokens) from initial input to storage and logging.

## Project Structure

* **`datasets/`**: Contains the CSV datasets used for analysis:
    * `web_server_logs.csv`: Simulated web server logs with authentication data.
    * `user_data.csv`: User credentials and last login information.
* **`scripts/`**: Contains the scripts for data analysis and visualization:
    * `analyze.py`: Python script for data analysis and security checks.
    * `DataLineageMap.java`: Java code for interactive visualization.
    * `visualize.cpp`: C++ code for advanced 3D visualization (optional).

## Data Lineage Map

The following diagram illustrates the flow of authentication data within the system:

![Data Lineage Map](./data-lineage-map.png)  

* **User:** Initiates the authentication process by providing their credentials.
* **Web Server:** Receives the credentials, performs initial validation, and interacts with the database for authentication.
* **Database:** Stores user credentials and other relevant authentication data.

## Key Features

* **Data Analysis:**
    * Calculates login success rate and identifies users with multiple failed login attempts.
    * Analyzes user activity patterns and resource access counts.
    * Performs time series analysis of login attempts.
    * Correlates login activity with user's last login information.
* **Security Analysis:**
    * Detects potential SQL injection, cross-site scripting (XSS), and brute-force attacks.
    * Includes simplified examples for detecting authentication bypass and data exfiltration attempts.
* **Visualization:**
    * Provides an interactive visualization of the data lineage using Java Swing.
    * Optionally allows for advanced 3D visualization using C++ and a graphics library.

## Getting Started

1. Clone the repository.
2. Install the necessary dependencies (Python, pandas, Java, C++ compiler, SFML/OpenGL if using C++).
3. Run the `analyze.py` script to perform data analysis and security checks.
4. Compile and run the Java visualization (`DataLineageMap.java`).
5. (Optional) Compile and run the C++ visualization (`visualize.cpp`).

## Future Enhancements

* Expand security analysis with more sophisticated checks and tools.
* Enhance the Java visualization with more interactivity and data representation.
* Implement the C++ visualization for a more immersive experience.
* Integrate the project with real-time data streaming platforms (e.g., Apache Kafka).
* Explore data transformation and enrichment techniques for improved security.
