#!/usr/bin/env python3

import argparse
import subprocess
import re


# Filter out stdout and only print out the IP address so the user can do something like
# export DOCKER_HOST=$(~/multipass_get_ip_addr.py docker-host)
def get_ip_addr(args):
    batcmd = ["multipass", "info", args.container]
    proc = subprocess.Popen(batcmd, stdout=subprocess.PIPE)
    out = proc.stdout.read()
    out = "".join(chr(x) for x in out)
    out = out.split("\n")
    for line in out:
        if line.startswith("IPv4:"):
            line = line.strip().replace("\t", " ")
            line = re.sub("\s+", " ", line)
            chunks = line.split(" ")
            if len(chunks) > 1:
                print(chunks[1])
                return


# Get the arguments - really in this case it's the container
def parse_args():
    parser = argparse.ArgumentParser(description="Get IP address for a container in multipass (https://multipass.run)")
    parser.add_argument("container", help="Container to get IP address from in multipass")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    get_ip_addr(args)
