from flask import Flask
from flask import jsonify
from flask import request
import os
import subprocess
import sys
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def sh_script(script):
    script_dir=os.path.join(os.getcwd(),"scripts",script)
    read_script=os.popen(script_dir)
    read_script.read()
    print(read_script)
    return read_script

@app.route('/')
def index():
    return 'Hello diffusion'

#api for running sh scripts
@app.get('/scripts/<script>')
def script(script):
    try:
        if script=="finetune_gen.sh":
            print("finetune_gen.sh is running")
            sh_script(script)
            return jsonify({"message":"finetune_gen.sh script is running"}), 200
        elif script=="finetune_joint.sh":
            print("finetune_joint.sh is running")
            sh_script(script)
            return jsonify({"message":"finetune_joint.sh script is running"}), 200
        elif script=="finetune_real.sh":
            print("finetune_real.sh is running")
            sh_script(script)
            return jsonify({"message":"finetune_real.sh script is running"}), 200
        else:
            print(f"{script} is running")
            sh_script(script)
            return jsonify({"message":f"{script} script is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":str(e)}), 500

def args_validate():
    user_params = request.args.to_dict()
    args=[]
    for name,val in user_params.items():
        args.append("--{}".format(name))
        args.append(val)
    return subprocess.run(["python","sample.py"]+args)

#api for running with client parameters
@app.get("/sample")
def sample():
    try:
        args_validate()
        return jsonify({"message":"sample.py script is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":str(e)}), 500

#api for training with client parameters
@app.get("/train")
def train():
    try:
        args_validate()
        return jsonify({"message":"train.py script is running"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":str(e)}), 500

if __name__=="__main__":
    app.run(debug=True,host="localhost",port=5000)