#
# Copyright SCRIPT TACTICS LLC
#
from misb_0601_19.uas_datalink_local_set import UasDatalinkLocalSet
from misb_0601_19 import uas_datalink_local_set
from ..packet.packet import Packet


def parse_key_name(key):
    for enum_member in UasDatalinkLocalSet:
        if enum_member.value == key:
            return enum_member
    return None


def parse_fields(value, idx):
    if idx >= len(value):
        return []

    key = value[idx]
    length = value[idx + 1] if idx + 1 < len(value) else 0
    data = value[idx + 2 : idx + 2 + length]

    current_result = uas_datalink_local_set.parse_class(key, length, data)
    remaining_values = parse_fields(value=value, idx=(idx + 2 + length))
    return [current_result] + remaining_values


def parse_packet(value) -> Packet:
    return Packet(parse_fields(value=value, idx=0))


def parse_length(data, length_indicator, idx, data_len):
    value = b""
    if length_indicator:  # Long form (MSB is set)
        # BER Long format: first byte indicates length of the length field
        length_of_length_field = data[idx] & 0x7F  # Get the number of length bytes
        idx += 1  # Move past the first byte

        # Check if there are enough bytes for the length encoding
        if idx + length_of_length_field > data_len:
            print("Incomplete long-form length, skipping packet")
            return None

        # Now get the actual length, which spans the next 'length_of_length_field' bytes
        length = 0
        for _ in range(length_of_length_field):
            length = (length << 8) | data[idx]  # Shift and add the next byte to length
            idx += 1

        # Ensure there's enough data for the value
        if idx + length > data_len:
            print("Incomplete value, skipping packet")
            return None

        value = data[idx : idx + length]
        idx += length  # Move past the value
    else:  # Short form (MSB is not set)
        # BER Short format: length is encoded in the first byte (last 7 bits)
        length = data[idx] & 0x7F  # Get the last 7 bits
        idx += 1  # Move past the length byte

        # Ensure there's enough data for the value
        if idx + length > data_len:
            print("Incomplete value, skipping packet")
            return None

        value = data[idx : idx + length]

    return value


# Define a helper function to extract KLV data based on the Key-Length-Value format (16-byte key)
def parse_klv(data) -> Packet:
    idx = 0

    data_len = len(data)
    while idx < data_len:
        # Ensure there is enough data for the key (16 bytes) and the length byte
        if idx + 16 > data_len:
            print("Incomplete key, skipping packet")
            break

        # Extract the 16-byte key
        idx += 16  # Move past key.

        # Ensure there's enough data for the length byte and the value
        if idx >= data_len:
            print("Incomplete length field, skipping packet")
            break

        # Extract the length indicator
        length_indicator = data[idx] & 0x80  # Check MSB of the first length byte
        value = b""

        length = parse_length(
            data=data, length_indicator=length_indicator, idx=idx, data_len=data_len
        )
        parsed_value = parse_packet(value)
        idx += length  # Move past the value

    return parsed_value
