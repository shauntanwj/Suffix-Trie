# Question 1: DNA Fragments
class Node:
    
    """
    This class is to create a Node for the Trie data structure.
    It have only 1 function that is the constructor of the class __init__.
    Each Node contains payload of link, frequency, word, and fakelink.
    link: a list of size 5 where each index for each letter, index 0 = terminal, index 1 = A, index 2 = B, index 3 = C, index 4 = D
    frequency: the total number of time the word added to the Trie
    word: the word which inserted into the Trie
    fakelink: a reference to a node 
    """
    
    def __init__(self, frequency = None, word = None, fakelink=None, size=5):
        
        """
        Input: frequency, word, fakelink, size
        Output: a Node with all the input variable
        
        Time Complexity: O(1)
        Space Complexity: O(N) where N is the size of the payload
        Auxiliary Space Complexity: O(1)
        """

        self.link = [None] * size

        self.frequency = frequency
        
        self.word = word
        
        self.fakelink = fakelink
        
class Trie:
    
    """
    This class is to create a Trie data structure
    This class have a total of 4 method, constructor, insert_recur, insert_recur_aux and search.
    Each Trie will have a root which is a Node. 
    """
    
    def __init__(self):
        
        """
        This constructor will create a variable root and assign it to a new Node
        
        Time Complexity: O(1) creating the Node()
        Space Complexity: O(N) where N size of the payload in the Node
        Auxiliary Space Complexity: O(1)
        """
        
        self.root = Node()
     
    def insert_recur(self, key):
        
        """
        Input: a single nonempty string of uppercase letters [A-D]
        Output: Inserting the string into the Trie
        
        This function inserts a string into the Trie starting from the root. 
        This function calls insert_recur_aux to start the recursion. This will be explained below.
        The root will store the reference to the Node which has the word with the highest frequency. 
        
        Time Complexity: O(N) where N is the length of the key
        Space Complexity: O(N) where N is the length of the key
        """
        

        current = self.root  
        previous_node = self.insert_recur_aux(current, key)
        
        # check the root frequency and compare it with the previous node frequency 
        if current.frequency is None:       
            current.frequency = previous_node.frequency
            current.fakelink = previous_node.fakelink
        elif previous_node.frequency > current.frequency:
            current.frequency = previous_node.frequency
            current.fakelink = previous_node.fakelink
        elif previous_node.frequency == current.frequency:
            if previous_node.fakelink.word < current.fakelink.word:
                current.frequency = previous_node.frequency
                current.fakelink = previous_node.fakelink
        
    def insert_recur_aux(self, current, key, frequency=None, i=0):
        
        """
        Input: current points to the current Node, key is the string/word, i is a pointer which point to each letter of the word
        Output: Insert the key to the Trie
        
        This function will first check if i is 0, if i is 0 means it has reach the last letter of the word then it will create a Terminal Node with
        the appropriate payload. 
        
        Base case: i equals to length of the key
        Recursive case: get the index of the letter and then check if there's Node for the letter, if there is the point to the Node and go to the 
                        next letter, if not create a new Node and point to that new Node and go to the next letter. 
                        
        Time Complexity: O(N) where N is the size of the word
        Space Complexity: O(M) where M is the size of the payload 
        """    

        # base case
        # check if i equals length of the key
        # terminal node
        if i == len(key):
            index = 0
            # if the terminal Node exist 
            if current.link[index] is not None:
                current = current.link[index]
                current.frequency += 1
            # if terminal node does not exist
            else:
                current.link[index] = Node(frequency=1, word=key)
                current = current.link[index]
                current.fakelink = current
            return(current)

        # recursive case
        else:
            # get the index
            index = ord(key[i]) - 65 + 1
            
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
                i+=1
                previous_node = self.insert_recur_aux(current, key, frequency, i)
                
                if previous_node.frequency > current.frequency:
                    current.frequency = previous_node.frequency
                    current.fakelink = previous_node.fakelink
                elif previous_node.frequency == current.frequency:
                    if previous_node.fakelink.word < current.fakelink.word:
                        current.frequency = previous_node.frequency
                        current.fakelink = previous_node.fakelink
                return(current)
                
            # if path doesnt exits
            else:
                current.link[index] = Node()
                current = current.link[index]
                i+=1
                previous_node = self.insert_recur_aux(current, key, frequency, i)
                if current.frequency is None:
                    current.frequency = previous_node.frequency
                    current.fakelink = previous_node.fakelink
                return(current)
            
    def search(self, key):
        
        """
        Input: a single string with only uppercase [A-D]
        Output: the word of with key as the prefix and have the highest frequency in the database of words with key as prefix
        
        This function will loop through each of the letter in the string and check if there's a Node of that letter, then go until the last 
        letter and get the reference node and then get the word of the referenced node. 
        If the length of the key is 0 (empty list) the function will return the root's reference node and get the word, if there's nothing 
        then it will return None. 
        
        Time Complexity: O(N) where N is the length of the string
        Space Complexity: O(N) where N is the length of the string
        """
        
        # begin from the root
        current = self.root

        # get the root's referenced node key if input is empty 
        try:
            if len(key) == 0:
                return(current.fakelink.word)
        except AttributeError as e:
            return None
        
        #go through each letter of the key
        for char in key:
            # calculate index
            index = ord(char) - 65 + 1
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
                
            # if path doesnt exits
            else:
                return None
        return(current.fakelink.word)

class SequenceDatabase():
    
    """
    This class creates a SequenceDatabase object. It have a total of 3 methods, constructor, addSequence and query.
    Each object of SequenceDatabase will have a db variable which is a empty Trie.
    addSeqeunce is to add a word into the db (database)
    query will return the word in the database with the input parameter as prefix,
    """
    
    def __init__(self):
        
        """
        This constructor creates a Trie object and assign it to the db variable. 
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        self.db = Trie()
    
    def addSequence(self, s):
        
        """
        Input: s, a string with only [A-D]
        Output: insert s into the database
        
        This function will use the Trie method, insert_recur to insert the string into the database
        
        Time Complexity: O(N) where N is the length of the string
        Space Complexity: O(N) where N is the length of the string
        """
        
        self.db.insert_recur(s)
    
    def query(self, q):
        
        """
        Input: q, a string with only [A-D]
        Output: the word of with q as the prefix and have the highest frequency in the database of words with q as prefix
        
        This function calls the Trie method, search() to return the word with q as 
        the prefix and have the highest frequency in the database of words with q as prefix.
        
        Time Complexity: O(N) where N is the length of the string
        Space Complexity: O(N) where N is the length of the string 
        """
        
        return self.db.search(q)
        

# Question 2: Open reading frames
class Suffix_Node:
    
    """
    This class creates a Node for the Suffix Trie,
    Each Node has a payload of link, start_index and start_fakelink
    
    link: a list of size 5 where each index for each letter, 
          index 0 = terminal, index 1 = A, index 2 = B, index 3 = C, index 4 = D  
    start_index: the index of the first letter of the key
    start_fakelink: a list of reference to the Node
    
    Time Complexity: O(1)
    Space Complexity: O(N) where N is the size of the payload
    Auxiliary Space Complexity: O(1)
    """
    
    def __init__(self, word = None, start_fakelink=[], start_index = None, size=5):

        self.link = [None] * size
        
        self.start_index = start_index
        
        self.start_fakelink = start_fakelink
        
class Suffix_Trie:
    
    """
    This class creates a Suffix Trie for a given string.
    It contains 4 function constructor, suffix_insert_recur, suffix_insert_recur_aux and start_search
    Each Suffix Trie will contain a root which is a Suffix Node.
    """
    
    def __init__(self):
        
        """
        This function creates a variable root and assign it to a new Suffix Node
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        self.root = Suffix_Node(start_fakelink=[])
     
    def suffix_insert_recur(self, key): 
         
        """
        Input: a single non-empty string consisting only uppercase [A-D]
        Output: insert the string to the Suffix Trie
        
        This function loops through the key/string from index 1 until the length of the list + 2.
        For each iteration of the loop it will call suffix_insert_recur_aux to do the recursion. This will be explained below.
        For each key, "#" will be added to the start of the list to indicate the start of the string.
        For example, if a string "ABCD" is the parameter for the function then it will be modify to "#ABCD"
        
        Time Complexity: O(N^2) where N is the length of the key/string
        Space Complexity: O(N) where N is the length of the key/string
        """
        
        # add the character "#" to front of the key
        key = "#" + key
        
        # loop from the start of the key
        for start in range(1, len(key)):
            current = self.root
            self.suffix_insert_recur_aux(current, key=key, i = start, start_index = start)     
    
    def suffix_insert_recur_aux(self, current, key, i=0, start_index = 0):
        
        """
        This function gets the each of the letter from the string using pointer i and check if there's Suffix Node for the letter, if there's no
        Suffix Node for the letter than a new Suffix Node will be created and add all the appropriate payload for the Node. This function will
        be called resursively until pointer i equals to the length of the key minus 1 which means it reach the end of the string.
        
        Parameter: 
        1. current: points to the current Suffix Node
        2. key: the string/word
        3. i: pointers for the string
        4. start_index: the start index of the string/word
        
        Base Case: when i equals to length of the key minus 1, then it reach the end of string and create a terminal Node for it
        Recursive Case: get the index of the letter and check if there's a existing path/Node for the letter, if there is, then current 
                        will go to the existing Node and i + 1 and go to the next letter. If there's no path/Node existed, create a new Suffix Node
                        and currrent then equals to the new Suffix Node and i + 1 and go to the next letter. After the recursion, the start_index of
                        current node will be equals to the previous node start_index and will also append the last fakelink/reference that is added 
                        to the previous node. 
                        
        Time Complexity: O(N) where N is the length of the key/string
        Space Complexity: O(N) where N is the length of the key/string
        """
        
        # base case
        # check if i equals length of the key minus 1
        # terminal node
        if i == len(key)-1:
            index = 0
            current.link[index] = Suffix_Node(start_fakelink=[])
            current = current.link[index]
            current.start_index = start_index
            current.start_fakelink.append(start_index)
            return(current)

        # recursive case
        else:
            # get the index of the current letter
            index = ord(key[i]) - 65 + 1
            
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
                i+=1
                previous_node = self.suffix_insert_recur_aux(current, key, i, start_index=start_index)
                current.start_index = previous_node.start_index
                current.start_fakelink.append(previous_node.start_fakelink[-1])
                return(current)
                
            # if path doesnt exits
            else:
                current.link[index] = Suffix_Node(start_fakelink=[])
                current = current.link[index]
                i+=1
                previous_node = self.suffix_insert_recur_aux(current, key, i, start_index=start_index)
                current.start_index = previous_node.start_index
                current.start_fakelink.append(previous_node.start_fakelink[-1])
                return(current)
     
    def start_search(self, key):
        
        """
        This function will search the key/string in the Suffix Trie and then it will return a list of all the start_index.
        For example, start_search("A"), the function will return a list of index of the letter "A"
        If there's no such string/key in the Suffix Trie then a empty list will be return.
        
        Time Complexity: O(N) where N is the length of the key/string
        Space Complexity: O(N) where N is the length of the key/string
        Auxiliary Space Complexity: O(1)
        """
        
        # begin from the root
        current = self.root
        out = []
        #go through the key 1 by 1
        for char in key:
            # calculate index
            index = ord(char) - 65 + 1
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
                
            # if path doesnt exits return empty list
            else:
                return out
        return current.start_fakelink
    
class Prefix_Node:
    def __init__(self, word = None, end_fakelink=[], end_index = None, size=5):
        
        """
        This class creates a Node for the Prefix Trie,
        Each Node has a payload of link, end_index and end_fakelink
    
        link: a list of size 5 where each index for each letter, 
              index 0 = terminal, index 1 = A, index 2 = B, index 3 = C, index 4 = D  
        end_index: the index of the last letter of the key
        end_fakelink: a list of reference to the Node
        
        Time Complexity: O(1)
        Space Complexity: O(N) where N is the size of the payload
        Auxiliary Space Complexity: O(1)
        """
        
        self.link = [None] * size
        
        self.end_index = end_index
        
        self.end_fakelink = end_fakelink
        
class Prefix_Trie:
    
    """
    This class creates a Prefix Trie for a given string.
    It contains 4 function constructor, prefix_insert_recur, prefix_insert_recur_aux and end_search
    Each Prefix Trie will contain a root which is a Prefix Node.
    """
    
    def __init__(self):
        
        """
        This function creates a variable root and assign it to a new Prefix Node
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        self.root = Prefix_Node(end_fakelink=[])
     
    def prefix_insert_recur(self, key):  
        
        """
        Input: a single non-empty string consisting only uppercase [A-D]
        Output: insert the string to the Prefix Trie
        
        This function loops through the key/string from the last character in the string until the first letter of the string
        For each iteration of the loop it will call prefix_insert_recur_aux to do the recursion. This will be explained below.
        However, this function will insert the each prefix of the word from the last letter until the first letter, it's
        not inserting the prefixes from the first letter to the last letter. That is why the loop starts from the last letter. 
        For each key, "#" will be added to the start of the list to indicate the start of the string.
        For example, if a string "ABCD" is the parameter for the function then it will be modify to "#ABCD"
        
        Time Complexity: O(N^2) where N is the length of the key/string
        Space Complexity: O(N) where N is the length of the key/string
        """
        
        # add the character "#" to the front of the key
        key = "#" + key
        
        # loop from the back of the key/string
        for start in range(len(key)-1, -1, -1):
            current = self.root
            self.prefix_insert_recur_aux(current, key=key, i = start, end_index = start)     
    
    def prefix_insert_recur_aux(self, current, key, i=0, end_index = 0):
        
        """
        This function gets the each of the letter from the string using pointer i and check if there's Prefix Node for the letter, if there's no
        Prefix Node for the letter than a new Prefix Node will be created and add all the appropriate payload for the Node. 
        This function will be called resursively until pointer i equals to 0 which means it reach the first letter of the string.
        
        Parameter: 
        1. current: points to the current Prefix Node
        2. key: the string/word
        3. i: pointers for the string
        4. end_index: the end index of the string/word
        
        Base Case: when i equals to 0, then it reach the first letter of the string and create a terminal Node for it
        Recursive Case: get the index of the letter and check if there's a existing path/Node for the letter, if there is, then current 
                        will go to the existing Node and i + 1 and go to the next letter. If there's no path/Node existed, create a new Prefix Node
                        and currrent then equals to the new Prefix Node and i + 1 and go to the next letter. After the recursion, the end_index of
                        current node will be equals to the previous node end_index and will also append the last fakelink/reference that is added 
                        to the previous node. 
                        
        Time Complexity: O(N) where N is the length of the key/string
        Space Complexity: O(N) where N is the length of the key/string
        """
        
        # base case
        # check if i equals 0
        # terminal node
        if i == 0:
            index = 0
            current.link[index] = Prefix_Node(end_fakelink=[])
            current = current.link[index]
            current.end_index = end_index
            current.end_fakelink.append(end_index)
            return(current)

        # recursive case
        else:
            index = ord(key[i]) - 65 + 1
            
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
                i-=1
                previous_node = self.prefix_insert_recur_aux(current, key, i, end_index=end_index)
                current.end_index = previous_node.end_index
                current.end_fakelink.append(previous_node.end_fakelink[-1])
                return(current)
                
            # if path doesnt exits
            else:
                current.link[index] = Prefix_Node(end_fakelink=[])
                current = current.link[index]
                i-=1
                previous_node = self.prefix_insert_recur_aux(current, key, i, end_index=end_index)
                current.end_index = previous_node.end_index
                current.end_fakelink.append(previous_node.end_fakelink[-1])
                return(current)
            
    def end_search(self, key):
        
        """
        This function will search the key/string in the Prefix Trie starting from the last letter of the key till the first letter
        and then it will return a list of all the end_index.
        For example, end_search("ABC"), it will looop from C -> B -> A, and check if there's a existing path. If there is then go to the next letter.
        If there's no such string/key in the Prefix Trie then a empty list will be return.
        
        Time Complexity: O(N) where N is the length of the key/string
        Space Complexity: O(N) where N is the length of the key/string
        """
        
        # begin from the root
        current = self.root
        out = []
        #go through the key 1 by 1 from the back
        for i in range(len(key)-1, -1,-1):
            # calculate index
            char = key[i]
            index = ord(char) - 65 + 1
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
                
            # if path doesnt exits
            else:
                return out
            
        return current.end_fakelink
    
class OrfFinder:
    
    """
    This class have 2 methods, constructor and find(). 
    The constructor of this class acceps a single non-empty string consisting of uppercase [A-D].
    Then for each object of the class, it will have a Suffix Trie and Prefix Trie.
    """
    
    def __init__(self, genome):
        
        """
        Input: a single non-empty string consisting of uppercase [A-D]
        
        This constructor will create a Suffix Trie and Prefix Trie and insert the string to both Suffix and Prefix Trie.
        
        Time Complexity: O(N^2) where N is the length of the string
        Space Complexity: O(N) where N is the length of the string
        """
        
        self.genome = genome
        self.suffix_trie = Suffix_Trie()
        self.suffix_trie.suffix_insert_recur(genome)
        self.prefix_tire = Prefix_Trie()
        self.prefix_tire.prefix_insert_recur(genome)
 
    def find(self, start, end):
        
        """
        Input: start and end are each a single non-empty string consisting of uppercase [A-D]
        Output: returns a list of strings with all the substrings which have start as prefix and end as suffix, with 
                start and end not overlap
                
        This function calls the start_search function in Suffix Trie to get all the indexes of the word with start as prefix
        And also the function calls end_seacrh function in Prefix Trie to get all the indexes of the word with end as suffix
        Then loop the both start list and end list, if the index in end list minus the index in start list is smaller then the length 
        of the start and end added together, that means there's overlap, else it will then slice the genome with the start index and
        end index and add it into the out_list and return it
        
        Time Complexity: O(len(start) + len(end) + U) where U is the number of characters in the output list
        Space Complexity: O(len(start + len(end))
        Auxiliary Space Complexity: O(U) where U is the number of characters in the output list
        """
        
        start_list = self.suffix_trie.start_search(start)
        end_list = self.prefix_tire.end_search(end)
        least_sub_length = len(start + end)
        out_list = []
    
        for start in start_list:
            for end in end_list:
                if abs(end-start) + 1 >= least_sub_length and start<end:     # check if the string is overlapped
                    w = self.genome[start-1:end]
                    out_list.append(w)     
        return(out_list)
            
