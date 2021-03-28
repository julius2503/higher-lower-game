from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json
import random
import numpy
from colorama import *

class game:
    def __init__(self):
        init(convert=True)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        self.driver.get("http://www.higherlowergame.com/")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div/div/span/section/div[2]/div/button[1]").click()  # Classic Game
        self.play()

    def play(self):
        while True:
            sleep(3)
            try:
                self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[1]/div[1]/div/div[1]/p[1]") # testen ob noch im Game
            except NoSuchElementException:
                print(Back.RED + "falsch" + Style.RESET_ALL)
                self.driver.get("http://www.higherlowergame.com/")
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div/div/span/section/div[2]/div/button[1]").click()
            else:
                print(Back.YELLOW + "richtig" + Style.RESET_ALL)

            print(" ")

            global value
            sleep(2)
            leftname = self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[1]/div[1]/div/div[1]/p[1]").text
            leftname = leftname.replace('“', "")
            leftname = leftname.replace('”', "")
            print("links Name: " + leftname)

            leftvalue = self.driver.find_element_by_class_name("term-volume__volume").text
            leftvalue = leftvalue.replace(",", "")
            leftvalue = int(leftvalue)
            print("links Wert: " + str(leftvalue))

            rightname = self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[1]/div[2]/div/div[1]/p[1]").text
            rightname = rightname.replace('“', "")
            rightname = rightname.replace('”', "")
            print("rechts Name: " + rightname)

            with open("db.json") as db:
                try:
                    data = json.load(db)
                except ValueError:
                    print(Fore.RED + "Fehler!!" + Style.RESET_ALL)
                    self.play()


            found = False

            for x in data["objects"]:   #check ob Links in der DB ist
                if x['name'] == leftname:
                    print(Back.CYAN + x["name"] + " found with value: " + str(x["value"]) + Style.RESET_ALL)
                    x['value'] = leftvalue
                    print("Value wurde erneurt")
                    value = x["value"]
                    found = True

            if not found:
                with open("db.json") as db:
                      data = json.load(db)
                      temp = data['objects']
                      newValue = {"name": leftname, "value": leftvalue}
                      temp.append(newValue)
                      with open("db.json", 'w') as dbw:
                         json.dump(data, dbw, indent=4)
                      print(Back.GREEN + "Added " + leftname + Style.RESET_ALL)


            xyz = False #check ob gefunden

            for y in data["objects"]:
                if y['name'] == rightname:
                    value = y['value']
                    print(Back.MAGENTA + rightname + " found with value: " + str(value) + Style.RESET_ALL)
                    xyz = True

            if xyz:
                if value > leftvalue:
                    print(rightname + " is higher than " + leftname)
                    self.driver.find_element_by_xpath('/html/body/div/div/span/span/div/div[2]/div[2]/button[1]').click() #höher
                else:
                    print(leftname + " is higher than " + rightname)
                    self.driver.find_element_by_xpath('/html/body/div/div/span/span/div/div[2]/div[2]/button[2]').click() #niedriger

            if not xyz:
                datamedian = [element["value"] for element in data["objects"]]
                datamedian.sort()
                datamedian = numpy.median(datamedian)
                print("median: " + str(datamedian))

                rand = random.randint(1, 100)
                print("Zufallszahl: " + str(rand))
                if leftvalue > 3*datamedian:
                    self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                    print(leftname + " 3x höher")
                elif leftvalue > 2*datamedian:
                    print(leftname + " 2x höher")
                    if rand >= 80:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                elif leftvalue > 1.5*datamedian:
                    print(leftname + " 1,5x höher")
                    if rand >= 70:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                elif leftvalue > 1.25*datamedian:
                    if rand >=60:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                elif leftvalue >= datamedian:
                    print(leftname + " etwas höher")
                    if rand > 53:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                elif 3*leftvalue < datamedian:
                    print(leftname + " 3x niedriger")
                    self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                elif 2*leftvalue < datamedian:
                    print(leftname + " 2x niedriger")
                    if rand >= 80:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                elif 1.5*leftvalue < datamedian:
                    print(leftname + " 1,5x niedriger")
                    if rand >= 70:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                elif 1.25*leftvalue < datamedian:
                    if rand >= 60:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                else:
                    print(leftname + " etwas niedriger")
                    if rand > 55:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[1]").click()  # höher
                    else:
                        self.driver.find_element_by_xpath("/html/body/div/div/span/span/div/div[2]/div[2]/button[2]").click()  # niedriger



game()
