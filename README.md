Intro
=====
This project contains often-used Python utilities during my work 
as web developer such as git clone, run bash command, command line argument parser, etc.

The Context
===========
In which situation we may use the utilities in this project?

We are working on Python project and need a command e.g. to run a bash command form Python code
the same way we run it from command line.

Usage
=====
- Create a sub folder in your project e.g. `$APP_HOME/util`; we call this `$UTIL_HOME`
- Download this project to `$UTIL_HOME` via running below 
[let-me-in.sh](https://github.com/namgivu/yihabapar/blob/master/let-me-in.sh) script - 
please edit `$UTIL_HOME` before you run it
```
$ let-me-in.sh $UTIL_HOME
```
e.g.
```
u=~/your-project/util
$ rm $u/* -rf ; let-me-in.sh $u 
```


Demo
====
- Apply `let-me-in.sh` (revision [6e12dc](https://github.com/namgivu/yihabapar/commit/6e12dccf91bb92f9b269627293924cf8f4aa81f8)) 
to project [namgivu/django-start](https://github.com/namgivu/django-start)
i.e. the project starts from revision [ff2d4d](https://github.com/namgivu/django-start/commit/ff2d4d7663057a8c18b15bb3503d520831a9b396)
, and then do apply to get revision [5d866c](https://github.com/namgivu/django-start/commit/5d866c958cb3cd67505d6d44831d218caff09b22)

Testing
=======
- [test](https://github.com/namgivu/django-start/commit/de6c2e2e0eb4abcea20cb81a215dbba899e93ee7) [run_bash](https://github.com/namgivu/yihabapar/commit/ccf1dae4d3d262f0f559023ad362664c6b33f00a#diff-f639b142ebd421e596f92ad3855b4892)
- [test](https://github.com/namgivu/django-start/commit/db36eb5b2a9ce00f92b3be7da1afa59de550d683) [get_arg](https://github.com/namgivu/yihabapar/commit/ce9585bd318855019ed29ee284e6d67b0bea529c#diff-11f1b60d8a13d8bc1b5af7c34c81c4dd)

The end.
