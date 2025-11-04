# Final-Practice
### Owner: Ashly Sofia Robayo

### Video: https://www.youtube.com/watch?v=Dqvx9GNtqPU&list=PL06RwGLHjQbbVoopJL3LJ_MnXiX4jDjsi&pp=gAQB0gcJCbAEOCosWNin




Its goal is to generate an interactive graphical interface using data parsed by regular expressions.

## 1. Imported Modules:

The program needs two modules from the Python standard library to function.

  1.1. Re: It's the abbreviation for *regular expressions*, patterns used to find a specific combination of characters or symbols.
  
  1.2. tkinter: it's one of the Python's libraries about graphical interfaces, and one of the easiest.

  <img width="177" height="45" alt="image" src="https://github.com/user-attachments/assets/2ad6557f-245e-4197-bc1b-4f311b612f47" />


## 2. The FEN:

The program ask for an input with the FEN to be graphed, after given instructions. We need a process to evaluate if the input has the needed requirements:

  **2.1. The regular expression:** By using the module re, *re.fullmatch()* in specific, we're checking if all the text matches with the pattern  

<img width="420" height="24" alt="image" src="https://github.com/user-attachments/assets/71190458-7416-4408-8f90-cf29952b157d" />

This ensures ensure the FEN only contains valid piece letters, numbers (1-8), and 7 slashes (/). *r''* indicates us the text is a raw.

If the format is wrong, the program stops immediately with exit() and gives and output, on the contrary says it was successfull:

<img width="846" height="100" alt="image" src="https://github.com/user-attachments/assets/2f3f61ec-12c4-4f56-8d42-0889aae1e46e" />

Then, it uses string.split('/'): A built-in string method to break the string into a list.


  **2.2. Large validation:**The program starts a loop through the rows (thanks to the array from the split) to make sure each one has exactly 8 spaces of information.  *def calc_Sum(parts)* Verifies that the sum of pieces ) and empty spaces adds up to 8 for every single row, prints "Correct to the valid ones or shows the error.

  - The first 'if' verifies if the array has 8 elements thanks to len, a Python native function.

  - The valid values are initialized with the array of the sums of each row, then uses enumerate(predefined function) for going through the row, making the sum and define if the sum is minor than 8, equal or bigger than 8 and gives and answer or adds an error. With *.append()*, the sums are added to the array.


<img width="566" height="532" alt="image" src="https://github.com/user-attachments/assets/2fe821c1-3fa4-4fcc-a7da-fbe25bd37558" />


The program collects the errors and gives an output, on the contrary, without errors, just says 'Correct' again.



## 3. The graphic.


The program develops a GUI (Graphical User Interface), Tkinter in this case, to make a chessboard.

**3.1. Creation:** With the root lines, the program creates the window for the graphic and gives it a title.

<img width="218" height="43" alt="image" src="https://github.com/user-attachments/assets/ce46b514-0b7d-4389-9045-59ba41c00ddc" />

Then it makes the measures of the board with canva commands:


<img width="521" height="61" alt="image" src="https://github.com/user-attachments/assets/828af9f1-9c66-4bda-9fc1-cdd8b792e825" />



**3.2. The design:** The program avoids the rows and columns to be more than 8 in a loop, then chosses the colors of the cells with hex code, calculates the ends and then makes a rectangle to complete the board:


<img width="594" height="183" alt="image" src="https://github.com/user-attachments/assets/5a57d66f-ee19-42f6-a761-33b0e69d459a" />

After that, creates the conversion ot the fen string to the images of the chess pieces in Unicode symbols:

<img width="573" height="87" alt="image" src="https://github.com/user-attachments/assets/b958cf1b-ff7f-45b6-b440-9c2667fdaab1" />


**3.3. Draw_fen:**The program goes through each character of the rows of the FEN, identifies blank spaces and pieces, and ubicates them in the center of the cell with a canvas function.


<img width="914" height="241" alt="image" src="https://github.com/user-attachments/assets/64ee6b43-ad6f-4606-8e86-3c02a7c470ad" />

**3.4. Interactive:**The program inserts a button for update the chess.


<img width="483" height="348" alt="image" src="https://github.com/user-attachments/assets/56711648-54be-47b5-b428-899d919a0706" />























  
