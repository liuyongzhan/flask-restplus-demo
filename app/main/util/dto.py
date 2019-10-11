from flask_restplus import Namespace, fields
from flask_restplus import reqparse

# 定义数据传输对象--dto;相当于django-restframework的序列化


class UserDto:
    api = Namespace('user', description='用户相关操作')

    # fields模块可以控制响应数据或预期数据(客户端传过来的)的格式
    update_user_model = api.model('updateUser', {
        'email': fields.String(required=True, description='email地址'),
        'username': fields.String(required=True, description='用户名'),
        'password': fields.String(required=True, description='密码')
    })
    user_model = api.inherit('user', update_user_model, {
        'public_id': fields.String(description='用户标识')
    })

    # parser模块只可以校验客户端传过来的数据格式
    user_parser = reqparse.RequestParser(bundle_errors=True)
    user_parser.add_argument('email', type=str, required=True, help="email不能为空")
    user_parser.add_argument('username', type=str, required=True, help="用户名不能为空")
    user_parser.add_argument('password', type=str, required=True, help="密码不能为空")

