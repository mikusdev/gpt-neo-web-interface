# gpt-neo-web-interface
A simple GPT-Neo web interface. This can run on a vultr 1 VCPU, and 512MB ram.

## How can I run this?
Use a VPS service, or run it yourself!

`git clone https://github.com/mikusdev/gpt-neo-web-interface.git`
`cd gpt-neo-web-interface`

Now the Python part.
To install the modules required, run `pip install -r requirements.txt` or `pip install -r requirements.txt`, depending on your version of python.

Then simply run `python3 main.py` or `python main.py`

You should make sure that port 80 is open, and ready for traffic (you can run `sudo ufw allow 80` on ubuntu)
