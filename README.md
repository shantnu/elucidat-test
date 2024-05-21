# Elucidat Test

- [Elucidat Test](#elucidat-test)
  - [To run the tests](#to-run-the-tests)
  - [Bug Report](#bug-report)


## To run the tests

Create and activate virtual env:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install python libraries:

```
pip install -r requirements.txt
```

Install playwright libraries:

```
playwright install
```

Run the tests:



```
behave -f html -o out.html

```

This will output the result as an html file (out.html).

Any failure videos will be under the videos folder

Tested on Mac & Linux (though should work on Windows)

## Bug Report

The bug report is in "Bug Report.docx". There is also a video showing a failure on a mobile in the git repo : elucidat-iphone-bug.MP4
