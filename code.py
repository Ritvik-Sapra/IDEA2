import json

# Function to convert txt file to json
def json_converter(filename):
    # Creating an empty dictionary
    dict = {}
    firstPass = True
    out_file = open('output.json', 'w')
    with open(filename) as fh:
        # Processing meta data
        for line in fh:
            # Starting of meta data
            if((line == "---\n" and firstPass) or line == '\n'):
                firstPass = False
                continue
            # Ending of meta data
            elif(line == "---\n" and firstPass == False):
                break
            # Spliting the line for obtaining key-value pairs
            key, value = line.strip().split(None, 1)
            # Removing "" from the key
            key = key[:-1]
            if(value[0] == "\""):
                value = value[1:-1]
            if(key == "tags"):
                # Converting 'tags' into list
                value = list(value.split(", "))
            dict[key] = value
        # Meta data completely proccessed
        # Now processing 'short-content'
        for line in fh:
            if(line == '\n'):
                continue
            elif(line == "READMORE\n"):
                break
            dict['short-content'] = line[:-1]
        # Now processing 'content'
        content_str = ""
        for line in fh:
            if(line == '\n'):
                content_str += " "
            else:
                content_str += line[:-1]
        dict['content'] = content_str
    # Writing 'dict' to json file
    json.dump(dict, out_file, indent = 4, sort_keys = False)
    # Closing output file
    out_file.close()

# Main function
def main():
    filename = 'input.txt'
    json_converter(filename)
    print("Converted to JSON successfully!")

# Calling the main() for starting the execution
if __name__ == '__main__': main()
