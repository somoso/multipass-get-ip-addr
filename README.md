# multipass-get-ip-addr
Get IP Address from multipass command line tool. Based off this [guide](https://github.com/ibmrcruicks/multipass-docker-engine) to getting Docker CLI on macOS.

Multipass's containers can change IP addresses when connecting to a new place (especially if you have a MacBook like me).

This was created so that when the shell is initialised (i.e. every time a new terminal instance is created - tab or window), the new shell will attempt to get the latest IP address info.

`multipass`'s info output will give this:

~~~
Name:           docker-host
State:          Running
IPv4:           192.168.64.3
                172.17.0.1
Release:        Ubuntu 20.04.3 LTS
Image hash:     10f8ae579fbf (Ubuntu 20.04 LTS)
Load:           0.00 0.00 0.01
Disk usage:     2.3G out of 4.7G
Memory usage:   186.4M out of 981.3M
Mounts:         --
~~~

Whereas `multipass-get-ip-addr.py` will simply return

```
192.168.64.3
```

allowing you to add an entry into your `.bashrc`/`.zshrc` shell like e.g.:

~~~
DOCKER_HOST=tcp://$(~/multipass_get_ip_addr.py docker-host):2375
export DOCKER_HOST
~~~

and get the latest IP address info in a new shell.

## Setup

1. Read the python script and make sure you are comfortable with it. *Don't* go running code you don't feel comfortable with, especially when sticking it in your `.bashrc`/`.zshrc`.
2. Download either the repo or the script itself and place it somewhere - remember the location. In my example I'll use `~`.
3. Give the script executable permissions (`chmod +x ~/multipass_get_ip_addr.py` in the terminal will do, replacing `~` with your directory).
4. Put the following in your `~/.bashrc` or `~/.zshrc` file:

~~~
DOCKER_HOST=tcp://$(~/multipass_get_ip_addr.py docker-host):2375
export DOCKER_HOST
~~~

Replacing `~` in `~/multipass_get_ip_addr.py` with your directory.

5. Run `source ~/.bashrc` or `source ~/.zshrc` depending on your shell. See if there are any errors. If there are, either fix them, report them as an issue, or just undo the changes in your `.*shrc` file and delete the script.

If you have no issues, try running a command like `docker images` and see if there any issues. If not, you've successfully setup multipass with docker
