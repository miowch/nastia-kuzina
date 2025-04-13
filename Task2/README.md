### Prerequisites

[Python 3](https://www.python.org/downloads/)

[Appium](https://appium.io/docs/en/latest/quickstart/install/)

[Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)

### Installing

1. Clone the repository.
2. Go to the cloned directory.
   ```bash
   cd <PATH-TO-YOUR-CLONED-DIRECTORY>
   ```
3. Create and activate virtual environment (e.g. n26_nastia_kuzina).
   ```bash
   pyenv virtualenv n26_nastia_kuzina
   pyenv activate n26_nastia_kuzina
   ```
4. Install packages from "requirements file"
   ```bash
   pip install -r requirements.txt
   ```

## Running the tests

1. [Start Appium Server.](https://appium.io/docs/en/latest/quickstart/install/#starting-appium)
2. Run an emulator with installed Monefy app

   If the app is not installed,
   add the path to the app as the desired capability in webdriver.py

   ```
   app='<PATH-TO-YOUR-CLONED-DIRECTORY>/Task2/apks/{apkFile}'
   ```

3. Make sure it is the only connected device.
   ```bash
   adb devices
   ```
4. Run tests.

   ```bash
    pytest
   ```
