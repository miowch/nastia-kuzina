# Task 3

## Prerequisites

[Python 3](https://www.python.org/downloads/)
[Docker](https://docs.docker.com/desktop/)

### Installing

1. Clone the repository.
1. Go to the cloned directory.

   ```bash
   cd <PATH-TO-YOUR-CLONED-DIRECTORY>
   ```

1. Create and activate virtual environment (e.g. n26_nastia_kuzina).

   ```bash
   pyenv virtualenv n26_nastia_kuzina
   ```

   ```bash
   pyenv activate n26_nastia_kuzina
   ```

1. Install packages from "requirements file"

   ```bash
   pip install -r requirements.txt
   ```

## Running tests

### In Docker

1. Open Docker.
1. Run tests in container.

   ```bash
   docker compose up -d
   ```

   After that you will be able to see running Swagger on `http://localhost:8080/` and generated Allure reports in the `allure_results` folder.

1. Generate Allure report

   ```bash
   allure serve allure-results
   ```

### In CLI

1. Open Docker.
1. Run Swagger server.

   ```bash
   docker compose up -d
   ```

   After that you will be able to see running Swagger on `http://localhost:8080/`.

1. Run tests.

   ```bash
   pytest --alluredir allure_results
   ```

1. Generate Allure report

   ```bash
   allure serve allure_results
   ```

## Reasoning

I tried to achieve scalability and maintainability of the tests by leaning to the following rules:

1. Tests logic is separated from tests framework implementation. Util methods are in the lib folder, tests are stored in the tests one.
1. Don't Repeat Yourself principle in creating classes, methods and variables.
1. Clear logging for debugging.
1. Clear reporting with Allure annotations.
1. Clear README file with information about the project setup and instruction of how to run tests.

I chose **Python** language because I feel more confident in writing the code in it. If I have more time I would rather use **Kotlin**.

I selected **Allure** for generating reports because of the following:

1. Actionable, visual reporting for fast debugging
1. Clear test coverage and history tracking
1. Seamless integration with existing tools
