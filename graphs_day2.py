"""
Given two words (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word, such that:
​
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
​
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
You may not remove or add extra letters
​
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
​
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
​
beginWord = "hungry"
endWord = "happy"
None
"""
​
f = open('words.txt', 'r')
words = f.read().split("\n")
​
all_words = set()
for word in words:
    all_words.add(word.lower())
​
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
​


def get_neighbors(current_word):
    # should return a list of neighbors
    neighbors = []
    # Generate all possible "words" by replacing one letter at a time
    for i in range(len(current_word)):
        for letter in letters:
            temp_word = list(current_word)
            temp_word[i] = letter
            # check if any of those words are valid
            word = "".join(temp_word)
            if current_word != word and (word in all_words):
                neighbors.append(word)


        # if they are valid append to a neighbors list
​
   # return neighbors list
   return neighbors
​
​


def find_path_bfs(start_word, end_word):
    queue = [[start_word]]
    visited = set()


​
   while len(queue) > 0:
        # pop the latest word
        current_path = queue.pop(0)
        current_word = current_path[-1]
​
       if current_word not in visited:
​
           # Compare if the current word is the end_word
           # return the path
           if current_word == end_word:
                return current_path
            visited.add(current_word)
            # get all neighboring words for the current word
            print(f'all neighbors for {current_word}')
            print(get_neighbors(current_word))
            for neighbor_word in get_neighbors(current_word):
                # MAKE A COPY OF THE CURRENT PATH
                current_path_copy = list(current_path)
                current_path_copy.append(neighbor_word)
                queue.append(current_path_copy)
​
print(find_path_bfs('hit', 'cog'))
