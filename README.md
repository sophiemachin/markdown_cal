# Markdown calendars

## Example output

This is a small script to create markdown calendars, for example here is January 2021:

    | M  | T  | W  | T  | F  | S  | S  |
    | -  | -  | -  | -  | -  | -  | -  |
    |    |    |    |    | 1  | 2  | 3  |
    | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
    | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
    | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
    | 25 | 26 | 27 | 28 | 29 | 30 | 31 |


## Usage 

Run the script with

    python2 cal.py

This will print the output in the terminal.

Or to send the output directly to a markdown file, use something like

    python2 cal.py > example_output_file.mdown
    

## Building an html page with Sublime Text 3

Sublime Text 3 has a package called Markdown Preview which will allow you to generate html from your markdown. The generated markdown will look similar to (depending on the flavour of html you choose) 

| M  | T  | W  | T  | F  | S  | S  |
| -  | -  | -  | -  | -  | -  | -  |
|    |    |    |    | 1  | 2  | 3  |
| 4  | 5  | 6  | 7  | 8  | 9  | 10 |
| 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| 25 | 26 | 27 | 28 | 29 | 30 | 31 |
