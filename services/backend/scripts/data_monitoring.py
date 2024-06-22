def monitorar_dados():
    pressure_change_limit = 1110 #valores alterados para permanecerem estaveis 
    temperature_change_limit = 28  #valores alterados para permanecerem estaveis 
    pressure_range = (1000, 1100)
    temperature_range = (21, 27)

    data_array = get_datas()  

    while True:
        data_array = get_datas(data_array)  

        status_pressure = compare_pressure_data(data_array, pressure_change_limit)
        status_temperature = compare_temperature_data(data_array, temperature_change_limit)
        range_check = check_data_within_range(data_array, pressure_range, temperature_range)

        send_notification(f'Status pressão: {status_pressure}')
        send_notification(f'Status temperatura: {status_temperature}')
        send_notification(range_check)

        time.sleep(5) 

monitorar_dados()