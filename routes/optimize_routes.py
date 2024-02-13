from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from schema import FestivalSchema
from scheduler import Scheduler

# Create a Blueprint for optimization routes
optimize_bp = Blueprint('optimize', __name__)

@optimize_bp.route('/optimize', methods=['POST'])
def optimize():
    try:
        # Get festival request payload
        data = request.json
        schema = FestivalSchema()
        festival = schema.load(data)

        # Optimize each schedule
        for schedule in festival.schedules:
            scheduler = Scheduler(schedule=schedule)
            optimized_schedule = scheduler.optimize_schedule(iterations=15000)

            schedule.shows = optimized_schedule.shows

        result = schema.dump(festival)
        return jsonify(result), 200

    except ValidationError as err:
        return jsonify(err.messages), 400