#!/usr/bin/env python3

import cmd

# Start gamut console
# > gamut

# console started, first line is the mode, second line is just a simple prompt
# [gamut]
# > 

# enter pocket, login process start if auth required
# [gamut]
# > pocket
# upon login success, prompt updated
# [pocket|username]
# >

# below will hide the mode line

# use 'select --list --untagged'
# vim will open, when file saved and vim quite, contents left over is being selected
# > select -lu

# update with tag 'Tech'
# > update -t Tech 

class Console (cmd.Cmd):
    """
    Console: the driver of command loop.

    Setup the instance
    >>> console = Console()

    Enure it behave like a shell
    >>> console.use_rawinput=0
    >>> console.cmdqueue=["", "pocket", "q"]
    >>> console.start()
    """

    def start(self):
        self.prompt = '[gamut] '
        self.cmdloop()

    def do_quit(self, args):
        return True


def main():
    console = Console()
    console.start()

if __name__ == '__main__':
    main()
