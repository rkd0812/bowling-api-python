swagger_config = {
    'openapi': '3.0.2',
    'doc_dir': './docs'
}

swagger_template = {
    "info": {
        "description": "Bowling User Api",
        "version": "0.1"
    },
    "tags": [{
        "name": "user",
        "description": "Operation about user"
    }],
    "components": {
        "schemas": {
            "user": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "example": "001"
                    },
                    "password": {
                        "type": "string",
                        "example": "password"
                    },
                    "name": {
                        "type": "string",
                        "example": "John"
                    },
                    "email": {
                        "type": "string",
                        "example": "test@email.com"
                    }
                }
            },
            "api_response": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Success to ~~~~"
                    }
                }
            }
        }
    }
}
