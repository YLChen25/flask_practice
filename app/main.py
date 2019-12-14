from flask import Flask

app = Flask(__name__) # Let the flask can find the module name

@app.route('/', methods = ['GET'])
def hello_world():
    return "hello world"

@app.route('/read/<name>', methods = ['GET'])
def read_data(name):
    return "Hi " + name  

@app.route('/write/', methods = ['GET'])
def write_data():
    return "write"

# Try some convert
"""
string 字符串
int 整形
float 浮点型
path 接受路径，接收的时候是str，/也当做字符串的一个字符
uuid 只接受uuid字符串
any 可以同时指定多种路径，进行限定
""" 
@app.route('/printint/<int:id>') # If the type is wrong, the page will not be found
def print_int(id):
    text = "Your ID is {}".format(id)
    return text


if __name__ == "__main__":
    app.run(host='localhost',port='9000',debug=True)