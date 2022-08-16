from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
app = Flask(__name__)
api = Api(app)
# 인수를 찾지 못하는 경우 발신자에게 자동으로 처리
reqparser = reqparse.RequestParser()
reqparser.add_argument('name', type=str, help='Name of the content is required', required=False)
reqparser.add_argument('views', type=int, help='views of the content', required=False)
reqparser.add_argument('likes', type=int, help='likes of the content', required=False)
contents = { 1 :{'name':'nick', 'views':10, 'likes':100}}

def abort_content_exists(content_id):
    if content_id in contents:
        abort(400, message='content alread exists with that ID')

class Test_Class(Resource):

    reqparser = reqparse.RequestParser()
    reqparser.add_argument("name", type=str, help='name of the content is required', required=True)
    # 데이터 저장
    def post(self, content_id):
        abort_content_exists(content_id)
        args = Test_Class.reqparser.parse_args()
        contents[content_id] = args
        print(contents)
        return contents[content_id], 201

    def get(self, content_id):
        return contents[content_id]


api.add_resource(Test_Class, '/content/<int:content_id>')

if __name__ == '__main__':
    app.run(debug=True)

