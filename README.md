# nox-plugin-proposal

Small demo of what comes to mind for a nox plugin system mimicking pytest's system

## Overview

This example contains a couple examples of some locally defined plugins. The nox sessions defined within them could 
also be defined in the noxfile, or remotely in a package.

The order of overwriting sessions is meant to match the behavior that pytest has for overwriting fixtures. Additionally 
I could see arguments for the concept of cicd related scopes or fixtures here, but that also might just be me drinking 
the pytest kool-aid a bit too much.

## Caveat

This is an incredibly rough draft and exists mostly just to communicate an idea to see if others are interested in 
moving this direction.

Personally I'm really biased toward Pytest plugins and general pytest structures, but that may not be the best way 
forward. Not to mention, if anyone has a better way to solve the issues I have encountered then that's the ideal 
situation, since this is quite a heavy proposal.
