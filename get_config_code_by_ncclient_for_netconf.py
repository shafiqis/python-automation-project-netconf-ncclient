from ncclient import manager

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

        # Save the configuration to a file
        with open('router_config.xml', 'w') as xml_data:
            xml_data.write(output)

        print("Running configuration saved to 'router_config.xml'.")

except Exception as e:
    print(f"An error occurred: {e}")
