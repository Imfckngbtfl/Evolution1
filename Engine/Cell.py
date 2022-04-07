class Cell:
    def __init__(self, objects):
        self.objects = objects

    def set_object(self, object):
        self.objects.append(object)

    def get_object(self):
        return self.objects

    def remove_object(self, object):
        self.objects.pop(object)
