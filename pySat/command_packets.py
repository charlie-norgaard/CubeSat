import communication_protocols as protocol

def header(packet, payload_size):

    # Grab and decode packet fields
    id = int.from_bytes(packet[0:4], byteorder='big')
    length = int.from_bytes(packet[4:8], byteorder='big')
    message = packet[8:34].decode()
    hmac = packet[34:98].decode()
    nack_array = list(bytearray(packet[98:122:4]))
    crc = int.from_bytes(packet[122:], byteorder='big')

    # Show packet contents
    print('\nHEADER COMMAND PACKET\n')
    print('Packet ID:', id)
    print('Packet Length:', length)
    print('Header Message:', message)
    print('Packet HMAC:', hmac)
    print('NACK Array:', nack_array)
    print('Packet CRC:', crc)

    # Check HMAC
    print('\n* MESSAGE AUTHENTICATION CHECK *')
    protocol.check_hmac(packet[8:34], hmac)
    
    # Check CRC
    print('\n* CRC VERIFICATION CHECK *')
    return protocol.check_crc(payload_size + packet[0:122], crc, id)

def com(packet):

    # Grab and decode packet fields
    id = int.from_bytes(packet[0:4], byteorder='big')
    length = int.from_bytes(packet[4:8], byteorder='big')
    reconfig_radio = int.from_bytes(packet[8:12], byteorder='big')
    check_health = int.from_bytes(packet[12:16], byteorder='big')
    shut_down_trans = int.from_bytes(packet[16:20], byteorder='big')
    req_payload = int.from_bytes(packet[20:24], byteorder='big')
    req_image = int.from_bytes(packet[24:28], byteorder='big')
    check_ant_status = int.from_bytes(packet[28:32], byteorder='big')
    enter_data_mode = int.from_bytes(packet[32:36], byteorder='big')
    enter_cmd_mode = int.from_bytes(packet[36:40], byteorder='big')
    dep_ant_1 = int.from_bytes(packet[40:44], byteorder='big')
    dep_ant_2 = int.from_bytes(packet[44:48], byteorder='big')
    crc = int.from_bytes(packet[48:], byteorder='big')

    cmd_dict = {0 : 'NO', 1 : 'YES'}

    # Show packet contents
    print('\nCOM COMMAND PACKET\n')
    print('Packet ID:', id)
    print('Packet Length:', length)
    print('Reconfigure Radio:', cmd_dict.get(reconfig_radio))
    print('Check Radio Health:', cmd_dict.get(check_health))
    print('Shut Down Transmissions:', cmd_dict.get(shut_down_trans))
    print('Request Payload:', cmd_dict.get(req_payload))
    print('Request Image:', cmd_dict.get(req_image))
    print('Check Antenna Status:', cmd_dict.get(check_ant_status))
    print('Enter Data Mode:', cmd_dict.get(enter_data_mode))
    print('Enter Command Mode:', cmd_dict.get(enter_cmd_mode))
    print('Deploy Antenna (Alg 1):', cmd_dict.get(dep_ant_1))
    print('Deploy Antenna (Alg 2):', cmd_dict.get(dep_ant_2))
    print('Packet CRC:', crc)

    # Check CRC
    print('\n* CRC VERIFICATION CHECK *')
    return protocol.check_crc(packet[0:48], crc+1, id)


def gnc(packet):
    # Grab and decode packet fields
    id = int.from_bytes(packet[0:4], byteorder='big')
    length = int.from_bytes(packet[4:8], byteorder='big')
    orbit_tle_1 = int.from_bytes(packet[8:16], byteorder='big')
    orbit_tle_2 = int.from_bytes(packet[16:24], byteorder='big')
    orbit_tle_3 = int.from_bytes(packet[24:32], byteorder='big')
    orbit_tle_4 = int.from_bytes(packet[32:40], byteorder='big')
    orbit_tle_5 = int.from_bytes(packet[40:48], byteorder='big')
    orbit_tle_6 = int.from_bytes(packet[48:56], byteorder='big')
    orbit_tle_7 = int.from_bytes(packet[56:64], byteorder='big')
    orbit_tle_8 = int.from_bytes(packet[64:72], byteorder='big')
    orbit_tle_9 = int.from_bytes(packet[72:80], byteorder='big')
    met_utc_s = int.from_bytes(packet[80:88], byteorder='big')
    met_soar_utc_s = int.from_bytes(packet[88:96], byteorder='big')
    quat_soar_cmd_1 = int.from_bytes(packet[96:104], byteorder='big')
    quat_soar_cmd_2 = int.from_bytes(packet[104:112], byteorder='big')
    quat_soar_cmd_3 = int.from_bytes(packet[112:120], byteorder='big')
    quat_soar_cmd_4 = int.from_bytes(packet[120:128], byteorder='big')
    set_targ_lat = int.from_bytes(packet[128:136], byteorder='big')
    set_targ_lon = int.from_bytes(packet[136:144], byteorder='big')
    set_targ_alt = int.from_bytes(packet[144:152], byteorder='big')
    init_gnc_mode = int.from_bytes(packet[152:156], byteorder='big')
    en_crit_power_mode = int.from_bytes(packet[156:160], byteorder='big')
    en_low_power_mode = int.from_bytes(packet[160:164], byteorder='big')
    en_auto_point = int.from_bytes(packet[164:168], byteorder='big')
    en_imaging = int.from_bytes(packet[168:172], byteorder='big')
    en_soar = int.from_bytes(packet[172:176], byteorder='big')
    tri_override = int.from_bytes(packet[176:180], byteorder='big')
    crc = int.from_bytes(packet[180:], byteorder='big')

    cmd_dict = {0 : 'NO', 1 : 'YES'}

    # Show packet contents
    print('\nGNC COMMAND PACKET\n')
    print('Packet ID:', id)
    print('Packet Length:', length)
    print('Orbit Telemetry 1 (Year):', orbit_tle_1)
    print('Orbit Telemetry 2 (Days Since Epoch):', orbit_tle_2)
    print('Orbit Telemetry 3 (Bstar "Drag"):', orbit_tle_3)
    print('Orbit Telemetry 4 (Inclination):', orbit_tle_4)
    print('Orbit Telemetry 5 (RAAN):', orbit_tle_5)
    print('Orbit Telemetry 6 (Eccentricity):', orbit_tle_6)
    print('Orbit Telemetry 7 (AOP):', orbit_tle_7)
    print('Orbit Telemetry 8 (Mean Anomaly):', orbit_tle_8)
    print('Orbit Telemetry 9 (Mean Motion):', orbit_tle_9)
    print('MET UTC S (Event Time):', met_utc_s)
    print('MET UTC S (Event Time):', met_utc_s)
    print('MET SOAR UTC S (SOAR Event Time):', met_soar_utc_s)
    print('Quat Soar Command 1:', quat_soar_cmd_1)
    print('Quat Soar Command 2:', quat_soar_cmd_2)
    print('Quat Soar Command 3:', quat_soar_cmd_3)
    print('Quat Soar Command 4:', quat_soar_cmd_4)
    print('Set Target Latitude:', set_targ_lat)
    print('Set Target Longitude:', set_targ_lon)
    print('Set Target Altitude:', set_targ_alt)
    print('Initialize GNC Mode:', cmd_dict.get(init_gnc_mode))
    print('Enable Critical Power Mode:', cmd_dict.get(en_crit_power_mode))
    print('Enable Low Power Mode:', cmd_dict.get(en_low_power_mode))
    print('Enable Auto Pointing:', cmd_dict.get(en_auto_point))
    print('Enable Imaging:', cmd_dict.get(en_imaging))
    print('Enable SOAR:', cmd_dict.get(en_soar))
    print('Peform Triad Override:', cmd_dict.get(tri_override))
    print('Packet CRC:', crc)

    # Check CRC
    print('\n* CRC VERIFICATION CHECK *')
    return protocol.check_crc(packet[0:180], crc, id)


def img(packet):
    # Grab and decode packet fields
    id = int.from_bytes(packet[0:4], byteorder='big')
    length = int.from_bytes(packet[4:8], byteorder='big')
    check_stat = int.from_bytes(packet[8:12], byteorder='big')
    take_pic = int.from_bytes(packet[12:16], byteorder='big')
    get_pic_size = int.from_bytes(packet[16:20], byteorder='big')
    get_pic = int.from_bytes(packet[20:24], byteorder='big')
    set_pic_cont = int.from_bytes(packet[24:28], byteorder='big')
    set_pic_bright = int.from_bytes(packet[28:32], byteorder='big')
    set_pic_expo = int.from_bytes(packet[32:36], byteorder='big')
    set_slp_time = int.from_bytes(packet[36:40], byteorder='big')
    crc = int.from_bytes(packet[40:], byteorder='big')

    cmd_dict = {0 : 'NO', 1 : 'YES'}

    # Show packet contents
    print('\nIMG COMMAND PACKET\n')
    print('Packet ID:', id)
    print('Packet Length:', length)
    print('Check Status:', cmd_dict.get(check_stat))
    print('Take Picture:', cmd_dict.get(take_pic))
    print('Get Picture Size:', cmd_dict.get(get_pic_size))
    print('Get Picture:', cmd_dict.get(get_pic))
    print('Set Picture Contour:', set_pic_cont)
    print('Set Picture Brightness:', set_pic_bright)
    print('Set Picture Exposure:', set_pic_expo)
    print('Set Sleep Time:', set_slp_time)
    print('Packet CRC:', crc)

    # Check CRC
    print('\n* CRC VERIFICATION CHECK *')
    return protocol.check_crc(packet[0:40], crc+1, id)


def main():
    # header()
    # com()
    # gnc()
    # img()
    pass


if __name__=='__main__':
    main()