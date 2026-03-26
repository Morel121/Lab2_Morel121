#!/bin/bash

# Social Media Feed Analyzer
# Bash script to find most active Twitter users

echo "=== Social Media Feed Analyzer ==="
echo

# Check if the CSV file exists
if [ ! -f "twitter_dataset.csv" ]; then
    echo "Error: twitter_dataset.csv not found!"
    exit 1
fi

echo "Analyzing Twitter dataset..."
echo

# Extract usernames from CSV (skip header, get column 2)
echo "Extracting usernames..."
cut -d',' -f2 twitter_dataset.csv | tail -n +2 > usernames.txt

# Count occurrences of each username
echo "Counting user activity..."
echo
echo "=== Top 5 Most Active Users ==="
echo

# Sort usernames, count unique occurrences, sort by count descending, show top 5
sort usernames.txt | uniq -c | sort -nr | head -5 | while read count username; do
    echo "$count tweets - $username"
done

echo
echo "=== Analysis Complete ==="

# Clean up temporary file
rm -f usernames.txt
