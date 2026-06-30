# Word Frequency Analyzer

# Open and read the file
text = input("Enter your text here: ")

# Convert all text to lowercase
text = text.lower()

# Remove punctuation
for char in ".,!?;:()[]{}\"'":
    text = text.replace(char, "")

# Split text into words
words = text.split()

# Count frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Sort words by frequency
sorted_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

# Display results
print("WORD FREQUENCY ANALYZER")
print("-" * 30)

print("Total Words:", len(words))
print("Unique Words:", len(frequency))

print("\nTop 10 Most Common Words:\n")

for word, count in sorted_words[:10]:
    print(word, "-", count)

# Search for a specific word
word = input("\nEnter a word to search: ")

print("Frequency:", frequency.get(word.lower(), 0))
