from selenium.webdriver import Chrome

'''
This program opens the Blanton's website to add a product to a cart once it become available.
'''


def main() -> None:
    base_url = 'https://app.singlebarrelselect.com/'
    driver = Chrome()
    driver.get(base_url)


if __name__ == '__main__':
    main()
