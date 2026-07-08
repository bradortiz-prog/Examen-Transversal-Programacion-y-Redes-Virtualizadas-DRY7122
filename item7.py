from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.117",
    "username": "cisco",
    "password": "cisco123!"
}

conexion = ConnectHandler(**router)

print("=" * 60)
print("SHOW IP INTERFACE BRIEF")
print("=" * 60)

print(conexion.send_command("show ip interface brief"))

print("\n" + "=" * 60)
print("SHOW RUNNING-CONFIG")
print("=" * 60)

print(conexion.send_command("show running-config"))

print("\n" + "=" * 60)
print("SHOW VERSION")
print("=" * 60)

print(conexion.send_command("show version"))

conexion.disconnect()
