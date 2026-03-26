# Social Media Data Detective - Lab Explanation

## Bubble Sort Algorithm Explanation

**What is Bubble Sort?**
Bubble Sort is a simple sorting algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.

**How it works in this code:**
1. Start at the beginning of the list
2. Compare the first two elements (tweets by likes)
3. If the first element has fewer likes than the second, swap them
4. Move to the next pair and repeat
5. Continue until the end of the list
6. Repeat the entire process until no swaps are needed

**Why Bubble Sort for this lab:**
- Easy to understand for beginners
- Uses only basic loops and comparisons
- Follows the rule of not using built-in sorting functions
- Demonstrates manual sorting logic

## Code Structure

### 1. Data Loading (`load_data()`)
- Opens CSV file using basic `open()` function
- Reads all lines with `readlines()`
- Skips header row (first line)
- Splits each line by commas
- Handles quoted text that might contain commas
- Stores each tweet as a list: [ID, Username, Text, Likes, Retweets]

### 2. Data Cleaning (`clean_data()`)
- Removes tweets with missing Text
- Replaces missing Likes/Retweets with 0
- Converts Likes and Retweets from strings to integers
- Uses `len()` to check list sizes
- Uses `.append()` to build the cleaned data list

### 3. Finding Maximum Likes (`find_max_likes()`)
- Does NOT use `max()` function (follows rules)
- Starts with first tweet as maximum
- Loops through all tweets manually
- Compares each tweet's likes with current maximum
- Returns tweet with most likes

### 4. Bubble Sort (`bubble_sort_descending()`)
- Implements Bubble Sort algorithm from scratch
- Sorts by likes in descending order (highest first)
- Uses nested loops for comparison and swapping
- Creates a copy to avoid changing original data

### 5. Search Functionality (`search_tweets()`)
- Uses `.append()` to build matches list
- Converts search keyword to lowercase
- Compares with tweet text (also lowercase)
- Returns list of matching tweets

## Key Rules Followed

✅ **NO** `sorted()` function
✅ **NO** `.sort()` method  
✅ **NO** `max()` function
✅ Uses only basic Python: loops, lists, conditionals, functions
✅ Uses `len()` to check list sizes
✅ Uses `.append()` to build new lists
✅ Converts Likes/Retweets to integers before comparison
✅ Clean, beginner-friendly code with comments

## Running the Scripts

### Python Script:
```bash
python data-detective.py
```

### Bash Script (Linux/Mac):
```bash
chmod +x feed-analyzer.sh
./feed-analyzer.sh
```

### Batch Script (Windows):
```cmd
feed-analyzer.bat
```

## Expected Output

The Python script will:
1. Load and clean the data
2. Show the tweet with maximum likes
3. Display top 10 tweets (sorted by Bubble Sort)
4. Ask for a keyword and show matching tweets

The Bash script will:
1. Extract usernames from CSV
2. Count how many times each username appears
3. Show the top 5 most active users
