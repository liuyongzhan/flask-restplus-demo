#### FLASK-RESTFUL 框架样例工程
##### 适用于：开发/测试/生产环境

### 安装依赖包
    pip install flask-bcrypt flask-restplus Flask-Migrate pyjwt Flask-Script flask_testing gunicorn
    
    pip freeze > requirements.txt

### 初始化数据库
    修改app/main目录下的dev_db.py文件中的数据库连接配置。
    然后执行数据库迁移操作：
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

### 运行
    make run 或者 python manage.py run

### 打开浏览器查看
    http://IP:5000/
    
### Tip
    开发/测试/生产环境的切换：
    请修改manage.py文件中create_app()的参数，参数可选：dev/prod/test; 默认dev。
    
    启动端口的修改：
    请修改manage.py文件中app.run()的port关键字参数。
    
    如果请求的接口需要携带Authorization请求头，则需要使用Postman工具来测试。
    Key: Authorization
    Value: "登录生成的Token信息"

    关于make命令的更多用法,请看工程根目录下的Makefile文件。
