# ChIP-Seq data similarity search prototype

## Description
This is a solution for the **Intelligent search through public ChIP-Seq data** task, for my JetBrains internship application.   
The web service works this way: You upload a .bed file on the website, the application compares your file with the existing ones in the database and calculates the Jaccard index. It then shows you the best matches based on your data. 

## Requirements:
- Python 3.10+
- Flask
- PyBedTools
- BEDTools

## Usage:
run: flask --app app.py run