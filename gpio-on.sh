#!/bin/bash
# Shell script to turn on the timer
# Made by John David Villarreal 09/08/26
# Ensure gpio-pulse.service and gpio-pulse.timer exist in /etc/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable --now gpio-pulse.timer
echo "gpio-pulse.timer started"
sudo systemctl list-timers gpio-pulse.timer --no-pager
