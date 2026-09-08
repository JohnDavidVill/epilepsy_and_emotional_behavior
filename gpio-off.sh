#!/bin/bash
# gpio-off.sh, turn off the gpio clock
# Made by John David Villarreal
# Ensure gpio-pulse.service and gpio-pulse.timer exists in /etc/systemd/system

sudo systemctl disable --now gpio-pulse.timer
echo "gpio-pulse.timer has been turned off"
