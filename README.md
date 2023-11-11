<p align='center'>
  <img src="./logo.png?raw=true" height="250px" alt="starbucks db" />
</p>

<h1 align="center">☕ STARBUCKS DB:  distributed tensor ☕</h1>

## What's all about 🤔

I'm implementing distributed tensor.<br/>

You will be able to write, read and modify your AI tensors (as in normal database).<br/>
It will also have worker like processing features. And it will be distributed.<br/>

Don't know if it will be useful in any way, but it's worth trying 😀<br/>


<br/><br/>
\* the db engine itself will be implemented in c++/cython

## Current state

Heavily in progress ! It's not usable yet 🔥 I should have something running till end of November 2023 🤞



## Install required packages

```
  python -m pip install -r requirements.txt
```


## Run tests

```
  python3 -m pytest -s tests or PYTHONPATH=`pwd` python3 -m pytest -s tests
```



# Run Mypy

```
  python3 -m mypy starbucks
```


# Roadmap

- [ ] 30/11/2023: working version of database engine in c++/cython
- [ ] 29/12/2023: pre-alpha
- [ ] 31/01/2024: alpha
- [ ] 29/02/2024: beta
- [ ] 29/03/2024: we are going live 
