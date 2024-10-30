from datetime import datetime

def transform_data(data):
    data['timestamp'] = datetime.now()  # Adds the current timestamp
    return data
