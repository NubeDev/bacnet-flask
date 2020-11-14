from flask_restful import reqparse, marshal_with, Resource

from src.bacnet_server.models.model_server import BACnetServerModel
from src.bacnet_server.resources.mod_fields import server_field


class BACnetServer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ip', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('device_id', type=str)
    parser.add_argument('local_obj_name', type=str)
    parser.add_argument('model_name', type=str)
    parser.add_argument('vendor_id', type=str)
    parser.add_argument('vendor_name', type=str)

    @marshal_with(server_field)
    def get(self):
        return BACnetServerModel.find_one()

    @marshal_with(server_field)
    def patch(self):
        data = BACnetServer.parser.parse_args()
        data_to_update = {}
        for key in data.keys():
            if data[key] is not None:
                data_to_update[key] = data[key]
        BACnetServerModel.query.filter().update(data_to_update)
        return BACnetServerModel.find_one()
