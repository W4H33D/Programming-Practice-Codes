### Project: The Automated Sales Auditor

**Scenario**

You have been hired as a Junior Data Analyst for a pop-up retail shop. After a busy weekend, the sales team handed you
a list of transactions. However, the data is messy: some entries are correct numbers, but others are strings like
"error" or "missing" where a value should have been recorded.

Your goal is to build a resilient tool that "audits" this list, ignoring the junk data and providing a clean summary of
the total revenue and the average sale price.

**Your tasks are:**

- Create a list of sales values: `[25.50, "error", 40.00, 15.75, "missing", 100.00]`.
- Write a function called `clean_and_sum` that takes a list as an input.
- Inside the function, use a `loop` to iterate through the list. 
- Use `try-except` to skip any value that cannot be converted to a `float`. 
- Calculate the `total sales` and the `average sale` price. 
- Return a dictionary containing the total and the average.

---


> **Final Thoughts**
Congratulations! You have built a basic data-cleaning pipeline. In the professional world, data is rarely perfect.
Using try-except within loops is a standard practice to ensure that one "bad" row of data doesn't crash an entire
multi-hour analysis job. 
> Think about how you could make this script even more useful. Try to answer or implement the following:
> - The Count – can you modify the dictionary to also return the count of items that were successfully processed?
> - The Log – instead of just using continue, can you create a second list called errors that stores the "junk" values
  so you can report them to the sales team later?
> - Logic Check – what would happen to your average calculation if the input list was completely empty?
  (Hint: Review the if len(clean_data) > 0 logic in the sample solution).