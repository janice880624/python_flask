from flask import Flask 
from flask import request # 載入 request 物件

app = Flask(
  __name__,
  static_folder="static", # 靜態檔案的資料夾名稱
  static_url_path="/janice" # 靜態檔案對應的網址路徑
)

# 所有在 static 資料夾底下的路徑，都對應到網址路徑 /static/檔案名稱底下

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): 
  lang = request.headers.get('accept-language')
  if lang.startswith('en'):  
    return "Hello ha" 
  else: 
    return "您好，歡迎光臨"

# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData(): 
  return "My Data" 

@app.route("/user/<username>")
def handleUser(username): 
  if username == 'janice':
    return "你好 " + username
  else:
    return "Hello " + username

# 啟動網站伺服器
app.run(port=3000)

