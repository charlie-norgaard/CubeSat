import serial
import telemetry_packets as tlm
import command_packets as cmd

def get_cmds():

    # Initialize variables
    serial_port = serial.Serial(port='COM2', baudrate=9600, timeout=None)
    payload_size_data = serial_port.read(4)
    payload_size = int.from_bytes(payload_size_data, 'big') // 8
    payload = serial_port.read_until(size=payload_size+4)
    print(f'Total Payload Size: {payload_size} bytes')


    # Return the data
    print('\n--- Start Payload ---\n')
    print(payload)
    print('\n--- End Payload ---\n')
    return payload, payload_size_data


# UPDATE: Trying TERMINATED Protocol, delineate packets on termination character
def uplink():

    # Get the data from the serial port
    print('\n* GRABBING DATA *\n')
    payload, payload_size = get_cmds()
    nack_array = [0, 0, 0, 0]

    # Parse the data into packets
    print('* PROCESSING PACKETS *\n')
    term_char = b'\xab\xcd'
    packets = payload.split(term_char)
    for i in range(len(packets)):
        print(f'Packet {i}:', packets[i], '\n')

    # Unpack the command packets
    print('----- PAYLOAD CONTENTS -----\n')
    for packet in packets:
        pkt_id = int.from_bytes(packet[0:4], 'big')
        if pkt_id == 1:
            header_ack = cmd.header(packet, payload_size) # boolean
            if header_ack == False:
                nack_array[pkt_id - 1] = 1
            print('--------------------')
        elif pkt_id == 2:
            com_ack = cmd.com(packet) # boolean
            if com_ack == False:
                nack_array[pkt_id - 1] = 1
            print('--------------------')
        elif pkt_id == 3:
            gnc_ack = cmd.gnc(packet) # boolean
            if gnc_ack == False:
                nack_array[pkt_id - 1] = 1
            print('--------------------')
        elif pkt_id == 4:
            img_ack = cmd.img(packet) # boolean
            if img_ack == False:
                nack_array[pkt_id - 1] = 1
            print('--------------------')

    print('\n* NACK PROTOCOL *\n')
    print(f' nack_array = {nack_array}')

    # How and where should I store / return the nack array
    


def downlink():

    # Serial Port
    ser = serial.Serial('COM1')
    
    # Downlink Payload
    beacon = tlm.beacon()
    header = tlm.header()
    eps = tlm.eps()
    com = tlm.com()
    gnc = tlm.gnc()
    soar = tlm.soar()
    # img = tlm.img()
    
    # Send the packets
    # ser.write(beacon)
    ser.write(header)
    ser.write(eps)
    ser.write(com)
    ser.write(gnc)
    ser.write(soar)
    # ser.write(img)


def main():
    # get_data()
    uplink()
    # downlink()


if __name__=='__main__':
    main()