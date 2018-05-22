from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait
import argparse


parser = argparse.ArgumentParser(description='Stress test the python selenium webdriver')
parser.add_argument('--num', type=int, help='Number of simultaneous instances', default=20)
parser.add_argument('--type', help='How to run the instances', choices=['parallel', 'concurrent'])
args = parser.parse_args()

def run():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    try:
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:9515',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
        )
        driver.close()
        driver.quit()
    except Exception as e:
        raise

num = args.num
with ProcessPoolExecutor(max_workers=num) if \
     args.type == 'parallel' else \
     ThreadPoolExecutor(max_workers=num) as executor:
    futures = []
    for _ in range(num):
        futures.append(executor.submit(run))
    wait(futures)
    for f in futures:
        print(f.exception())

