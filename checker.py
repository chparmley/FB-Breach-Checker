
class Database_Search():

    def __init__(self):
        self.search_data = ''
        self.line_number = 0
        self.list_of_results =[]

        self.file_list = ['USA01.txt', 'USA02.txt', 'USA03.txt', 
        'USA04.txt', 'USA05.txt', 'USA06.txt', 
        'USA07.txt', 'USA08.txt']

        print('\n\n---------------------------')
        print('  Facebook Breech Checker')
        print('---------------------------\n')

        self.search_data = input('Enter First Name:\n\n\n')


    def search_string_in_file(self):
        """Search for the given string in file and return lines containing that string,
        along with line numbers"""
        line_number = 0
        # Open the file in read only mode
        with open(self.file_name, 'r') as open_file:
            # Read all lines in the file one by one
            for line in open_file:
                # For each line, check if line contains the string
                line_number += 1
                if self.search_data in line:
                    # If yes, then add the line number & line as a tuple in the list
                    print(self.file_name)
                    print(line)
                    self.list_of_results.append(line)
    
        # Return list of tuples containing line numbers and lines where string is found
        return self.list_of_results


    def refine_search(self):
        self.refine_search_word = input('\nEnter Last Name: ')
        print('----------------')
        for result in self.list_of_results:
            # For each line, check if line contains the string
            if self.refine_search_word in result:
                # If yes, then add the line number & line as a tuple in the list
                print(result)


    def run(self):
        for self.file_name in self.file_list:
            self.search_string_in_file()
        self.refine_search()

Database_Search().run()

