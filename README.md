# Markdown calendars

## Example output

This is a small script to create [markdown](https://daringfireball.net/projects/markdown/) calendars, for example here is January 2021:

    ### January 2021

    | M  | T  | W  | T  | F  | S  | S  |
    | --:| --:| --:| --:| --:| --:| --:|
    |    |    |    |    |  1 |  2 |  3 |
    |  4 |  5 |  6 |  7 |  8 |  9 | 10 |
    | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
    | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
    | 25 | 26 | 27 | 28 | 29 | 30 | 31 |

This is a standard markdown table with the default head options. The month label is a level 3 heading. The columns are right aligned. 


## Usage 

Run the script with

    python2 cal.py

This will print the current month as a markdown calendar, in the terminal.

To send the output directly to a markdown file, use something like

    python2 cal.py > example_output_file.mdown

### Options

To run a whole year instead of just a single month:

    python2 cal.py --whole_year
    
To run a different year to the current year (this will run on whatever month we are on now, but for the specified year):

    python2 cal.py --year=1987

To run a different month to the current month, for example March of the current year:

    python2 cal.py --month=3
    
To run a different month AND year:

    python2 cal.py --year=1987 --month=3

 
## Building an html page with Sublime Text 3

[Sublime Text 3](https://www.sublimetext.com/3) has a package called [Markdown Preview](https://packagecontrol.io/packages/MarkdownPreview) which will allow you to generate html from your markdown. The generated markdown will look similar to this (depending on the flavour of html you choose)

### January 2021

| M  | T  | W  | T  | F  | S  | S  |
| --:| --:| --:| --:| --:| --:| --:|
|    |    |    |    |  1 |  2 |  3 |
|  4 |  5 |  6 |  7 |  8 |  9 | 10 |
| 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| 25 | 26 | 27 | 28 | 29 | 30 | 31 |


### Usage

#### With Markdown Preview installed

1. Pipe the output to a file

        python2 cal.py > example_output_file.mdown

2. Open the file in Sublime Text 3 and type markdown into the Command Palette (Tools > Command Palette). 

3. Select Markdown Preview: Save to html. Choose which styling you want, I usually stick with github. 

4. This will generate a file with the same name and a .html extension. 


#### Without Markdown Preview installed

1. Make sure Sublime Text 3 has the package manager available:

  Tools > Install Package Control

2. Then open the Command Palette and type install, and select Package Control: Install Package using the arrow keys and then press return. 

3. When the Package Control Manager is open, type Markdown Preview, select and press return. The package will be installed. 

4. To use the package and generate the html, type open the Command Pallette and type markdown, and select Markdown Preview: Save to html. 

5. This will generate a file with the same name and a .html extension in the same folder that the source file is in. 
