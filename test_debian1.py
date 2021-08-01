# we'll connect to devices and run commands a lot, so let's 
# put this component into its own function right off the bat.
def run_remote_command(host, cmd):
    output = host.run(cmd)
    return output

# here's the actual test function that pytest will execute. 
# we get the contents of /opt/TomStatus.txt from the remote
# device, and compare it to what we expect those contents to be
def test_file_contents(host):
    command = 'cat /opt/TomStatus.txt'
    filecontents = run_remote_command(host, command)
    assert filecontents.stdout.strip() == 'Tom is a goofball'

