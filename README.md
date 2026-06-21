# PDF-Analysis
A simple code for the 'text analysis' of a given PDF file.


**Text analysis**, also known as text mining or text analytics, refers to the process of extracting meaningful information and insights from textual data. This is useful for, let's consider a real-life scenario where we are analyzing customer feedback for a product. We have a large data set of customer reviews in the form of strings, and we want to extract useful information from them.

## Goals
We will use a PDF file to extract the text. In general, we could use any file format. Goal is finding:
1. Frequency of all words in a given string
2. Frequency of a specific word

## Workflow
The process involves **four** steps: <br>
**i**. Extracting the text from the PDF file as a string <br>
<br>
**ii**. Remove all punctuation marks, special characters, etc., and convert all the text to lowercase. This helps standardize the text and allows you to focus on the content rather than the specific letter casing.<br>
<br>
**iii**. Using the .count() function and a dictionary to display the frequency of all the words. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.<br>
<br>
**iv**. Using the frequency dictionary from step iii to track the frequency of a particular word. This is relevant for our analysis, as we might be interested in monitoring how often the word "reliable" appears in customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, we can gain a deeper understanding of customer opinions or preferences related to that particular aspect.

### Attribution
This project was inspired from an IBM Skills Network course. Code implementations and analysis are my own work completed as part of portfolio development.




