# Latex Set of Words Highlighter

Script hardcoded, made in python to highlight a set of words  in a latex source file. 
The set of words is listed in the file  "listOfWords.txt" separeted by '\n'.
To do this the script read the .tex file and the "listOfWords.txt" and replace the words with \textit command plus the word.
Actually the output file is named "myfile.tex".

# Usage
  Replace "filename.tex" with the name of your file.
```{r, engine='bash', count_lines}
  python main.py filename.tex
```


# TODO Things

* Refactor code
* Expand hights to bold and colors
* Have a life.
