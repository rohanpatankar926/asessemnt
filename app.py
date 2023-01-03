from flask import Flask
from flask import request
import os
import subprocess
from flask_cors import CORS
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

@app.get('scripts/<script>')
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


@app.get("/sample")
def sample():
    user_params = request.args.to_dict()
    args=[]
    for name,val in user_params.items():
        args.append("--{}".format(name))
        args.append(val)
    print(args)
    subprocess.run(["python","sample.py"]+args)
    return "sample.py script is running"

@app.route("/train")
def train():
    params = request.args.to_dict()
    args=[]
    for name,val in params.items():
        args.append("--{}".format(name))
        args.append(val)
    print(args)
    subprocess.run(["python","train.py"]+args)
    return "train.py script is running"