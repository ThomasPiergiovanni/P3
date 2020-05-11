#-*-coding:utf-8 -*
"""Play module"""
import grid
import objects
import guard
import macgyver
import status
import constants

class Play:
    """Play class.
    """
    def __init__(self):
        self.grid = grid.Grid()
        grid.Grid.read_source(self.grid)
        grid.Grid.initialize(self.grid)
        self.objects = objects.Objects()
        objects.Objects.initialize(self.objects, self.grid)
        self.guard = guard.Guard()
        guard.Guard.position(self.guard, self.grid)
        self.macgyver = macgyver.MacGyver()
        macgyver.MacGyver.position(self.macgyver, self.grid)


    def actions(self, status_instance):
        """Method binding all macgyver.MacGyver actions methods
        """
        new_position = macgyver.MacGyver.move(self.macgyver, \
        status_instance)
        macgyver.MacGyver.true_move(self.macgyver, \
        new_position, self.grid)
        macgyver.MacGyver.collect(self.macgyver, self.objects)

    def finish(self, status_instance):
        """ Method initiated when macgyver.MacGyver instance reaches
        the guard.Guard instance position
        """
        for elt in self.grid.cells:
            if self.macgyver.xy_position == elt.xy_position and elt.cell_type == 3 \
            and len(self.macgyver.collected_objects) == len(constants.OBJECTS):
                status_instance.game = 1
                status.Status.play_end(status_instance)
            if self.macgyver.xy_position == elt.xy_position and elt.cell_type == 3 \
            and len(self.macgyver.collected_objects) < len(constants.OBJECTS):
                status_instance.game = 2
                status.Status.play_end(status_instance)
