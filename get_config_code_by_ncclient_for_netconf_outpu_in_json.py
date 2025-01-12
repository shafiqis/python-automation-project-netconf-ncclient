from ncclient import manager
import xmltodict
import json

# Router connection details
router_details = {
    'host': '192.168.96.132',  # Router IP
    'port': 830,               # NETCONF port (default)
    'username': 'admin',       # Username
    'password': 'strong_password',    # Password
    'hostkey_verify': False,   # Disable host key verification
    'device_params': {'name': 'csr'}  # Device type (Cisco CSR)
}

try:
    # Connect to the router using ncclient
    with manager.connect(**router_details) as rtr_mgr:
        print("Connected to the router.")

        # Fetch the running configuration
        print("Fetching the running configuration...")
        output = rtr_mgr.get_config('running').data_xml

        # Convert XML to Python dictionary
        config_dict = xmltodict.parse(output)

        # Convert the dictionary to JSON
        config_json = json.dumps(config_dict, indent=4)

        # Save the JSON configuration to a file
        with open('router_config.json', 'w') as json_data:
            json_data.write(config_json)

        print("Running configuration saved to 'router_config.json' in JSON format.")

except Exception as e:
    print(f"An error occurred: {e}")

