# cc-cheat
The MOSS interface scripts for CodeClassroom

## TODO:

Fetch the URL and gather following results:

- [x] Percentage of Code Matches
- [x] Number of Lines Matched
- [x] URL itself
- [x] Lines Matched
- [x] Date/Time of submission
- [ ] Convert Time to IST.
- [x] Return a list of dictionary containing:
    ```json
    [
      {
        "file1":"filename1.py",
        "file2":"filename2.py",
        "percentage":"34",
        "lines_matched":["2-3", "10-11"],
        "date":"2019-10-03",
        "time":"05:48:01",
        "url":"https://mossresults/..."
      },
    ....
    ]
    ```

### Process

1. We send files to MOSS.
2. MOSS returns a URL like `http://moss.stanford.edu/results/500496824`.
3. We Parse the page and obtain following details.
 - Files which have similarity.
 - Percentage Matches.
 - No.of Lines Matched.
4. For every 2 file matches, we parse the link given in table `http://moss.stanford.edu/results/500496824/match0.html`.
From this we parse:
 - Line Number which have matches
5. That's it.