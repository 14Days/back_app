import cv2
from pathlib import Path
from flask import Blueprint, request, g, current_app
from app.model.color import get_color_list
from app.util.response import fail_res, success_res
from app.model.user_color import post_color, get_color
from app.model.user import get_user_info, post_user_info, change_password, delete_jwt_in_redis
from app.util.exception import DataBaseException, CommonException
from app.model.user_follow_user import post_follow, delete_follow
from app.model.user_collect_recommend import post_collect, delete_collect
from app.model.user_like_recommend import post_like, delete_like
from app.util.md5 import encode_md5
from app.model.avatar import post_avatar, get_avatar
from app.model.comment import post_top_comment, post_second_comment

user = Blueprint('user', __name__)


@user.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'GET':
        return success_res(get_color_list())
    if request.method == 'POST':
        data = request.json
        user_id = g.user_id
        color_id = data.get('color_id')
        post_color(user_id, color_id)
        return success_res('提交成功')


@user.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'GET':
        try:
            data = get_user_info(user_id=g.user_id)
            user_color = get_color(user_id=g.user_id)
            data['color'] = user_color
            data['avatar'] = get_avatar(user_id=g.user_id)
            return success_res(data)
        except DataBaseException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)

    if request.method == 'POST':
        user_id = g.user_id
        data = request.json
        if data is None:
            return fail_res('参数缺失')
        email = data.get('email')
        sex = data.get('sex')
        nickname = data.get('nickname')
        post_user_info(user_id, sex, email, nickname)
        return success_res('编辑成功')


@user.route('/password', methods=['POST'])
def password():
    try:
        user_id = g.user_id
        data = request.json
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        change_password(user_id, old_password, new_password)
        return success_res('修改成功')
    except CommonException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)


@user.route('/logout', methods=['POST'])
def logout():
    user_id = g.user_id
    delete_jwt_in_redis(user_id)
    return success_res('退出登录')


@user.route('/follow', methods=['POST', 'DELETE'])
def follow():
    user_id = g.user_id
    data = request.json
    web_id = data.get('id')
    if request.method == 'POST':
        try:
            post_follow(user_id, web_id)
            return success_res('关注成功')
        except CommonException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)
    if request.method == 'DELETE':
        delete_follow(user_id, web_id)
        return success_res('取关成功')


@user.route('/collect', methods=['POST', 'DELETE'])
def collect():
    user_id = g.user_id
    data = request.json
    recommend_id = data.get('id')
    if request.method == 'POST':
        try:
            post_collect(user_id, recommend_id)
            return success_res('收藏成功')
        except CommonException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)
    if request.method == 'DELETE':
        try:
            delete_collect(user_id, recommend_id)
            return success_res('取消收藏成功')
        except CommonException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)


@user.route('/like', methods=['POST', 'DELETE'])
def like():
    user_id = g.user_id
    data = request.json
    recommend_id = data.get('id')
    if request.method == 'POST':
        try:
            post_like(user_id, recommend_id)
            return success_res('点赞成功')
        except CommonException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)
    if request.method == 'DELETE':
        try:
            delete_like(user_id, recommend_id)
            return success_res('取消点赞成功')
        except CommonException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)


@user.route('/avatar', methods=['POST'])
def avatar():
    user_id = g.user_id
    _UPLOAD_FOLDER = 'avatar'
    base_dir = Path(__file__).parent.parent.parent
    file_dir = base_dir / _UPLOAD_FOLDER
    _ALLOWED_EXTENSIONS = {'jpg', 'JPG', 'png', 'PNG', 'gif', 'GIF'}

    def allow_file(name: str) -> bool:
        return '.' in name and name.rsplit('.', 1)[1] in _ALLOWED_EXTENSIONS

    def compress(path: str):
        img1 = cv2.imread(path, cv2.IMREAD_COLOR)
        new_path = path.rsplit('.', 1)[0] + '.jpg'
        cv2.imwrite(new_path, img1, [cv2.IMWRITE_JPEG_QUALITY, 30])

    img = request.files.get('avatar')
    filename = img.filename

    if img and allow_file(filename):
        ext = filename.split('.', 1)[1]
        filename = encode_md5(filename)
        new_filename = filename + '.' + ext
        path1 = str(file_dir / new_filename)
        img.save(path1)
        compress(path1)
        post_avatar(user_id, filename + '.jpg')
        return success_res('上传成功')
    else:
        return fail_res('参数错误')


@user.route('/comment', methods=['POST'])
def comment():
    user_id = g.user_id
    data = request.json
    type_ = data.get('type')
    id_ = data.get('id')
    content = data.get('content')
    if type_ == 1:
        post_top_comment(user_id, id_, content)
    else:
        post_second_comment(user_id, id_, content)
    return success_res('评论成功')
