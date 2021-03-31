import mp_checker as mp

status = mp.mp_validate()
if status == 0:
    print('0 exit')
    import subprocess
    print('sftp uploading...')
    subprocess.call('chmod +x mediaplan_up.sh', shell=True)
    subprocess.call('./mediaplan_up.sh >> log.log', shell=True)
    print('succesful load')
