# Open the file in read mode
# the Jaccard similarity coefficient

file_ = 'D:\Mozzie\encyclopedia\encyclopedia-comb-mini.txt'

word1 = 'two'
word2 = 'one'


def calculate_similarity(list1, list2):
    # Convert lists to sets to get unique words
    set1 = set(list1)
    set2 = set(list2)

    # Calculate Jaccard similarity coefficient
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    similarity_percentage = (intersection / union) * 100

    #print(similarity_percentage)
    return similarity_percentage



a = 0 # keeping count on the words

# function that compares how similar two words are

word1_arr0 = []
word1_arr1 = []

word2_arr0 = []
word2_arr1 = []

# Open the file with explicit encoding
with open(file_, 'r', encoding='utf-8') as file:
    # Read the content of the file
    content = file.read()

    # Split the content into words
    words = content.split()

    # Print each word
    for word in words:

        word_lower = word.lower()

        # remove extras
        word_lower = word_lower.strip(",") 
        word_lower = word_lower.strip(".") 
        word_lower = word_lower.strip(":") 
        word_lower = word_lower.strip(";") 


        if word == word1:

            word1_arr0.append(words[a-1])
            word1_arr1.append(words[a+1])

        if word == word2:

            word2_arr0.append(words[a-1])
            word2_arr1.append(words[a+1])

            #print(words[a-1], word, words[a+1])


        a += 1




similarity = (calculate_similarity(word1_arr0, word2_arr0) + calculate_similarity(word1_arr1, word2_arr1))/2

print(similarity)


