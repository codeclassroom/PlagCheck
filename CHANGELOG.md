# Changelog


## [0.4] - March 10, 2020

### Changed [⚠️ Breaking Changes]
- `getShareScores` & `getInsights` have been decoupled from the check class, they now have to be imported separately.
- Minor changes in the `analyze.py` module.


## [0.3] - Jan 1, 2020

### Added

-  New module `analyze.py` for Moss Results analysis
- `getShareScores()` for returning frequency of shared files.
- `addFile()` for adding files.
- `addFilesByWildCard()` for submitting multiple files.
- Support for adding base code using `addBaseCode()`.

### Changed
- The plagcheck module is now more modularised. `check` is now a class.
- `__get_line_numbers()` now runs in a new thread.

### Removed
- `requests` as a dependency, network requests are now 50% faster.


## [0.2] - Nov 9, 2019
- Minor Improvements


## [0.1] - Nov 3, 2019
- Initial Release
