class MoveController:
    def check(self, next_cell):
        for object in next_cell:
            if object.collide_type == 'Collide':
                return None
        return 1

    def move(self, prev_cell, object, next_cell):
        if self.check(next_cell) is not None:
            next_cell.set_object(object)
            prev_cell.remove_object(object)
