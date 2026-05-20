from flask import Blueprint, jsonify, request
from models import db
from models.sensor import Sensor
from datetime import datetime

sensor_bp=Blueprint('sensor_bp',__name__)

@sensor_bp.route('',methods=['GET'])
def get_all():
    data=db.session.execute(db.select(Sensor).order_by(Sensor.id)).scalars()
    json_data=[]
    for d in data:
        json_data.append(d)
    return jsonify(json_data)

@sensor_bp.route('',methods=['POST'])
def create():
    data_hora=datetime.now()
    req=request.get_json()
    try:
        sensor=Sensor(
            temperature=req['temperature'],
            humidity=req['humidity'],
            air_quality=req['air_quality'],
            date_hour=data_hora
            )
        db.session.add(sensor)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
  
    return jsonify({
       'response':'dados enviados',
       'status':'sucesso'
   }),200

@sensor_bp.route('/current-temp', methods=['GET'])
def get_current_temp():
    current_temp=Sensor.query.order_by(Sensor.date_hour.desc()).first()
    return jsonify({
        'id': current_temp.id,
        'temperature':current_temp.temperature,
        'humidity':current_temp.humidity,
        'air_quality':current_temp.air_quality,
        'date_hour':current_temp.date_hour
    }),200

@sensor_bp.route('/<int:id>',methods=['GET'])
def get_by_id(id):
    sensor=db.get_or_404(Sensor,id)
    return jsonify({
        'id': sensor.id,
        'temperature':sensor.temperature,
        'humidity':sensor.humidity,
        'air_quality':sensor.air_quality,
        'date_hour':sensor.date_hour
    }),200