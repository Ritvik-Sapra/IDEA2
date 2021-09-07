# Problem Statement

We are given a text file 'input.txt' in which there is information about some blog. Every data entry has some meta data about the blog and also some additional information.

We have to make a JSON object out of this information and write it in a new file.

Check out the complete problem statement [here](https://hackmd.io/@N7nxXdBFSk6_7dihdnv-xg/SywqoqyJE?type=view).

# Solution

The code takes the input from the file calles 'input.txt' and creates a new file 'output.json' in which the JSON object from the text file is created and writen to.

## Approach

For solving this problem, we observe that meta data is marked by "---" on the starting and ending. Also, the "short-content" and "content" are seperated by the line "READMORE".

Therefore, we make use of these information and ignore any newline characters in the input line. We read the input line by line and firt process the meta data.

Once meta data is complete, we read line by line until "READMRE\n" is encountered. This is our "short-content". Whatever is left after this is our "content".

## Implementation

For solving this problem, Python is chosen. Python has in-built support for 'json'. We simply have to write "import json". 
Moreover, Python has Dictionary Data structure which is the closest representation of JSON object.

C++ does not have in-built library for converting data structures into JSON and also available data structures are hash map and tree map. 
In both the data structures there is a chance that the keys given in text file can be shuffled in the output JSON file, whereas Python's dictionary will keep the order of the keys
in text and JSON file exactly the same.

The code is writen as per the approach discussed above. We first create appropriate dictionary just like we want our JSON object to be. We do this by spliting every read line.

Then we use json.dump() to convert that dictionary into JSON object.

# Analysis of code

The time required by the code is directly related to how many lines does input file contains. The function json_converter() takes a parameter of the input filename and creates
a dictionary. It also creates a file and converts this dictionary into a JSON format. All of this requires constant operations. 

We also have to create a dictionary and output file which is directly related to the no. of lines in input text file.

Let input text file conatin "n" lines, then:

* **Time Complexity: O(n)**

* **Space Complexity: O(n)**

If we had used C++ map then an extra O(log k) time would be added where k is the no. of keys for sorting the keys in ascending order. This is also a reason why Python was a
better choice for solving this solution.
