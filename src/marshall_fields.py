from flask_restful import fields



address_fields_c = {
    'id': fields.Integer,
    'name' :fields.String,
    'str_name' :fields.String,
    'str_no' :fields.String,
    'city' : fields.String,
    'post_code' :fields.String,
    'country' : fields.String,
    'start_date': fields.DateTime,
    'end_date': fields.DateTime,
}

address_fields_d = {
    'id': fields.Integer,
    'name' :fields.String,
    'str_name' :fields.String,
    'str_no' :fields.String,
    'city' : fields.String,
    'post_code' :fields.String,
    'country' : fields.String,
    'start_date': fields.DateTime,
    'end_date': fields.DateTime,
}


box_fields = {
    'id' :fields.Integer,
    'uri' : fields.Url('boxressource', absolute=True),
    'name' : fields.String,
    'status': fields.String,
    'weight': fields.String,
    'size': fields.String,

    'addr_c' :fields.Nested(address_fields_c),
    'addr_d': fields.Nested(address_fields_d),

}

box_fields_reduced = {
    'id': fields.Integer,
    'uri': fields.Url('boxressource', absolute=True),
    'name': fields.String,
    'status': fields.String,
    'weight': fields.String,
    'size': fields.String,
}