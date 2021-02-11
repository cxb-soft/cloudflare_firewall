from flask import Flask
from flask import request
import json
import time
import os

def load_json(filename):
    f = open(filename)
    content = json.load(f)
    f.close()
    return content

def write_json(filename,content):
    content = json.dumps(content)
    f = open(filename,"w")
    f.write(content)
    f.close()

def unblock(ip):
    os.system("iptables -D INPUT -s %s -j DROP"%ip)
    configs = load_json("config.json")
    configs['ips'].remove(ip)
    write_json("config.json",configs)

def change_password_func(new_password):
    configs = load_json("config.json")
    configs['password'] = new_password
    write_json("config.json",configs)

def time_change_func(newtime):
    configs = load_json("config.json")
    configs['time'] = newtime
    write_json("config.json",configs)

def status(method):
    configs = load_json("config.json")
    if(method == "start"):
        if(configs['status'] == "on"):
            pass
        else:
            configs['status'] = "on"
            write_json("config.json",configs)
            os.system("nohup python3 main.py &")
    else:
        if(configs['status'] == "off"):
            pass
        else:
            configs['status'] = "off"
    write_json("config.json",configs)


app = Flask(__name__)

configs = load_json("config.json")
port = configs['port']

# Ping check online
@app.route('/online',methods=['GET'])
def online():
    return {
        "success" : True,
        "online" : True
    }
# Set config
@app.route('/config',methods=['POST'])
def config():
    postdata = request.form['config']
    postdata = json.loads(postdata)
    write_json("config.json",postdata)
    print(postdata)
    return postdata

# 获取当前配置
@app.route('/config_read',methods=['GET'])
def config_read():
    configs = load_json("config.json")
    password = configs['password']
    reqpass = request.args.get("password")
    if(reqpass == password):
        return {
            "success" : True,
            "detail" : configs
        }
    else:
        return {
            "success" : False,
            "error" : "Auth error : Password incorrect!"
        }


# 开启防火墙服务
@app.route('/start',methods=['GET'])
def start():
    configs = load_json("config.json")
    password = configs['password']
    reqpass = request.args.get("password")
    if(reqpass == password):
        status("start")
        return {
            "success" : True,
            "msg" : "Firewall is start now"
        }
    else:
        return {
            "success" : False,
            "error" : "Auth error : Password incorrect!"
        }



# 关闭防火墙服务
@app.route('/stop',methods=['GET'])
def stop():
    configs = load_json("config.json")
    password = configs['password']
    reqpass = request.args.get("password")
    if(reqpass == password):
        status("stop")
        return {
            "success" : True,
            "msg" : "Firewall is stop now"
        }
    else:
        return {
            "success" : False,
            "error" : "Auth error : Password incorrect!"
        }


# 改密码
@app.route('/change_password',methods=['GET'])
def change_password():
    configs = load_json("config.json")
    password = configs['password']
    reqpass = request.args.get("password")
    newpassword = request.args.get("newpassword")
    if(reqpass == password):
        change_password_func(newpassword)
        return {
            "success" : True,
            "msg" : "Password change successful ."
        }
    else:
        return {
            "success" : False,
            "error" : "Old password incorrect ."
        }

# 改防火墙检测时间
@app.route('/time_change',methods=['GET'])
def time_change():
    configs = load_json("config.json")
    password = configs['password']
    reqpass = request.args.get("password")
    if(reqpass == password):
        newtime = request.args.get("newtime")
        newtime = int(newtime)
        time_change_func(newtime)
        return {
            "success" : True,
            "msg" : "Time changed ."
        }
    else:
        return {
            "success" : False,
            "error" : "Auth error : Password incorrect!"
        }

# 解封IP
@app.route('/unblock_ip',methods=['GET'])
def unblock_ip():
    configs = load_json("config.json")
    password = configs['password']
    reqpass = request.args.get("password")
    if(reqpass == password):
        unblock_target = request.args.get("ip")
        unblock(unblock_target)
        return {
            "success" : True,
            "ip" : unblock_target
        }
    else:
        return {
            "success" : False,
            "error" : "Auth error : Password incorrect!"
        }

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=port)
