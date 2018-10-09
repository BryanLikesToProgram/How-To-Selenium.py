# How-To-Selenium.py
A step by step tutorial for setting up and working with Selenium's webdriver 

About
Why is Selenium cool?
Originally created as a web testing framework, the Selenium Webdriver library allows developers to control web browsers and interact with sites just like any other user. 
It was originally created, and is mostly used for testing of web applications. 
An automated testing bot can do both unit and volume testing on a relativley large scale.
What does that mean?
	You make a website, jerrysgoodies.com
	You want to test that website, make sure all the links aren't broken.
		Make a sitecrawler, test every link, button etc. 
		Return an error if you reach a 404 page
		Runs everytime you add a page, site update, even scheduled to run regularly
	Links work, your buisness is going well, but your getting featured on food network.
	What happens if all 596 thousand viewers try to access your site at once!?!?!
		If you have lots (Several hundred thousand) of friends, family, social media followers, you can have them all login at the same time, and browse your site. 
		Easy right? 
		Or, for those of us with a slightly smaller social network:
		Rent a beefy server, Amazon Web Services, Microsoft Azure, etc.
		Now you can run 596 Thousand Instances of your testing tool, no need to explain to Aunt Jackie that she can't use the Ipad Facebook app to browse the web.
		LPT: Don't want to pay for an expensive cloud server for testing? 
			 Just whisper this summuning spell into the nearest ethernet wall jack
			 "whats the difference between a systems admin and systems engineer"
			 A figure will emerge, treat them with great kidness and listen closely to their tale.
			 You have now successfully befriended a great and powerful IT Specialist. 
			 They will inevitably have a beefy homelab you can use to run your webapp 
Selenium Webdriver is extremely versitile, despite being primarily a web testing framework.
It's also used extensively for general web automation, web scraping, and plenty more.
Because we can see the program navigating and making selections in real time, as well as it's wide support for many drivers, operating systems, and languages, Selenium is a fan favorite. 
It's a great choice for people who aren't especially experienced with web automation or programming in general.
Paired with Python3's extensive documentation and libraries, and intuitive user friendly syntax, Python and Selenium is the perfect combination for experienced developers and non-STEM occupations and hobbyists. 
	What is Web Automation?
		Let me explain with a personal annecdote
		I work as a techinical developer for a University department who has a constant need for researchers, instructors, student workers, study perticipants etc.
		As such they use the hiring system and website used by the whole university.
		While its fine for hiring the occasional faculty, the application, department and HR review takes far too long.
		Often several hours a week were spent downloading resumes, curriculum vita, and cover leters, renaming and organizing files, and uploading applicants to our private server.
		I was tasked with a solution to this problem.
		The ideal answer would be to just change the job application site, however our department doesnt have access to the source. 
		Even if we did, it'd take far to long to understand the archetecture, and any plugins or dependancies used, then design a new solution and interface, as well as testing and uploading the new in production site.
		Therefore the best solution is actually adjust the interactions between the users and the jobsite. 
		And here's where web automation is a super useful tool. 
		Now we can create a python script (minimal setup for users, fast prototyping, and cross platform support) with a where the faculty member can enter their login information, 
		the script will open its own instance of the page, login, and iterate through the applicants, automatically downloading, naming, and categorizing the different files. 
		It's not the fastest or most elegant solution, but it was easy to create, is easy to adapt and support within our own department, and most importantly, the faculty is happy, 
	What is Web Scraping? 
		Web scraping is the practice of creating a local copy of already existing web data. You don't always need selenium or an activley interfacing browser when doing web scraping. 
		Often times the data you need is contained on just a couple urls, and contained within the page's source html. 
		We're going to work on an example of web scraping using a wikipedia table as our target.
	Web Scraping Vs Web Crawling?
		These two terms are used pretty interchangeably, however they do have two different semantic definitions. 
		Web crawling usually refers to a combination of web automation and web scraping, a bot would go to a url, visit and index every link available, and oftentimes would save either a portion, or a whole copy of those index pages.
		Web crawlers and indexers are an essential technology for search engines. Google can't just "search the internet" as it's arguably not a well organized data structure. 
		Often the only common factor between websites are urls, and even those can be drastically altered (see torproject.org and .onion urls). 
		To create a searchable indexed list of websites, Google and other data companies have armies of web crawlers indexing sites and reporting back. 
		Google has an excellent article on their indexing bots and how they work here google.com/search/howsearchworks/crawling-indexing/
Lets get started. 
	Getting setup 
		We will need three (four if your on mac) programs to get started. 
			Python
			Pip
			Selenium
		Insructions based on OS are as follows
		Mac
			Before we install python, we first need a UNIX package manager. 
			The most popular is Homebrew (https://brew.sh/#install)
				To install it, open the terminal and copy paste this line
					ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
				Then we need to add Homebrew to the bottom of your PATH (this is an indexed list of programs on your computer that allows you to open them from the command line)
					echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.profile
				To verify your homebrew installation 
					brew doctor
			Now its much easier, lets install python 3
				type this in terminal
					brew install python
			Pip should be automatically installed pointing to Python 3
			To test our installation
				python --version
			Make sure "Python 3.x.x" is the output	
		Linux
			Nearly every updated Linux distro should have python 3 preinstalled
			Verify this with 
				[Ubuntu]
				python3 --version
			otherwise
				[Ubuntu]
				sudo apt-get update
				sudo apt-get install python3.6
		Windows 10
			Use your preferred webbrowser to nagivate to "https://www.python.org/downloads/"
			Download the latest version (at this time is 3.7.0)
			Run the installer
			In the start menu type "Python"
			Right click the entry that says "Python 3.x" 
				Open file location
			If you do NOT see a series of shortcuts skip this next step
			If you do see a series of shortcuts, dont panic
				Right Click "Python 3.x" (It should look just like the one that appeared in windows search"
				Open file location
			You should see a file called python.exe
			In the file explorer nagivation menu (should say something like "> This PC> ...(C:) > ... > Python3X")
			Right click *In The Navigation Bar, After the "Python3X" entry*
				Copy address as text
			In the windows search bar type 
				"edit enviroment"
				Select "edit envrioment variables for your account"
			In the Envioment Varibles Window
				Select Path
				Click Edit
				New 
					Paste your address from the file explorer 
				you may need to add a '\' at the end of the line if it doesnt already exist 
				It should look something like this 
				"C:Program Files\Python36\"
				Make another copy of this path variable but add Scripts\ to the end
				This will allow us to call python library elements and the python package manager
				This should look something like 
				"C:Program Files\Python36\Scripts\"
				Press okay to exit
			
			After making your two path variables, lets test our installation
				close any currently open command prompt windows
				(you'll want to do this everytime you edit the windows path)
				open command prompt as administrator
				type "python"
				Command prompt should popup information about your python install
				and a new line header that begins with ">>>"
				This is your python shell! 
	A Note on Python and Terminal/Command Prompt
		Python runs as a container in your shell
		Typing shell commands in python will only result in errors and vice versa
		type 'python' in your shell window to enter python's terminal
		*Pythons terminal begins with '>>>'*
		to exit type 'exit()'
		It's easy to forget if your in python or shell, and this can lead to some odd error messages
		Always remeber to double check line beginnings in shell.
	Selenium Installation
		Python has a super neat package manager called pip.
		We can ask pip to get any library from the python package index "pypi.org" and it will handle installation and dependancies for us.
		To install selenium we type 
			pip3 install selenium
		You can also just use pip, however pip3 makes sure only libaries with python3 support will be installed 
			(python had a fork in 2008, and outdated libaries are largely not backwards compatable from 3.0 -> 2.7)
	Webdriver Setup
		Webdriver is the heart of our webscraping programs, it interfaces between the browser and Selenium.
		Each browser has their own unique webdriver, and each has their pros and cons 
			(chrome has more tools and support, safari has the easiest setup, firefox allows for simutanious user and bot control)
		For this example however, we're going to be using Firefox and GeckoDriver
		All of Firefox's source code is public, and we're going to download the Geckodriver off Mozilla's github page.
		https://github.com/mozilla/geckodriver/releases
		Download the latest zip or tar for your system, (at this moment v.023.0)
		NOTE: You're Firefox bowser must be FULLY UPDATED to use the most recent geckodriver, elsewise version conflicts appear that are hard to diagnose
		Windows
			Extract the Zip file somewhere memorable and safe (I reccomend in your python directory)
			Now we need to add this to path
			Follow the same steps as with adding python to path 
			(file location > address bar > copy address as text > account envioment varables>edit path> new > paste)
			and make sure you add a '\' at the end 
			Finally your path envioment varibles should look something like this 
		OSX/Linux
			Extract the zip file to /usr/local/bin directory
				sudo tar -xzf geckodriver-v0.23.0-linux64.tar.gz -C /usr/local/bin
			then navigate to the /usr/local/bin directory, and verify geckodriver has read and write permissions
				cd /usr/local/bin
				chmod u+x geckodriver
Opening Google!
	Congratulations on making it this far, setup of selenium hardest part!
	Now we can actually write code!
	Open your console and type 
		python (or 'python3' if python 2.7 appears)
	(Remeber, your line should now begin with '>>>')
	First we need to import the selenium library
		import selenium
	Next we need to import the webdriver class
		from selenium import webdriver
	Now lets make an instance of our webdriver object, and make sure its using the Firefox Webdriver (Geckodriver)
		driver = webdriver.Firefox()
	(A firefox window should have popped up, we're making some serious progress)
	Lets open a web address 
		driver.get("https://www.google.com")
		Note: Make sure you include the 'http://' or 'https://'
	Pretty cool right? 
	The ability to test python code so easily in console is part of what makes developing in python with webdriver so fun.
	However, we're probably going to want to be able to save and open our own files, so we have a more perminant copy, and so we can create more complex scripts.
	Open your favorite text editor and start a file called 'open_google.py'
		If your new to development I'd reccomend IDLE. 
		It should be already downloaded with python (search 'idle' in window start menu search)
		and has both syntax highligting, debugging tools, and has a handy python shell next to your .py file.
	We're going to input the same things as before and try running it.
		In "Idle" select Run>Run Module
		In shell, type "python open_google.py"
	pretty cool but how do we turn it off?
		After you're done with whatever you're doing in the browser, it's proper to close out your session so those resources can be properly reallocted.
		To do so we add 
			driver.quit()
		to the end of our file
		But Wait!?!?!
		Now google.com opens and then closes immediatley after!?! 
		Lets add a timer, so google will be open for exactly how long it takes to show your mom the super cool thing you did.
		Lets import the time library at the top of our program
			import time
		Then, between driver.get() and driver.quit() add
			time.sleep(60) 
		Now the program will open google, wait 60 seconds, then close everything for you.
	Woo! You're offically browing the web remotely!! 
	In the next section we'll try our hand at web scraping!