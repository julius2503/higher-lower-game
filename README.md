# Higher-Lower Game
A Python Bot that automates the Higher-Lower game

## How it works
I built a bot that automates the [Higher-Lower Game](http://www.higherlowergame.com). 
It creates a json-Database where all words and their value will be added to. 
To fill this database, the programm takes the left word and value and adds it to the db.
By looking at the size of the value, the programm determines a probability on wether the right word would have a higher or lower average monthly search.
The whole database has a capacity of 1.560 values. The highscore of the programm was 1.557. After this score was reached the higher-lower button disappeared, which leads to the conclusion that this is the final highscore.
The video of reaching the highscore is available [here](https://youtu.be/1wf2AVbQTxY?si=OfAltlhsbCnUA-8p).

This documentations contains the programm "higherlower.py" and the database "db.json".

## Requirements
To run this code the following arrangements must be set:
 1. Python 3.x must be installed
 2. Newest [ChromeDriver](https://chromedriver.chromium.org/) must be downloaded and added to the folder
 3. The following libraries must be installed:
    > pip install selenium 

    > pip install numpy

    > pip install colorama
