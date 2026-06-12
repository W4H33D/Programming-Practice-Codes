### Final Project: The Subscription Growth Review

**Scenario**

You are working as a Junior Data Analyst at SkillSprint, an online learning platform that offers short subscription-based courses.

The company recently launched a new weekend promotion to increase subscriptions. At the end of the quarter, the business team wants a clear review of how the campaign performed.

You have been given a CSV file containing weekly performance data. Before you can analyze it, you need to inspect the file, clean several issues, organize the data into a usable structure, and then produce findings for two audiences:

- a technical audience (the product analytics team),
- a non-technical audience (the executive leadership team).

Your task is to complete the full beginner-level analytics workflow: data collection, preprocessing, storage, analysis, EDA, and data storytelling.

**Instructions**

1. **Load and Inspect Data**

Read the file weekly_growth.csv using Python. Print the rows, check the field names, count the number of records, and identify at least three quality issues in the dataset (for example: duplicates, inconsistent text formatting, or missing values).

2. **Clean and Store the Data**

Create a cleaned list of dictionaries named cleaned_data. Your cleaning should:

- standardize region names
- remove the exact duplicate row
- convert numeric fields to integers
- fill the missing support_tickets value with the median of the available ticket values
- and create a new field called conversion_rate using this formula:`paid_subscriptions / signups * 100`

3. **Perform the core Analysis**

Use the cleaned dataset to answer the following questions with code:

- What is the total revenue?
- Which region generated the highest total revenue?
- Which week had the highest revenue?
- What is the average conversion rate across all records?

**Conduct a short EDA Review**

Perform a short exploratory review of the cleaned dataset. At minimum:

- summarize revenue by week to see the trend,
- identify the record with the highest support ticket count,
- and explain whether the ticket pattern suggests a possible outlier or an area that deserves more investigation.

**Write a Technical Report**

Use your code results to write a short report for the product analytics team. Your report should include:

- the objective,
- data quality issues found and how you handled them,
- the key metrics,
- the EDA finding,
- and one follow-up recommendation.

You may follow this structure:

**Objective**

- Data Preparation
- Key Metrics
- EDA Notes
- Recommendation

**Create Presentation Summary for a Non-Technical Audience**

Write a short presentation-style summary for the executive leadership team. Your answer should be clear, simple, and persuasive. It should include:

- what was analyzed,
- the most important result,
- why it matters,
- what should happen next,
- and which two visuals you would recommend for the presentation.

7. **Deliverables**

- A working Python solution that loads, cleans, and analyzes the CSV file.
- A cleaned dataset stored in a Python structure.
- A short technical report.
- A short presentation-style summary for a non-technical audience.
- This final project brings together the full beginner workflow of data analytics with Python. Good luck!
