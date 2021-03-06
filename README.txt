CS 6200 INFORMATION RETRIEVAL Fall '17'
Assignment 1 

Submitted By : Srijit Ravishankar
NUID : 001282238

SUMMARY :
		** The given instructions contains software installations and running the program that is suitable in MAC environment ** 

This file consists procedures to follow to run the following programs:
1. Task 1 : A python file implementing a basic web crawler, starting with the SEED : "https://en.wikipedia.org/wiki/Tropical_cyclone".
2. Task 2 : A python file implementing focused crawler, starting with the SEED : "https://en.wikipedia.org/wiki/Tropical_cyclone" and KEYWORD : "rain".

GENERAL INSTRUCTIONS :
1. Install Python v.3.6.1
2. Open Terminal and install BeautifulSoup by using the command 'pip install beautifulsoup4'

INSTRUCTIONS TO RUN THE PROGRAM : 
1. Open Terminal
2. Navigate to the desired directory
3. Enter the command "python <file_name>.py"


RESULTS AND INTERPRETATIONS :

TASK 1 :
1. Task 1 generates a file ‘crawledURLs.txt’ which lists all the unique URLs crawled, starting with the SEED : "https://en.wikipedia.org/wiki/Tropical_cyclone".
2. The generated file is created in the same directory as the program.
3. The maximum depth that Task 1 crawls is : 3

TASK 2 :
1. Task 2 generates a file ‘focusedCrawledURLs.txt’ which lists all the unique URLs crawled, starting with the same SEED as above and having the KEYWORD : "rain" and its variations.
2. The generated file is created in the same directory as the program.
3. The maximum depth that Task 2 crawls is : 4
