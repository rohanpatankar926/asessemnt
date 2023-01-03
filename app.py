from flask import Flask
from flask import request
from sample import main
import os
from flask_cors import CORS
from flask import main
app = Flask(__name__)
CORS(app)

class Call:
    def sh_script(self,script):
        script_dir=os.path.join(os.getcwd(),"scripts",script)
        read_script=os.popen(script_dir)
        read_script.read()
        print(read_script)
        return read_script
        
@app.route('/')
def index():
    return 'Hello diffusion'

@app.get('/<script>')
def script(script):
    if script=="finetune_gen.sh":
        print("finetune_gen.sh is running")
        Call().sh_script(script)
        return "done executing finetune_gen.sh"
    elif script=="finetune_joint.sh":
        print("finetune_joint.sh is running")
        Call().sh_script(script)
        return "done executing finetune_joint.sh"
    elif script=="finetune_real.sh":
        print("finetune_real.sh is running")
        return Call().sh_script(script)
    else:
        print(f"{script} is running")
        Call().sh_script(script)
        return f"done executing {script}"


@app.post("/sample")
def sample():
    print("sample is running")
    return main()