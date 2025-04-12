# Android environment
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.client_config import AppiumClientConfig


class Driver:
    def __init__(self):
        server_url_base = 'http://localhost:4723'
        desired_caps = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='AndroidTestDevice',
            appPackage='com.monefy.app.lite',
            appActivity='com.monefy.activities.main.MainActivity_',
            # app='<PATH-TO-YOUR-CLONED-DIRECTORY>/Task2/apks/com.monefy.app.lite.apk'
        )

        client_config = AppiumClientConfig(
            remote_server_addr=server_url_base,
            direct_connection=True,
            keep_alive=False,
            ignore_certificates=True,
        )
        self.driver = webdriver.Remote(
            options=UiAutomator2Options().load_capabilities(desired_caps),
            client_config=client_config
        )
