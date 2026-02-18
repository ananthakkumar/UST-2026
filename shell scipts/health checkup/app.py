#!/bin/bash

echo "------ System Health Report ------"
echo "Date: $(date)"
echo "---------------------------------"

# CPU Usage
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)" | awk '{print "User: "$2"%  System: "$4"%  Idle: "$8"%"}'
echo ""

# Memory Usage
echo "Memory Usage:"
free -h
echo ""

# Disk Usage
echo "Disk Usage:"
df -h
echo ""

# Top Processes (by CPU)
echo "Top 5 Processes by CPU:"
ps aux --sort=-%cpu | head -n 6
echo ""

# Active Network Connections
echo "Active Network Connections:"
netstat -tunapl 2>/dev/null | head -n 10
echo "---------------------------------"
