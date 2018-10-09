# How-To-Selenium.py
A step by step tutorial for setting up and working with Selenium's webdriver 

Selenium Explained
------------------
Originally created as a web testing framework, the Selenium Webdriver library allows developers to control web browsers and interact with sites just like any other user. 
It was originally created, and is mostly used for testing of web applications. 
An automated testing bot can do both unit and volume testing on a relativley large scale.

*__What does that mean in human terms?__*

You make a website for your bakery, jerrysgoodies.com
You want to be sure your website works, so you try every link, navigate to every page, make sure all the text boxes work etc.
A couple bugs are found, you fix them. Easy. 

It's been almost a year and buisness is going great,so great actually you need a more professional platform with a web store. 
You also make some UX adjustements and had to change your database to something more scaleable. 
There are too many elements to reliably test on your own, and you also need to simulate many simultanious users.
So, to solve this you invade your neices birthday party, give every overcaffinated 8 year old a laptop or tablet, and set them loose on your site, with a package of fundip to any child who can reach the "mystical 404 page".

It's been almost two years and Mary Berry herself walks into your bakery, she thinks your pasteries are positivley perfect, so perfect infact that she offers you a 1 hour time slot on the BBC. Although this is a wonderful oppertunity, the BBC One has up to 30 million viewers, scaling at this point is hard enough but *_testing!?!_*

This is where web automation and testing frameworks come in.
We can create a relativley simple bot to crawl through our site, test every controller element and report back any errors. Selenium is extra cool, as it iteracts exactly how a user would (at least as far as the host is concerned) and you can easily run a quarter million simultanious instances of the same program, emulating an army of ravenous foodies rampaging through your website. (and best of all, no small sticky handprints on your Macbook).

Web Automation, Scraping, and Crawling Explained
------------------------------------------------

*__What is Web Automation?__*

Let me explain with a personal annecdote.
I work as a techinical developer for a University department who has a constant need for researchers, instructors, student workers, study perticipants etc. As such they use the hiring system and website used by the whole university. While its fine for hiring the occasional faculty, the application, department and HR review takes far too long. Often several hours a week were spent downloading resumes, curriculum vita, and cover leters, renaming and organizing files, and uploading applicants to our private server.

I was tasked with a solution to this problem. The ideal answer would be to just change the job application site, however our department doesnt have access to the source.  Even if we did, it'd take far to long to understand the archetecture, and any plugins or dependancies used, then design a new solution and interface, as well as testing and uploading the new in production siteTherefore the best solution is actually adjust the interactions between the users and the jobsite. 

And once again, web automation becomes a super useful tool. 
Now we can create a python script (minimal setup for users, fast prototyping, and cross platform support) where the faculty member can enter their login information, the script will open its own instance of the page, login, and iterate through the applicants, automatically downloading, naming, and categorizing the different files. It's not the fastest or most elegant solution, but it was easy to create, is easy to adapt and support within our own department, and most importantly, the faculty is happy.
		
*__What is Web Scraping?__*

Web scraping is the practice of creating a local copy of already existing web data. You don't always need selenium or an activley interfacing browser when doing web scraping. Often times the data you need is contained on just a couple urls, and contained within the page's source html. We're going to work on an example of web scraping using a wikipedia table as our target.
		
*__Web Scraping Vs Web Crawling?__*

These two terms are used pretty interchangeably, however they do have two different semantic definitions. Web crawling usually refers to a combination of web automation and web scraping, a bot would go to a url, visit and index every link available, and oftentimes would save either a portion, or a whole copy of those index pages. Web crawlers and indexers are an essential technology for search engines. Google can't just "search the internet" as it's arguably not a well organized data structure.  Often the only common factor between websites are urls, and even those can be drastically altered (see torproject.org and .onion urls). To create a searchable indexed list of websites, Google and other data companies have armies of web crawlers indexing sites and reporting back. 
Google has an excellent article on their indexing bots and how they work here

[Google Site Indexing](https://www.google.com/search/howsearchworks/crawling-indexing/ "Google Site Indexing")

		
Getting Started
----------------
We will need three (four if your on mac) programs to get started. 
	Python
	Pip
	Selenium
	(and Firefox) 
*__Python Installation__*

**Mac**

Before we install python, we first need a UNIX package manager.  The most popular is [Homebrew](https://brew.sh/#install)
To install it
+ open the terminal and copy paste this line
```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
+ Then we need to add Homebrew to the bottom of your PATH (this is an indexed list of programs on your computer that allows you to open them from the command line)
```bash
echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.profile
```
+ To verify your homebrew installation 
```bash
brew doctor
```

Now we can easily install Python 3
+ type this in terminal
```bash
brew install python
```bash
Pip (The python package manager) should be automatically installed pointing to Python 3
To test our installation
```bash
python --version
```
+ Verify `Python 3.x.x` is the output

**Linux**

Nearly every updated Linux distro should have python 3 preinstalled
+ Verify this with
```bash
python3 --version
```
+ otherwise [Ubuntu]
```bash
sudo apt-get update
sudo apt-get install python3.6
```

**Windows 10**

+ Use your preferred web browser to nagivate to "https://www.python.org/downloads/"
+ Download the latest version (at this time is 3.7.0)
+ Run the installer
+ In the start menu type "Python"
+ >Right click the entry that says "Python 3.x" 	
+ >Open file location
If you do NOT see a series of shortcuts skip this next step
If you do see a series of shortcuts, dont panic
+ Right Click "Python 3.x" (It should look just like the one that appeared in windows search"
+ >Open file location
You should see a file called python.exe
In the file explorer nagivation menu (should say something like "> This PC> ...(C:) > ... > Python3X")
+ >Right click *In The Navigation Bar, After the "Python3X" entry*
+ >Copy address as text
+ In the windows search bar type "edit enviroment"
+ >Select "edit envrioment variables for your account"
In the Envioment Varibles Window
+ >Select Path
+ >Click Edit
+ >New 
+ >Paste your address from the file explorer 
you may need to add a '\' at the end of the line if it doesnt already exist 
It should look something like this 
```
C:Program Files\Python36\
```
+ Make another copy of this path variable but add Scripts\ to the end
This will allow us to call python library elements and the python package manager
This should look something like 
```
C:Program Files\Python36\Scripts\
```
+ Press okay to exit
			
After making your two path variables, lets test our installation
+ close any currently open command prompt windows
(you'll want to do this everytime you edit the windows path)
+ open command prompt as administrator
+ type 
```bash
python
```
Command prompt should popup information about your python install
and a new line header that begins with ">>>"
This is your python shell! 	

__A Note on Python and Terminal/Command Prompt__

+ Python runs as a container in your shell
+ Typing shell commands in python will only result in errors and vice versa
+ type 
```bash
python
```
in your shell window to enter python's terminal
**Pythons terminal begins with '>>>'**
to exit type 
```python
>>> exit()
```
It's easy to forget if your in python or shell, and this can lead to some odd error messages
Always remeber to double check line beginnings in shell.
		
*__Selenium Installation__*

Python has a super neat package manager called pip.
We can ask pip to get any library from the python package index "pypi.org" and it will handle installation and dependancies for us.
To install selenium we type in the terminal (not in python)
```bash
pip3 install selenium
```
You can also just use pip, however pip3 makes sure only libaries with python3 support will be installed 
*Note:python had a fork in 2008, and outdated libaries are largely not backwards compatable from 3.0 -> 2.7*

**Webdriver**

Webdriver is the heart of our webscraping programs, it interfaces between the browser and Selenium.
Each browser has their own unique webdriver, and each has their pros and cons (chrome has more tools and support, safari has the easiest setup, firefox allows for simutanious user and bot control).
For this example however, we're going to be using Firefox and GeckoDriver
All of Firefox's source code is public, and we're going to download the Geckodriver off Mozilla's github page.
+ https://github.com/mozilla/geckodriver/releases
+ Download the latest zip or tar for your system, (at this moment v.023.0)
+ NOTE: Your Firefox bowser must be FULLY UPDATED to use the most recent geckodriver, elsewise version conflicts appear that are hard to diagnose
	
**OSX/Linux**

+ Extract the zip file to /usr/local/bin directory
```bash
sudo tar -xzf geckodriver-v0.23.0-linux64.tar.gz -C /usr/local/bin
```
+ then navigate to the /usr/local/bin directory, and verify geckodriver has read and write permissions
```bash
cd /usr/local/bin
chmod u+x geckodriver
```
**Windows**

+ Extract the Zip file somewhere memorable and safe (I reccomend in your python directory)
Now we need to add the file folder to path
+ Follow the same steps as with adding python to path 
(file location > address bar > copy address as text > account envioment varables>edit path> new > paste)
+ make sure you add a '\' at the end 
+ Finally your path enviroment varibles should look something like this 

//Insert Image here//

Writing Your First Script
------------------------
				
*__Opening Google!__*

Congratulations on making it this far, setup was the hardest part!
+ Now we can actually write code!
+ Open your console and type 
```bash
python 
```
(or 'python3' if python 2.7 appears)
(Remember, your line should now begin with '>>>')
+ First we need to import the selenium library
```python
>>>import selenium
```
+ Next we need to import the webdriver class
```python
>>>from selenium import webdriver
```
+ Now make an instance of our webdriver object, and make sure its using the Firefox Webdriver (Geckodriver)
```python
>>>driver = webdriver.Firefox()
```
(A firefox window should have popped up, we're making some serious progress)
+ Lets open a web address 
```python
>>>driver.get("https://www.google.com")
```
Note: Make sure you include the 'http://' or 'https://'
	
Pretty cool right? 

The ability to test python code so easily in console is part of what makes developing in python with webdriver so fun.
However, we're probably going to want to be able to save and open our own files, so we have a more perminant copy, and so we can create more complex scripts.
	
+ Open your favorite text editor and start a file called 'open_google.py'
+ *If your new to development I'd reccomend IDLE.*
+ *It should be already downloaded with python (search 'idle' in window start menu search) and has both syntax highligting, debugging tools, and has a handy python shell next to your .py file.*
+ Now were going to input the same commands as before, but in the text editor.
+ To run
+ *In "Idle" select Run>Run Module*
+ In non-python shell, type
```bash 
python open_google.py
```
Sweet, but how do we turn it off?
After you're done with whatever you're doing in the browser, it's proper to close out your session so those resources can be properly reallocted.
+ To do so we add 
```python
driver.quit()
```
to the end of our file
		
But Wait!?!?!
Now google.com opens and then closes immediatley after!?! 
+Lets add a timer, so google will be open for exactly how long it takes to show your mom the super cool thing you did.
+ import the time library at the top of our program
```python
import time
```
+ Then, between `driver.get()` and `driver.quit()` add
```python
time.sleep(60) 
```
Now the program will open google, wait 60 seconds, then close everything for you.
		
Woo! You're offically browing the web remotely!! 
In the next section we'll try our hand at web scraping!
