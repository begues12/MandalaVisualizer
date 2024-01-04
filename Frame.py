class Frame:
    def __init__(self, image, angle):
        self.image = image
        self.angle = angle

    def get_image(self):
        return self.image

    def get_angle(self):
        return self.angle