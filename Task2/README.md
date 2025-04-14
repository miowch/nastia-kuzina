# Task 2

## Prerequisites

[Python 3](https://www.python.org/downloads/)
[Appium](https://appium.io/docs/en/latest/quickstart/install/)
[Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)

## Installing

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

## Running the tests

1. [Start Appium Server.](https://appium.io/docs/en/latest/quickstart/install/#starting-appium)
1. Run an emulator with installed Monefy app

   If the app is not installed,
   add the path to the app as the desired capability in webdriver.py

   ```python
   app='<PATH-TO-YOUR-CLONED-DIRECTORY>/Task2/apks/{apkFile}'
   ```

1. Make sure it is the only connected device.

   ```bash
   adb devices
   ```

1. Run tests.

   ```bash
   pytest --alluredir allure-results
   ```

1. Generate Allure report

   ```bash
   allure serve allure-results
   ```

## Reasoning

I tried to achieve scalability and maintainability of the tests by leaning to the following rules:

1. Business logic of E2E tests is separated from tests implementation. \
   Tests are stored in the tests folder and all methods are separated using Page-Object pattern.
1. Don't Repeat Yourself principle in creating classes, methods and variables.
1. Explicit waits for elements presence or invisibility instead of sleep method.
1. Clear reporting with Allure annotations.
1. Clear README file with information about the project setup and instruction of how to run tests.
1. Disclaimer: the next critical step if I have more time would be to integrate the solution into GitHub Actions (or any other CI/CD pipeline that is used in the company).

I chose **Python** language because I feel more confident in writing the code in it. If I have more time I would rather use **Kotlin** but the rest would be the same, Appium and Allure.

I opted for **Appium** because it provides cross-platform support for Android and iOS apps, it is language agnostic and it drives an app like a real user would, through the actual UI layer.

I selected **Allure** for generating reports because of the following:

1. Actionable, visual reporting for fast debugging
1. Clear test coverage and history tracking
1. Seamless integration with existing tools
