import subprocess

def set_user_policy():
    _, status = run_code("admin", "policy", "add", "avlcloud/", "test_policy", "D:\\temp\\tmp_policy.json")
    if status:
        return
    else:
        raise Exception("error on execute set_user_policy")
    
def run_code(*args):
    try:

        status = True
        # popenargs = [settings.MINIO_COMMAND_PATH]
        popenargs = ["D:\\mc\\mc.exe"]
        popenargs.extend(args)
        # print(' '.join(popenargs))
        output = subprocess.check_output(popenargs,
                                            universal_newlines=True,
                                            stderr=subprocess.STDOUT,
                                            timeout=30,
                                            # shell=settings.MINIO_COMMAND_OUTPUT_SHELL)
                                            shell=True)
    except subprocess.CalledProcessError as e:
        output, status = e.output, False
    except subprocess.TimeoutExpired as e:
        output, status = '\r\n'.join(['Time Out!!!', e.output]), False
    print(output)
    return output, status

set_user_policy()