import os
import json

config_path = '/home/root/papis/config/config.json'

default_config_path = '/home/root/papis/config/defaultConfig/config.json'

if os.path.exists(config_path):
    fileSize = os.path.getsize(config_path)
    fileSizeDefault = os.path.getsize(default_config_path)

    if fileSize > 0:
        if fileSize == fileSizeDefault:
            pass

        else:
            with open(default_config_path, 'r') as f_default:
                with open(config_path, 'w') as f:
                    f.write(f_default.read())

    else:
        with open(default_config_path, 'r') as f_default:
                with open(config_path, 'w') as f:
                    f.write(f_default.read())

else:
    print("File does not exist")  # or you can raise an exception here
    try:
        os.path.join('/home/root/papis/config/','config.json')
        with open(default_config_path, 'r') as f_default:
            with open(config_path, 'w') as f:
                f.write(f_default.read())
        
        print("config.json file has been created & replaced successfully!!!")
    
    except Exception as e:
        print(f"Error: {e}")
        