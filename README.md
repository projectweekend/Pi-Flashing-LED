Pi-Flashing-LED
===============

Make red and green LEDs flash using GPIO

## Prerequisites:

### Have git installed
Git makes every day a little brighter. Don't code without it. Seriously. Do it: `sudo apt-get install git`

### Use a virtualenv
Ok, technically this step is optional. You can skip it and still install all of the Python dependencies in the instructions, but you will feel dirty later. Trust me, [virtualenv](http://www.virtualenv.org/) is a Python developer's best friend.

* Install virtualenv: `sudo pip install virtualenv`
* Start a fresh Python environment: `virtualenv call_it_whatever --no-site-packages`
* Start your new environment: `source ./call_it_whatever/bin/activate`
* Stop your environment (when you're done using the server): `deactivate`

### Local network config
Your Raspberry Pi needs to be connected to your local network (Wifi or Ethernet). If you don't have `avahi-daemon` installed, go take care of that: `sudo apt-get install avahi-daemon`

This will expose your Pi using its `hostname` on the local network. If the `hostname` is still set as default, you can access your Pi at `raspberrypi.local`. When the web server is running you can access it in a browser at `http://raspberrypi.local`

### Physical LED config
* Green LED connected on GPIO 18
* Red LED connected on GPIO 23

## Instructions:

* Make sure your `virtualenv` is activated (see section above)
* Clone this repo on your Pi: `git clone https://github.com/projectweekend/Pi-Flashing-LED.git`
* Install Python requirements from inside the cloned repo directory: `pip install -r requirements.txt`
* Fire up the web server: `sudo python server.py`
* Hit site from any browser on your local network: `http://raspberrypi.local`
