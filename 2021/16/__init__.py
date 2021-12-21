from functools import reduce

from pyutils import *


def parse(lines):
    return Packet([0, ''.join(bin(int(char, 16))[2:].zfill(4) for char in lines[0])])


def consume_raw(bits, n):
    value = ''.join(bits[1][bits[0]+j] for j in range(n))
    bits[0] += n
    return value


def consume_int(bits, n):
    return int(consume_raw(bits, n), 2)


class Packet:
    def __init__(self, bits):
        self.version = consume_int(bits, 3)
        self.type = consume_int(bits, 3)
        self.subpackets = []

        if self.type != 4:
            length_type_id = consume_int(bits, 1)
            if length_type_id == 0:
                subpackets_length = consume_int(bits, 15)
                start = bits[0]
                while (bits[0]-start) < subpackets_length:
                    self.subpackets.append(Packet(bits))
            else:
                self.subpackets_number = consume_int(bits, 11)
                while len(self.subpackets) < self.subpackets_number:
                    self.subpackets.append(Packet(bits))

        if self.type == 0:
            self.value = sum(p.value for p in self.subpackets)
        elif self.type == 1:
            self.value = self.subpackets[0].value
            for subpacket in self.subpackets[1:]:
                self.value *= subpacket.value
        elif self.type == 2:
            self.value = min(p.value for p in self.subpackets)
        elif self.type == 3:
            self.value = max(p.value for p in self.subpackets)
        elif self.type == 4:
            value, chunk = '', consume_raw(bits, 5)
            while chunk[0] == '1':
                value += chunk[1:]
                chunk = consume_raw(bits, 5)
            value += chunk[1:]
            self.value = int(value, 2)
        elif self.type == 5:
            self.value = int(
                self.subpackets[0].value > self.subpackets[1].value)
        elif self.type == 6:
            self.value = int(
                self.subpackets[0].value < self.subpackets[1].value)
        elif self.type == 7:
            self.value = int(
                self.subpackets[0].value == self.subpackets[1].value)


@expect({'8A004A801A8002F478': 16, '620080001611562C8802118E34': 12, 'C0015000016115A2E0802F182340': 23, 'A0016C880162017C3686B18A3D4780': 31})
def solve1(packet):
    q, versions_total = [packet], 0
    while q:
        p = q.pop()
        versions_total += p.version
        if p.subpackets:
            q.extend(p.subpackets)
    return versions_total


@expect({'C200B40A82': 3, '04005AC33890': 54, '880086C3E88112': 7, 'CE00C43D881120': 9, 'D8005AC2A8F0': 1, 'F600BC2D8F': 0, '9C005AC2F8F0': 0, '9C0141080250320F1802104A08': 1})
def solve2(packet):
    return packet.value
