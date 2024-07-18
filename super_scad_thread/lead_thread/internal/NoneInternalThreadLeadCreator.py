from typing import List

from super_scad.type.Point2 import Point2

from super_scad_thread.lead_thread.internal.InternalThreadLeadCreator import InternalThreadLeadCreator
from super_scad_thread.ThreadAnatomy import ThreadAnatomy


class NoneInternalThreadLeadCreator(InternalThreadLeadCreator):
    """
    Creates no lead on a 2D internal thread profile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, pitch: float, major_diameter: float):
        """
        Object constructor.

        :param pitch: The pitch of the thread.
        :param major_diameter: The major diameter of the thread.
        """

        self.__pitch: float = pitch
        """
        The pitch of the thread.
        """

        self.__major_diameter: float = major_diameter
        """
        The major diameter of the thread. 
        """

    # ------------------------------------------------------------------------------------------------------------------
    def create_lead(self,
                    thread_profile: List[Point2],
                    thread_anatomy: List[ThreadAnatomy],
                    z: float,
                    angle: float) -> List[Point2]:
        """
        Creates a lead on a 2D thread profile.

        :param thread_profile: The thread profile in 2D.
        :param thread_anatomy: The location of a points on the thread profile.
        :param z: The current translation in z-axis direction.
        :param angle: The angle of the current rotation.

        It is guaranteed that 0.0 <= z < pitch.
        It is guaranteed that 0.0 <= angle < 360.0.
        """
        for index, point in enumerate(thread_profile):
            if point.y < 0.0:
                thread_profile[index] = Point2(self.__major_diameter / 2.0, 0.0)
            else:
                break

        return thread_profile

# ----------------------------------------------------------------------------------------------------------------------