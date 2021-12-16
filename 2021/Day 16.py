#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np

def handle_packet(packet, s, e):
    return (packet[s:e], packet[e:])

def parse_packet_a(packet, versions, inner_call=0):
    packet_length = len(packet)
    packet_version, packet = handle_packet(packet, 0, 3)
    packet_type, packet = handle_packet(packet, 0, 3)
    versions.append(int(packet_version, 2))
    if packet_type == '100':
        _, packet = handle_literal_value(packet)
    else:
        packet_length_type, packet = handle_packet(packet, 0, 1)
        if packet_length_type == '1':
            n_subpackets, packet = handle_packet(packet, 0, 11)
            n_subpackets = int(n_subpackets, 2)
            for _ in range(n_subpackets):
                packet, versions = parse_packet_a(packet, versions, 1)
        else:
            n_bits, packet = handle_packet(packet, 0, 15)
            n_bits = int(n_bits, 2)
            current_packet_length = len(packet)
            new_packet = packet
            while len(new_packet) > current_packet_length-n_bits:
                new_packet, versions = parse_packet_a(new_packet, versions, 1)
            packet = new_packet
    if inner_call:
        return (packet, versions)
    else:
        padding = (4 - (packet_length-len(packet)) % 4 ) % 4
        packet = packet[padding:]
        if packet:
            if int(packet, 2) == 0:
                return (packet, versions)
            else:
                parse_packet_a(packet, versions)
        else:
            return (packet, versions)

def parse_packet_b(packet, inner_call=0):
    packet_length = len(packet)
    _, packet = handle_packet(packet, 0, 3)
    packet_type, packet = handle_packet(packet, 0, 3)
    if packet_type == '100':
        value, packet = handle_literal_value(packet)
    else:
        packet_length_type, packet = handle_packet(packet, 0, 1)
        if packet_length_type == '1':
            n_subpackets, packet = handle_packet(packet, 0, 11)
            n_subpackets = int(n_subpackets, 2)
            sub_values = []
            for _ in range(n_subpackets):
                packet, sub_value = parse_packet_b(packet, 1)
                sub_values.append(sub_value)
            value = handle_values(packet_type, sub_values)
        else:
            n_bits, packet = handle_packet(packet, 0, 15)
            n_bits = int(n_bits, 2)
            current_packet_length = len(packet)
            new_packet = packet
            sub_values = []
            while len(new_packet) > current_packet_length-n_bits:
                new_packet, sub_value = parse_packet_b(new_packet, 1)
                sub_values.append(sub_value)
            value = handle_values(packet_type, sub_values)
            packet = new_packet
    if inner_call:
        return (packet, value)
    else:
        padding = (4 - (packet_length-len(packet)) % 4 ) % 4
        packet = packet[padding:]
        if packet:
            if int(packet, 2) == 0:
                return (packet, value)
            else:
                parse_packet_b(packet, value)
        else:
            return (packet, value)
    return True

def handle_values(type, sub_values):
    type = int(type, 2)
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
    _, versions = parse_packet_a(bits, [])
    return sum(versions)

def b(data):
    packet = data[0]
    bits = str(bin(int(packet, 16))[2:].zfill(len(packet)*4))
    _, value = parse_packet_b(bits, [])
    return value

#run script
if __name__ == '__main__': 
    main(year=2021, day=16, exampleOutput={'A':14, 'B':3}, funcs={'a': a, 'b': b})