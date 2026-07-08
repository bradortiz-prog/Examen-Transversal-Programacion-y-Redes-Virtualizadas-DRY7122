from ncclient import manager

router = {
    "host": "192.168.56.117",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False,
    "allow_agent": False,
    "look_for_keys": False,
    "timeout": 30
}

config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Ortiz</hostname>

    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>

  </native>
</config>
"""

try:
    with manager.connect(**router) as m:
        respuesta = m.edit_config(
            target="running",
            config=config
        )

        print("\n====================================")
        print("CONFIGURACION APLICADA CORRECTAMENTE")
        print("====================================")
        print(respuesta)

except Exception as e:
    print("\nERROR:")
    print(e)
