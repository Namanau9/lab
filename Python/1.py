#1.	Write a python program that accepts a sentence (string of space separated words) from the user. Perform the following task:
#i.	Count the frequency of each word in a string, ignoring the spaces and case
#ii.	For each word, print the word concatenated with itself as many times as it’s frequency (i.e., if a word appears 3 times, print the word 3 times in row)


def word_frequency_and_replication(input_sentence):
         # Convert the input sentence to lowercase and split it into words
    words = input_sentence.lower().split()
        # Create a dictionary to store the frequency of each word
    frequency_dict = {}
          # Count the frequency of each word
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
        # Print each word concatenated with itself according to its frequency
    for word, frequency in frequency_dict.items():
        # Use string concatenation and replication
        replicated_word = word * frequency                      # Replicate the word by its frequency
        print(f"{replicated_word} ({frequency})")                   # Print the replicated word with its frequency

# Input: Accept a sentence from the user
input_sentence = input("Enter a sentence (string of space-separated words): ")

# Call the function to process the input sentence
word_frequency_and_replication(input_sentence)
