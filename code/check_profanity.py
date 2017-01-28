import urllib

def read_text():
    # Open the source file with the movie quotes
    quotes = open('resources/movie_quotes.txt')
    # Read the contents of the file into the buffer
    contenst_of_file = quotes.read()
    # print(contenst_of_file)
    # Close the connection with the file
    quotes.close()
    check_for_profanity(contenst_of_file)

def check_for_profanity(text_to_check):
    connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    # print(output)
    connection.close()

    if "true" in output:
        print "Profanity alert!"
    elif "false" in output:
        print "No curse words found"
    else:
        print "Could not scan the provided output from the call"

read_text()