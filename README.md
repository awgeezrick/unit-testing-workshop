# Unit Testing Workshop

### Setup

Build docker and start container
```shell
# 1. build docker image
docker build . -t unit-testing-workshop

# 2. start docker container
docker run -it -v $(pwd):/code -p 8888:8888 unit-testing-workshop

# 3. in a second terminal window, get id of running container
docker ps 

# 4. start a second bash shell in the running container
docker exec -it <container-id> bash

# 5. Open yet another terminal window and run: 
bin/configure_venv_locally.sh
# After the command completes, configure your IDE to tell it that the python interpreter is in .venv-local/
# More instructions here: https://github.com/davified/ci-workshop-app/blob/master/docs/FAQs.md#ide-configuration

# 6. Open unit-testing-workshop repo in your IDE
```

### Commands to be run inside the docker container

```shell
# 1. add some color to your terminal
source bin/color_my_terminal.sh

# For exercise 1: run tests in watch mode and with colored output
nosetests --with-watch --rednose

# For execise 2: in another docker terminal, start jupyter notebook
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

# To stop the notebook / nosetests: hit Ctrl + C
# To exit the docker container    : hit Ctrl + D
```

### Exercises

#### Exercise 1: Calculator

Implement the following functions in `src/calculator.py`:

```python
# subtract(a, b)
subtract(2, 1) -> 1

# multiply(a, b)
multiply(2, 3) -> 6

# divide(a, b)
divide(10, 5) -> 2

# bonus: handle rounding of floats to 2 precision points
divide(10, 3) -> 3.33
```

#### Exercise 2: Adding tests and refactoring a notebook

We will refactor [this notebook](notebooks/sklearn-nlp-pipeline-before-refactoring.ipynb) by creating and extracting functions and adding tests.
