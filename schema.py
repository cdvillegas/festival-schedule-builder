from marshmallow import Schema, fields, post_load
from datetime import datetime
from model import *

class ArtistSchema(Schema):
    name = fields.Str()

    @post_load
    def make_artist(self, data, **kwargs):
        return Artist(**data)


class ShowSchema(Schema):
    artist = fields.Nested(ArtistSchema)
    start_time = fields.Str()
    end_time = fields.Str()
    rank = fields.Int()

    @post_load
    def make_show(self, data, **kwargs):
        # Convert ISO 8601 date format to datetime
        data['start_time'] = datetime.strptime(data['start_time'], "%Y-%m-%dT%H:%M:%S")
        data['end_time'] = datetime.strptime(data['end_time'], "%Y-%m-%dT%H:%M:%S")

        return Show(**data)


class ScheduleSchema(Schema):
    shows = fields.List(fields.Nested(ShowSchema))

    @post_load
    def make_schedule(self, data, **kwargs):
        return Schedule(**data)


class FestivalSchema(Schema):
    schedules = fields.List(fields.Nested(ScheduleSchema))

    @post_load
    def make_festival(self, data, **kwargs):
        return Festival(**data)