Python web development on chromebooks?
---
It’s not what you think…
----

I began a journey several months ago to see what it would take to be a web developer. After much research I decided upon [Thinkful] which I highly recommend.  I quickly found out that I needed a new laptop to be able to work on assignments over my lunch break and money was tight.  An uncommon solution emerged. The [HP14] chromebook.  With a couple hours and $350 the HP14 becomes a python web development machine which rivals laptops 3 times it’s cost.

All development will be done natively, there’s been much talk about chromebooks and web app IDE’s.  I found out quickly that this did not work well for me.  It’s really hard to beat a native environment configured with all professional level tools that other developers will be using.  Your mileage may vary of course.

Were going to be doing a side installation of Linux beside the current Chrome OS using [ChrUbuntu].  We will be able to hot switch between the two using some simple keyboard shortcuts.  Some people may have been turned off by mention of Linux.  Let me tell you, Elementary OS (eOS) is an awesome distro of Linux which I think will change the way you think of it.  Check it out [here] and [here ]. 

I am a new Linux user so I am simply compiling everything I came across on the internet.  I can vouch that everything works if followed per instruction but there may be a better way.  Just let me know in the comments. 

 _**Let’s get started.**_

---

###Install eOS###
>Follow this excellent [guide] from [+Jean-Louis Nguyen] which walks you thru every step, no knowledge of command line or linux required.  Second time around this took me an hour to complete.  Will vary based on speed of your internet connection.

-----

###Configure Dev Environment###
>Now that we have an eOS environment, let’s install and configure all the software we will need for web development.  Before we begin, review some [tips] regarding using eOS on the chromebook.  

####__Good? Ok let’s go.__####

---

  - ####Launch eOS####

  - ####CTRL+ALT+T (Open command terminal)#####

```sh
sudo apt-get install firefox
```

_Open up firefox to paste the following commands into the terminal_

---

**Web Browser - 64 bit Chrome**
```sh
cd ~/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo gdebi google-chrome-stable_current_amd64.deb
y
```
---
**Video player - VLC Player**
```sh
sudo apt-get install vlc
```
---
**File Compression**
```sh
sudo apt-get install unace rar unrar p7zip-rar p7zip
```

---

**File Backup - Dropbox**

[Download Ubuntu 64bit version]
```sh
sudo gdebi dropbox_1.6.2_amd64.deb
```
Start dropbox from Applications menu
Follow prompts

---

**Office Compatible - Libre Office**  (_big install_)
```sh
sudo apt-get install libreoffice
```

-----

**Graphic Editor - Gimp**
```sh
sudo apt-get install gimp
```

-----

**File cleanup - Bleachbit** (CCleaner for Ubuntu)
```sh
sudo apt-get install bleachbit
```

----

**Install SublimeText 3**
```sh
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
```

---

**Configure Sublime for Web development**
>Follow this excellent [guide] from Michael Herman from [RealPython.com]
 - ####Use CTRL where CMD is referenced ie. (CTRL+SHFT+P)
 - ####Jump right to Install Package Control

---

**Install Git **
```sh
sudo apt-get install git-core
```

**Install Sqlite3**
```sh
sudo apt-get install sqlite3 libsqlite3-dev
```

**Install ez_setup**
```sh
wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
```

**Install pip**
```sh
sudo easy_install pip
Install virtualenv
sudo pip install virtualenv
```

---

**Dependencies for SQLAlchemy**
```sh
sudo apt-get build-dep python-psycopg2
```

---


**Heroku Setup**
```sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```
Make sure your heroku profile is setup up.
```sh
heroku login

your email 
your password 

heroku keys:add
y

mkdir ~/Dropbox/projects
cd ~/Dropbox/projects
git clone https://github.com/heroku/python-getting-started.git
cd python-getting-started
virtualenv --no-site-packages env
source env/bin/activate
pip install -r requirements.txt --allow-all-external
foreman start
```

Click on hyperlink in terminal window to view local website

"CTRL+C" to kill foreman process

---

**Deploy to Heroku**
```sh
heroku create
git push heroku master
yes
heroku open
```


[Thinkful]:http://www.thinkful.com
[HP14]:http://www.amazon.com/gp/product/B00FGOTBQO/ref=pd_lpo_sbs_dp_ss_2?pf_rd_p=1535523722&pf_rd_s=lpo-top-stripe-1&pf_rd_t=201&pf_rd_i=B00FGOTC0Y&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1FW8J9AKAJHWT3DRNEX8
[ChrUbuntu]:http://chrubuntu.blogspot.ca/
[here]:http://elementaryos.org/
[here ]:http://www.macworld.com/article/2048021/if-i-had-to-leave-the-mac-id-switch-to-elementary-os.html
[guide]:http://jeanlouisnguyen.blogspot.com/2014/01/guide-how-to-install-elementary-os-on.html
[+Jean-Louis Nguyen]:http://www.google.com/url?q=http%3A%2F%2Fjeanlouisnguyen.blogspot.com%2F2014%2F01%2Fguide-how-to-install-elementary-os-on.html&sa=D&sntz=1&usg=AFQjCNGBIO8uLqFyJKrWw9aLI21hjyCiGw
[tips]:http://www.thisiswherewejumptotipsatbottom.com
[Download Ubuntu 64bit version]:https://www.dropbox.com/install?os=lnx
[guide]:https://www.google.com/url?q=https%3A%2F%2Frealpython.com%2Fblog%2Fpython%2Fsetting-up-sublime-text-3-for-full-stack-python-development%2F&sa=D&sntz=1&usg=AFQjCNH6XrV734vpm7oZlm7_0jtYKcYWdg
[RealPython.com]:http://www.realpython.com




