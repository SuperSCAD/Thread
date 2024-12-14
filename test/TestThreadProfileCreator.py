import math
from typing import Tuple

from super_scad.scad.Unit import Unit
from super_scad.type.Vector2 import Vector2

from super_scad_thread.enum.ThreadAnatomy import ThreadAnatomy
from super_scad_thread.ThreadProfileCreator import ThreadProfileCreator


class TestThreadProfileCreator(ThreadProfileCreator):
    """
    Class for generating a test thread profile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 nominal_diameter: float,
                 pitch: float, ):
        """
        Object constructor.

        :param nominal_diameter: The nominal diameter of the thread.
        :param pitch: The pitch of the thread.
        """
        ThreadProfileCreator.__init__(self, pitch=pitch)

        self.__nominal_diameter = nominal_diameter
        """
        The nominal diameter of the thread.
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def unit_of_length(self) -> Unit:
        """
        Returns the unit of length in which the thread is specified.
        """
        return Unit.MM

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def minor_diameter(self) -> float:
        """
        Return the minor diameter of the thread.
        """
        h = self.pitch * math.cos(math.radians(30.0))
        thread_depth = 5 / 8 * h

        return self.__nominal_diameter - 2 * thread_depth

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def major_diameter(self) -> float:
        """
        Returns the major diameter of the thread.
        """
        return self.__nominal_diameter

    # ------------------------------------------------------------------------------------------------------------------
    def create_master_profile(self) -> Tuple[Tuple[ThreadAnatomy, Vector2], ...]:
        """
        Returns the thread profile points.
        """
        crest_width = self.pitch / 8.0
        root_width = self.pitch / 4.0
        step = (self.pitch - crest_width - root_width) / 2.0

        major_radius = self.major_diameter / 2.0
        minor_radius = self.minor_diameter / 2.0

        y = root_width / 2.0
        p1 = Vector2(minor_radius, y)
        y += step
        p2 = Vector2(major_radius, y)
        y += crest_width
        p3 = Vector2(major_radius, y)
        y += step
        p4 = Vector2(minor_radius, y)

        return (ThreadAnatomy.AT_MINOR, p1), \
            (ThreadAnatomy.AT_MAJOR, p2), \
            (ThreadAnatomy.AT_MAJOR, p3), \
            (ThreadAnatomy.AT_MINOR, p4)

# ----------------------------------------------------------------------------------------------------------------------
