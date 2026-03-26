# Social Media Data Detective
# Year 1 Python Lab - Complete Solution
# Rules: No sorted(), no .sort(), no max() - only basic Python

def load_data(filename):
    """Load CSV data into a list of lists"""
    data = []
    
    try:
        # Open the CSV file
        file = open(filename, 'r')
        
        # Read all lines
        lines = file.readlines()
        
        # Skip header row (first line) and process the rest
        for i in range(1, len(lines)):
            line = lines[i].strip()
            
            # Split by comma (simple CSV parsing)
            parts = line.split(',')
            
            # Handle quoted text (if text contains commas)
            if len(parts) > 5:
                # Reconstruct text if it was split
                text_parts = []
                for j in range(2, len(parts) - 1):
                    text_parts.append(parts[j])
                text = ','.join(text_parts)
                row = [parts[0], parts[1], text, parts[-2], parts[-1]]
            else:
                row = parts
            
            data.append(row)
        
        file.close()
        print(f"Loaded {len(data)} tweets from {filename}")
        
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return data

def clean_data(data):
    """Clean the dataset following lab requirements"""
    cleaned_data = []
    removed_count = 0
    fixed_count = 0
    
    # Loop through all tweets
    for tweet in data:
        # Check if we have enough columns
        if len(tweet) < 5:
            removed_count += 1
            continue
        
        tweet_id = tweet[0]
        username = tweet[1]
        text = tweet[2]
        likes = tweet[3]
        retweets = tweet[4]
        
        # Remove tweets with missing Text
        if not text or text.strip() == '' or text == '""':
            removed_count += 1
            continue
        
        # Fix missing Likes - replace with 0
        if not likes or likes.strip() == '' or likes == '""':
            likes = "0"
            fixed_count += 1
        
        # Fix missing Retweets - replace with 0
        if not retweets or retweets.strip() == '' or retweets == '""':
            retweets = "0"
            fixed_count += 1
        
        # Convert Likes to integer
        try:
            likes = int(likes)
        except ValueError:
            likes = 0
            fixed_count += 1
        
        # Convert Retweets to integer
        try:
            retweets = int(retweets)
        except ValueError:
            retweets = 0
            fixed_count += 1
        
        # Create cleaned tweet as list
        cleaned_tweet = [tweet_id, username, text, likes, retweets]
        cleaned_data.append(cleaned_tweet)
    
    print(f"Data cleaning complete:")
    print(f"- Removed {removed_count} rows with missing Text")
    print(f"- Fixed {fixed_count} missing Likes/Retweets values")
    print(f"- Remaining rows: {len(cleaned_data)}")
    
    return cleaned_data

def find_max_likes(data):
    """Find tweet with most likes without using max()"""
    if len(data) == 0:
        return None
    
    # Start with first tweet as maximum
    max_tweet = data[0]
    max_likes = data[0][3]  # Likes is at index 3
    
    # Loop through remaining tweets
    for i in range(1, len(data)):
        current_likes = data[i][3]
        
        # Compare manually
        if current_likes > max_likes:
            max_likes = current_likes
            max_tweet = data[i]
    
    return max_tweet

def bubble_sort_descending(data):
    """Sort tweets by likes in descending order using Bubble Sort"""
    # Create a copy to avoid changing original data
    sorted_data = []
    for tweet in data:
        sorted_data.append(tweet.copy())
    
    n = len(sorted_data)
    
    # Bubble Sort algorithm
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Compare likes (index 3)
            if sorted_data[j][3] < sorted_data[j + 1][3]:
                # Swap elements
                temp = sorted_data[j]
                sorted_data[j] = sorted_data[j + 1]
                sorted_data[j + 1] = temp
    
    return sorted_data

def search_tweets(data, keyword):
    """Search for tweets containing keyword using .append()"""
    matches = []
    keyword_lower = keyword.lower()
    
    # Loop through all tweets
    for tweet in data:
        text = tweet[2]  # Text is at index 2
        text_lower = text.lower()
        
        # Check if keyword is in text
        if keyword_lower in text_lower:
            # Use .append() to add to matches list
            matches.append(tweet)
    
    return matches

def print_tweet(tweet, show_index=None):
    """Print a tweet in formatted way"""
    if show_index is not None:
        print(f"{show_index + 1}. ", end="")
    
    tweet_id = tweet[0]
    username = tweet[1]
    text = tweet[2]
    likes = tweet[3]
    retweets = tweet[4]
    
    print(f"ID: {tweet_id}")
    print(f"   Username: {username}")
    print(f"   Likes: {likes}")
    print(f"   Retweets: {retweets}")
    print(f"   Text: {text}")
    print()

def main():
    """Main function to run the Social Media Data Detective"""
    print("=== Social Media Data Detective ===")
    print("Year 1 Python Lab - Complete Solution")
    print()
    
    # Task 1: Load Data
    filename = "twitter_dataset.csv"
    data = load_data(filename)
    
    if len(data) == 0:
        print("No data to process. Please check your CSV file.")
        return
    
    print()
    
    # Task 2: Data Cleaning
    cleaned_data = clean_data(data)
    
    if len(cleaned_data) == 0:
        print("No valid data after cleaning.")
        return
    
    print()
    
    # Task 3: Find Maximum Likes
    print("=== Tweet with Maximum Likes ===")
    max_tweet = find_max_likes(cleaned_data)
    if max_tweet:
        print_tweet(max_tweet)
    else:
        print("No tweets found.")
    print()
    
    # Task 4: Custom Sorting (Bubble Sort)
    print("=== Top 10 Tweets by Likes (Bubble Sort) ===")
    sorted_tweets = bubble_sort_descending(cleaned_data)
    
    # Get top 10 using len() check
    top_count = 10
    if len(sorted_tweets) < 10:
        top_count = len(sorted_tweets)
    
    for i in range(top_count):
        print_tweet(sorted_tweets[i], i)
    print()
    
    # Task 5: Search Functionality
    print("=== Search Tweets ===")
    keyword = input("Enter a keyword to search for: ")
    
    if keyword.strip():
        matches = search_tweets(cleaned_data, keyword)
        print(f"\nFound {len(matches)} tweets containing '{keyword}':")
        print()
        
        # Print all matches using .append() was used in search function
        for i in range(len(matches)):
            print_tweet(matches[i], i)
        
        if len(matches) == 0:
            print("No matching tweets found.")
    else:
        print("No keyword entered.")
    
    print("\n=== Analysis Complete ===")
    print("All tasks completed successfully!")

# Run the main function
if __name__ == "__main__":
    main()
