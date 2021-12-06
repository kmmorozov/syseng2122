#!/bin/bash 

IPT=/sbin/iptables

#flush 

$IPT -F 

$IPT -P INPUT DROP
$IPT -P OUTPUT DROP
$IPT -P FORWARD DROP

$IPT  -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
$IPT  -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

$IPT -A INPUT -i lo -j ACCEPT
$IPT -A OUTPUT -o lo -j ACCEPT 



$IPT -A INPUT -p tcp --dport 22 -j ACCEPT
$IPT -A OUTPUT -p tcp --sport 22 -j ACCEPT


$IPT -A INPUT -p tcp --dport 80 -j ACCEPT
$IPT -A OUTPUT -p tcp --sport 80 -j ACCEPT


$IPT -A OUTPUT -p udp --dport 53 -j ACCEPT 
$IPT -A INPUT -p udp --sport 53 -j ACCEPT 

$IPT -A OUTPUT -p tcp --dport 80 -j ACCEPT
$IPT -A INPUT -p tcp --sport 80 -j ACCEPT

$IPT -A OUTPUT -p tcp --dport 443 -j ACCEPT
$IPT -A INPUT -p tcp --sport 443 -j ACCEPT






