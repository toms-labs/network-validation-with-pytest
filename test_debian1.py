import json

# we'll connect to devices and run commands a lot, so let's 
# put this component into its own function right off the bat.
def run_remote_command(host, cmd):
    output = host.run(cmd)
    return output

# here's our first actual test function that pytest will execute. 
# we get the contents of /opt/TomStatus.txt from the remote
# device, and compare it to what we expect those contents to be
def test_file_contents(host):
    command = 'cat /opt/TomStatus.txt'
    filecontents = run_remote_command(host, command)
    assert filecontents.stdout.strip() == 'Tom is a goofball'

# second test, to see if debian-2 (at 192.168.1.2) has a BGP
# session in state "Established"
def test_bgp_peer_up(host):
    # FRR syntax to request output in json
    command = 'vtysh -c "show ip bgp summary json"'
    output = run_remote_command(host, command)
    # deserialize the json object found in output.stdout into the bgp_data dict
    bgp_data = json.loads(output.stdout)
    # find the session state in the dict and ensure that it meets our criteria
    assert bgp_data['ipv4Unicast']['peers']['192.168.1.2']['state'] == "Established"

