from abc import ABC
from typing import List, Tuple

from super_scad.type.Point2 import Point2


class ThreadLeadCreator(ABC):
    """
    Creates a lead thread on a 2D thread profile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def create_lead(self,
                    profile: List[Point2] | Tuple[Point2, ...],
                    root_at: float,
                    angle: float) -> List[Point2] | Tuple[Point2, ...]:
        """
        Creates a lead thread on a 2D thread profile.

        :param profile: The thread profile in 2D.
        :param root_at: The y-coordinate of the root of the thread.
        :param angle:The angle of the current rotation.

        It is guaranteed that 0.0 <= root_at < pitch.
        It is guaranteed that 0.0 <= angle < 360.0.
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
