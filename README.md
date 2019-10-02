# cc-cheat
The MOSS interface scripts for CodeClassroom

## TODO:

Fetch the URL and gather following results:

- [x] Percentage of Code Matches
- [x] Number of Lines Matched
- [x] URL itself
- [ ] Lines Matched
- [ ] Date/Time of submission
- [ ] Return a list of dictionary containing:
    ```json
    [
      {
        "file1":"filename1.py",
        "file2":"filename2.py",
        "percentage":"34",
        "lines_matched":["2-3", "10-11"],
        "date":"x/x/201x",
        "time":"XX:YY AM/PM",
        "url":"https://mossresults/..."
      },
    ....
    ]
    ```
