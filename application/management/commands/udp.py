from django.core.management.base import BaseCommand
from django.utils import timezone
# -*- coding: utf-8 -*-
import os
import sys
import socket


class Command(BaseCommand):

        msgFromClient       = "Hello UDP Server"
        bytesToSend         = str.encode(msgFromClient)
        serverAddressPort   = ("192.168.1.100", 4370)
        bufferSize          = 600 
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)
        