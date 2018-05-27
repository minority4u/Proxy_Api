from flask_restful import fields





box_content_fields = {
    #'id' : fields.Integer,
    'name' : fields.String,
    'box_id' : fields.Integer,
    'style' : fields.String,
    'color' : fields.String,
    'prize' : fields.String,
    'condition' : fields.String
}


address_fields_all = {
    'id': fields.Integer,
    'name' :fields.String,
    'str_name' :fields.String,
    'str_no' :fields.String,
    'city' : fields.String,
    'state' : fields.String,
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
    'addr_c' :fields.Nested(address_fields_all),
    'addr_d': fields.Nested(address_fields_all),
    'box_contents' : fields.Nested(box_content_fields)

}

box_fields_reduced = {
    'id': fields.Integer,
    'uri': fields.Url('boxressource', absolute=True),
    'name': fields.String,
    'status': fields.String,
    'weight': fields.String,
    'size': fields.String,
}





possible_routes_fields = {
    'Box' : fields.String,
    'Address' : fields.String
}

base_field_reduced = {
    'App' : fields.String,
    'Version' : fields.String
}

base_field_full = {
    'App' : fields.String,
    'Version' : fields.String,
    'Instance' : fields.String,
    'possible_routes' : fields.Nested(possible_routes_fields)
}

