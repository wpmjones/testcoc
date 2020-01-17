import constants
import random

from datetime import datetime, timedelta
from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


class About(Resource):
    def get(self):
        return {"about": "This API has been put together for the simple purpose of providing test data (both "
                         "valid and invalid) so that developers can test their code without having to abuse the "
                         "official COC API.  This is also a great tool to see how your code handles invalid input "
                         "from end users.  This API is maintained by TubaKid.  If you have questions or concerns, "
                         "you can find me on Discord at https://discord.gg/Eaja7gJ"}


class ValidPlayerTags(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of tags returned.")
        self.reqparse.add_argument("wrong_prefix",
                                   type=bool,
                                   required=False,
                                   default=False,
                                   help="Choose whether or not to responde with incorrect prefixes.")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        wrong_prefix = args['wrong_prefix']
        return_list = []
        if limit:
            while len(return_list) < limit:
                x = random.choice(constants.valid_player_tags)
                if x not in return_list:
                    return_list.append(x)
        else:
            return_list = constants.valid_player_tags
        if wrong_prefix:
            return_list = [tag.replace("#", random.choice(constants.prefixes)) for tag in return_list]
        return {"tags": return_list}


class GarbledPlayerTags(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of tags returned.")
        self.reqparse.add_argument("wrong_prefix",
                                   type=bool,
                                   required=False,
                                   default=False,
                                   help="Choose whether or not to respond with incorrect prefixes.")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        wrong_prefix = args['wrong_prefix']
        return_list = []
        if limit:
            while len(return_list) < limit:
                x = random.choice(constants.garbled_player_tags)
                if x not in return_list:
                    return_list.append(x)
        else:
            return_list = constants.garbled_player_tags
        if wrong_prefix:
            return_list = [tag.replace("#", random.choice(constants.prefixes)) for tag in return_list]
        return {"tags": return_list}


class InvalidPlayerTags(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of tags returned.")
        # self.reqparse.add_argument("wrong_prefix",
        #                            type=bool,
        #                            required=False,
        #                            default=False,
        #                            help="Choose whether or not to responde with incorrect prefixes.")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        if not limit:
            limit = 190
        return_list = []
        while len(return_list) < limit:
            if len(return_list) == len(constants.valid_player_tags):
                break
            tag = random.choice(constants.valid_player_tags)
            bad_chars = ["X", "@", "4", "7", "i"]
            if tag not in return_list:
                return_list.append(f"{tag[:3]}{random.choice(bad_chars)}{tag[4:]}")
        return {"tags": return_list}


class ValidClanTags(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of tags returned.")
        self.reqparse.add_argument("wrong_prefix",
                                   type=bool,
                                   required=False,
                                   default=False,
                                   help="Choose whether or not to responde with incorrect prefixes.")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        wrong_prefix = args['wrong_prefix']
        return_list = []
        if limit:
            while len(return_list) < limit:
                x = random.choice(constants.valid_clan_tags)
                if x not in return_list:
                    return_list.append(x)
        else:
            return_list = constants.valid_player_tags
        if wrong_prefix:
            return_list = [tag.replace("#", random.choice(constants.prefixes)) for tag in return_list]
        return {"tags": return_list}


class GarbledClanTags(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of tags returned.")
        self.reqparse.add_argument("wrong_prefix",
                                   type=bool,
                                   required=False,
                                   default=False,
                                   help="Choose whether or not to respond with incorrect prefixes.")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        wrong_prefix = args['wrong_prefix']
        return_list = []
        if limit:
            while len(return_list) < limit:
                x = random.choice(constants.garbled_clan_tags)
                if x not in return_list:
                    return_list.append(x)
        else:
            return_list = constants.garbled_clan_tags
        if wrong_prefix:
            return_list = [tag.replace("#", random.choice(constants.prefixes)) for tag in return_list]
        return {"tags": return_list}


class InvalidClanTags(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of tags returned.")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        if not limit:
            limit = 190
        return_list = []
        while len(return_list) < limit:
            if len(return_list) == len(constants.valid_clan_tags):
                break
            tag = random.choice(constants.valid_clan_tags)
            bad_chars = ["X", "@", "4", "7", "i"]
            if tag not in return_list:
                return_list.append(f"{tag[:3]}{random.choice(bad_chars)}{tag[4:]}")
        return {"tags": return_list}


class Dates(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("limit",
                                   type=int,
                                   required=False,
                                   default=None,
                                   help="Optional limit on number of dates returned.")
        self.reqparse.add_argument("date_type",
                                   type=str,
                                   required=True,
                                   help="Required: Past or Future (date_type=future)")

    def get(self):
        args = self.reqparse.parse_args()
        limit = args['limit']
        tense = args['date_type'].lower()
        return_list = []
        if not limit:
            limit = 255
        while len(return_list) < limit:
            if tense == "past":
                new_date = datetime.utcnow() - timedelta(hours=random.randint(0, 168),
                                                         minutes=random.randint(1, 59),
                                                         seconds=random.randint(1, 59))
            elif tense == "future":
                new_date = datetime.utcnow() + timedelta(hours=random.randint(0, 168),
                                                         minutes=random.randint(1, 59),
                                                         seconds=random.randint(1, 59))
            else:
                return {"error": "You must provide a valid argument for date_type (either past or future)."}
            return_list.append(new_date.strftime("%Y%m%dT%H%M%S.000Z"))
        return {f"{tense}_dates": return_list}


api.add_resource(About, '/')
api.add_resource(ValidPlayerTags, "/player_tags")
api.add_resource(GarbledPlayerTags, "/player_tags/garbled")
api.add_resource(InvalidPlayerTags, "/player_tags/invalid")
api.add_resource(ValidClanTags, "/clan_tags")
api.add_resource(GarbledClanTags, "/clan_tags/garbled")
api.add_resource(InvalidClanTags, "/clan_tags/invalid")
api.add_resource(Dates, "/dates")

if __name__ == "__main__":
    app.run(debug=True)
