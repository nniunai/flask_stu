from flask import Flask,jsonify,url_for,redirect,request,render_template
import config


app = Flask(__name__)

# 加载外部配置项
app.config.from_object(config)


books=[
    { "id":1,"name":"三国演义" },
    { "id":2,"name":"水浒传" },
    { "id":3,"name":"红楼梦" },
    { "id":4,"name":"西游记" }
]


@app.route("/book/<int:book_id>")
def book_detail(book_id):
    print(book_id)

    for book in books:
        if book_id == book["id"]:
            return book
    return f"id位{book_id}找不到"



@app.route("/book/list")
def book_list():
    for book in books:
        book['url'] = url_for("book_detail",book_id=book['id'])
    return jsonify(books)



@app.route('/')
def index():
    # return 'Hello 你好啦风格恢复啦啦!'
    # return {"name":"你好 世界"}
    return jsonify(books)


@app.route("/profile")
def profile():

    user_id =request.args.get("id")
    if user_id:
        return "用户个人中心"
    else:
        return redirect(url_for("index"))



@app.route("/about")
def about():

    contest ={"username":"数据库的数据"}
    return render_template("about.html",**contest)





@app.route("/control")
def control():

    context = {
        "age" : 18,
        "books" : ["红楼梦",'西游记','水浒传','三国演绎'],
        "person":{"name":"小明","age":23}

    }

    return render_template("control.html",**context)








if __name__ == '__main__':
    app.run()

