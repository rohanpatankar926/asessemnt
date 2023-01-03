from flask import Flask
from flask import request
# from sample import main
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

class Call:
    def sh_script(self,script):
        # os.system(f"chmod +x {script}")
        script_dir=os.path.join(os.getcwd(),script)
        read_script=os.popen(script_dir)
        read_script.read()
        print(read_script)
        return read_script
        
@app.route('/')
def index():
    return 'Hello diffusion'

# @app.get('/<script>')
# def script(script):
#     if script=="finetune_gen.sh":
#         print("finetune_gen.sh is running")
#         return Call().sh_script(script)
#     elif script=="finetune_joint.sh":
#         print("finetune_joint.sh is running")
#         return Call().sh_script(script)
#     elif script=="finetune_real.sh":
#         print("finetune_real.sh is running")
#         return Call().sh_script(script)
#     elif script:
#         print(f"{script} is running")
#         Call().sh_script(script)
#         return "done"

import subprocess
@app.get("/sample")
def sample():
    print("sample is running")
    a=request.args.getlist("parameters")
    print(a)
    params=f"--{a}"
    print("=========",params)
    subprocess.run(["python","d.py",params]+a)
    print(a)
    return a
@app.route('/run_script')
def run_script():
    # Get the list of parameters
    params = request.args.to_dict()

    # Create a list of command-line arguments for the script
    args = []
    for name, value in params.items():
        # Append the parameter name and value to the list
        args.append("--{}".format(name))
        args.append(value)
    print(args)

    # Run the script with the provided parameters
    subprocess.run(["python", "d.py"] + args)

    return "Script executed successfully!"

if __name__ == '__main__':
    app.run()