import mp_checker as mp

status = mp.mp_validate()
if status == 0:
    print('0 exit')
    import subprocess
    subprocess.call('chmod +x mediaplan_up.sh', shell=True)
    print('sftp uploading...')
    subprocess.call('chmod +x mediaplan_up.sh', shell=True)
    subprocess.call('./mediaplan_up.sh >> log.log', shell=True)
    print('succesful load')
    print('---matchrate evaluation:')
    subprocess.call('cd ..', shell=True)
    subprocess.call('./matchrate_upd.sh >> match.log', shell=True)
