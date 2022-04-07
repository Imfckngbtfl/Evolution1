class Cell:
    def __init__(self, objects):
        self.objects = objects
        self.is_update = 1

    def set_object(self, object):
        self.objects.append(object)
        self.is_update = 1

    def get_object(self):
        return self.objects

    def remove_object(self, object):
        self.objects.pop(object)
        self.is_update = 1

    def update(self):
        self.is_update = 0
