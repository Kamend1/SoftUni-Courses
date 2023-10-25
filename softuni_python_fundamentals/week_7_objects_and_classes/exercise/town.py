class Town:
    def __init__(self, name: str, latitude="0°N", longitude="0°E" ):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

