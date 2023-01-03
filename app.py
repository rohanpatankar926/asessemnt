from flask import Flask
from flask import jsonify
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
    try:
        if script=="finetune_gen.sh":
            print("finetune_gen.sh is running")
            Call().sh_script(script)
            return jsonify({"message":"finetune_gen.sh script is running"}), 200
        elif script=="finetune_joint.sh":
            print("finetune_joint.sh is running")
            Call().sh_script(script)
            return jsonify({"message":"finetune_joint.sh script is running"}), 200
        elif script=="finetune_real.sh":
            print("finetune_real.sh is running")
            Call().sh_script(script)
            return jsonify({"message":"finetune_real.sh script is running"}), 200
        else:
            print(f"{script} is running")
            Call().sh_script(script)
            return jsonify({"message":f"{script} script is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":str(e)}), 500


@app.get("/sample")
def sample():
    try:
        user_params = request.get_json()
        args=[]
        for name,val in user_params.items():
            args.append("--{}".format(name))
            args.append(val)
        print(args)
        subprocess.run(["python","sample.py"]+args)
        return jsonify({"message":"sample.py script is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":str(e)}), 500

@app.get("/train")
def train():
    try:
        params = request.get_json()
        args=[]
        for name,val in params.items():
            args.append("--{}".format(name))
            args.append(val)
        print(args)
        subprocess.run(["python","train.py"]+args)
        return jsonify({"message":"train.py script is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":str(e)}), 500