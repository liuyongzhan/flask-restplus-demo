from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, update_user, delete_user

api = UserDto.api
_user = UserDto.user_model
_update_user = UserDto.update_user_model
_user_parser = UserDto.user_parser


@api.route('/')
class UserList(Resource):

    @api.doc('列出所有的用户')
    @api.marshal_list_with(_user, envelope='my_data')  # marshal系列的装饰器控制响应数据的格式
    def get(self):
        """列出所有用户"""
        return get_all_users()

    @api.expect(_user_parser, validate=True)  # expect装饰器校验客户端传送过来的数据
    @api.response(201, '创建用户成功')
    @api.doc('创建一个新用户')
    def post(self):
        """创建新用户"""
        data = _user_parser.parse_args()
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', '用户标识')
class User(Resource):

    @api.marshal_with(_update_user)  # marshal系列的装饰器控制响应数据的格式
    @api.doc('通过用户标识查询用户')
    @api.response(404, '找不到该用户')
    def get(self, public_id):
        """通过用户标识查询用户"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

    @api.expect(_update_user, validate=True)
    @api.doc('更新用户')
    @api.response(204, '更新用户成功')
    def put(self, public_id):
        """更新用户"""
        data = request.json
        update_user(public_id, data)
        return None, 204

    @api.doc('删除用户')
    @api.response(204, '删除用户成功')
    def delete(self, public_id):
        """删除用户"""
        delete_user(public_id)
        return None, 204



