## PlagCheck Usage Guide
> Derived from [Reading the Results](http://moss.stanford.edu/general/format.html).

*PlagCheck* returns the following list of dictionaries:
```json
[
  {
    "file1":"filename1.py",
    "file2":"filename2.py",
    "percentage":"34",
    "lines_matched":[["2-3", "10-11"]],
    "date":"2019-10-03",
    "time":"05:48:01",
    "url":"https://mossresults/..."
  },
....
]
```
Each dict item contains the following items:

- **file1** & **file2** : 
The pair of file names that have similar code.

- **percentage** : 
It is the the percentage of the code in one file considered to match code in the other file.

- **lines_matched** : 
  Lines Matched is approximately the number of lines of code that matched between 2 given files.

  For example :
  If ***lines_matched* is [['88-99','119-131']]**
  
  Then the line numbers 88-99 of *file1* matched with lines 119-131 of *file2*.

  lines_matched is a list of lists indicating all line number matches between 2 code files.


> For both measures(*lines_matched* & *percentage*), higher numbers mean more code matches.

4. **date** & **time** : 
Date and Time of the submission of files to MOSS server. The Timezone is currently PDT.

5. **url** : 
The homepage link of the results for each submission to MOSS.


## [Tips](http://moss.stanford.edu/general/tips.html)

- Moss is quite conservative about what it considers to be matching passages of code. If Moss says that two passages look alike, then they almost certainly look quite alike. Moss also excludes all code that appears in too many of the submitted programs. Thus, all matches reported by Moss fairly accurately approximate the signature of plagiarized code: a passage of similar code in two programs that does not also appear in very many other programs.

- False positives are possible with Moss, as programs may legitimately share code (e.g., two programs making use of the same public-domain library). The higher-ranked pairs are more likely to be the result of plagiarism than the lower-ranked pairs. The recommended strategy is to start with the highest-ranked pair and work down the list until one finds that a large fraction of the reported matches are false positives.

- Moss can be more accurate if a base file is supplied. The -b option to Moss supplies a base file of code that should be ignored if it appears in programs; Moss never considers code that appears in a base file to match any other code. If your results include many unintended matches, then it is best to place all legitimately shared code in a base file (e.g., instructor-supplied code, common libraries, etc.) and resubmit the query to the server.

- Moss is a computer program that detects structural similarities in programs and nothing more; it has no idea why programs may be structurally similar. As noted above, there are reasons besides plagiarism that two programs may appear the same (e.g., they are both based on the same third program, such as instructor-supplied code for an assignment). Results from Moss cannot be taken as direct evidence of plagiarism---it is still necessary for someone to examine the programs and make a judgment. 

## Credits
Moss was written and is maintained by Alex Aiken, aiken@cs.stanford.edu.

The HTML interface was conceived of and designed by Guido Malpohl (s_malpoh@ira.uka.de), the author of JPlag, a plagiarism detection system for Java programs.

PlagCheck extracts information from the webpages for easier storing of results.
Contact [varshneybhupesh@gmail.com]() for more info.
