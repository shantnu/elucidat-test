# Elucidat Test

- [Elucidat Test](#elucidat-test)
  - [To run the tests](#to-run-the-tests)
  - [Test Details](#test-details)
  - [Bug Report](#bug-report)
  - [TO DO](#to-do)


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

## Test Details

The tests use the gherkin (cucumber) format with behave.

Playwright (https://playwright.dev/python/) is used to automate the browser.

2 tests have been implemented:

1. Check the header is correct -- a simple test to check the web page loads
2. Check the score is a digit only -- currently fails (see Bug Report below for details)

## Bug Report

The bug report is in "Elucidat Test Report.docx".

 There is also a video showing a failure on a mobile in the git repo : elucidat-iphone-bug.MP4


## TO DO

Still to do:

1. Add more automated tests for the other bugs found, plus a end to end "happy case".


2. API testing: I'm not sure if there is an API tool (like Swagger). If not, maybe reverse engineer the network calls using the dev tools?

For testing, my preferred choice is Python with a library like requests, but I have used tools like Postman/Insominia.