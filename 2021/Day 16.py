#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np

def handle_packet(packet, s, e):
    return (packet[s:e], packet[e:])

def parse_packet(packet, versions, inner_call=0):
    packet_length = len(packet)
    packet_version, packet = handle_packet(packet, 0, 3)
    packet_type, packet = handle_packet(packet, 0, 3)
    packet_type = int(packet_type, 2)
    versions.append(int(packet_version, 2))
    if packet_type == 4:
        value, packet = handle_literal_value(packet)
    else:
        packet_length_type, packet = handle_packet(packet, 0, 1)
        if packet_length_type == '1':
            n_subpackets, packet = handle_packet(packet, 0, 11)
            n_subpackets = int(n_subpackets, 2)
            sub_values = []
            for _ in range(n_subpackets):
                packet, versions, sub_value = parse_packet(packet, versions, 1)
                sub_values.append(sub_value)
            value = handle_values(packet_type, sub_values)
        else:
            n_bits, packet = handle_packet(packet, 0, 15)
            n_bits = int(n_bits, 2)
            current_packet_length = len(packet)
            sub_values = []
            while len(packet) > current_packet_length-n_bits:
                packet, versions, sub_value = parse_packet(packet, versions, 1)
                sub_values.append(sub_value)
            value = handle_values(packet_type, sub_values)
    if inner_call:
        return (packet, versions, value)
    else:
        padding = (4 - (packet_length-len(packet)) % 4 ) % 4
        packet = packet[padding:]
        if packet:
            if int(packet, 2) == 0:
                return (packet, versions, value)
            else:
                parse_packet(packet, versions)
        else:
            return (packet, versions, value)

def handle_values(type, sub_values):
    if type == 0:
        value = sum(sub_values)
    elif type == 1:
        value = np.prod(sub_values)
    elif type == 2:
        value = min(sub_values)
    elif type == 3:
        value = max(sub_values)
    elif type == 5:
        value = int(sub_values[0] > sub_values[1])
    elif type == 6:
        value = int(sub_values[0] < sub_values[1])
    elif type == 7:
        value = int(sub_values[0] == sub_values[1])
    else:
        value = 0
    return value

def handle_literal_value(packet):
    last, packet = handle_packet(packet, 0, 1)
    value, packet = handle_packet(packet, 0, 4)
    while last == '1':
        last, packet = handle_packet(packet, 0, 1)
        val, packet = handle_packet(packet, 0, 4)
        value += val
    return (int(value, 2), packet)

#day calculation
def a(data):
    packet = data[0]
    bits = str(bin(int(packet, 16))[2:].zfill(len(packet)*4))
    _, versions, _ = parse_packet(bits, [])
    return sum(versions)

def b(data):
    packet = data[0]
    bits = str(bin(int(packet, 16))[2:].zfill(len(packet)*4))
    _, _, value = parse_packet(bits, [])
    return value

#run script
if __name__ == '__main__': 
    main(year=2021, day=16, exampleOutput={'A':14, 'B':3}, funcs={'a': a, 'b': b})