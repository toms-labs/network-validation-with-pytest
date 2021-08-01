def run_remote_command(host, command):
    '''
    Function to connect to a remote host, run a command, and return its output.
    This function is consumed by pytest test functions, and uses the pytest-testinfra
    plugin to do its work.
    '''
    output = host.run(command)
    return output

def test_file_contents(host):
    '''
    Use pytest to compare the contents of a file on a remote host's filesystem
    to a standard string that we are expecting.

        Parameters:
            host (string): the remote host to connect to. This will be connected to
                with the pytest-testinfra plugin. The host parameter will be
                supplied when invoking pytest at the CLI. 

                Example:

                pytest test_debian1.py --hosts 100.66.12.202
    '''
    