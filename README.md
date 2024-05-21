# Elucidat Test

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
behave

```

The output will be visible on commandline. There is also an html report that can be generated:

```
behave -f html -o out.html

```


Tested on Mac & Linux (though should work on Windows)