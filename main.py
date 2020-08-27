# v1.1

from flask import Flask, jsonify, request
from flask_cors import CORS
from Predict_function import predict_function

app = Flask(__name__)
CORS(app)


@app.route('/health_check')
def health_check():
    return jsonify({"status":"healthy"})


@app.route('/predict_service', methods=['POST'])
def predict_service():
    
    http_req_body = request.get_json()
    form_fields = http_req_body.get("form_fields", [])
    
    secret = http_req_body.get("secret", "")
    if (secret != "aiinnovation2020"):
        return {}

    
    short_desc = ""
    description = ""
    reported_by_sys_id = ""
    contact_method = ""
    risk = ""
    contact_type = ""
    requested_for_sys_id = ""
    requested_for_dept_name = ""
    requested_for_dept_code = "n/a"
    requested_for_affiliation = ""
    requested_for_business_unit = ""
    ticket_type = "incident"

    for field in form_fields:        
        if field["fieldName"] == "short_description":
            short_desc = field.get("value", "")
        elif field["fieldName"] == "description":
            description = field.get("value", "")
        elif field["fieldName"] == "caller_id":
            reported_by_sys_id = field.get("value", "")
        elif field["fieldName"] == "u_alternate_contact":
            contact_method = field.get("value", "")
        elif field["fieldName"] == "impact":
            risk = field.get("value", "")
        elif field["fieldName"] == "contact_type":
            contact_type = field.get("value", "")
        elif field["fieldName"] == "requested_for":
            requested_for_sys_id = field.get("value", "")
        elif field["fieldName"] == "requested_for.department":
            requested_for_dept_name = field.get("displayValue", "")
        elif field["fieldName"] == "requested_for.u_primary_affiliation":
            requested_for_affiliation = field.get("displayValue", "")
        elif field["fieldName"] == "requested_for.department.u_business_unit":
            requested_for_business_unit = field.get("displayValue", "")
      
    print ("short_description", short_desc)
    print ("description", description)
    print ("reported_by_sys_id", reported_by_sys_id)
    print ("contact_method", contact_method)
    print ("risk", risk)
    print ("contact_type", contact_type)
    print ("requested_for_sys_id", requested_for_sys_id)
    print ("requested_for_dept_name", requested_for_dept_name)
    print ("requested_for_dept_code", requested_for_dept_code)
    print ("requested_for_affiliation", requested_for_affiliation)
    print ("requested_for_business_unit", requested_for_business_unit)

    aiReturnValues = predict_function(short_desc, description, reported_by_sys_id, contact_method, risk, contact_type,requested_for_sys_id,requested_for_dept_name, requested_for_dept_code,requested_for_affiliation,requested_for_business_unit,ticket_type)
    predictedValue = ""
    predictedScore = -1
    if (aiReturnValues and len(aiReturnValues) == 2):
        predictedValues = aiReturnValues[0]
        predictedScore= aiReturnValues[1]
        if predictedValues and len(predictedValues) > 0:
            predictedValue = predictedValues[0]

    print("predictedValue", predictedValue)
    print("predictedScore", predictedScore)
    return {"predictedValue": predictedValue, "predictedScore": predictedScore}


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8019)