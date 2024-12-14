from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit

from super_scad_thread.InternalThread import InternalThread
from super_scad_thread.lead_thread.internal.NoneInternalThreadLeadCreator import NoneInternalThreadLeadCreator
from super_scad_thread.lead_thread.internal.ScaleInInternalThreadLeadCreator import ScaleInInternalThreadLeadCreator
from super_scad_thread.enum.ThreadDirection import ThreadDirection
from test.ScadTestCase import ScadTestCase
from test.TestThreadProfileCreator import TestThreadProfileCreator


class InternalThreadTest(ScadTestCase):
    """
    Testcases for internal threads.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainRightThreadNoLead(self):
        """
        Plain right-handed and not centered thread without a lead.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())

        thread_profile_creator = TestThreadProfileCreator(nominal_diameter=6.0, pitch=1.0)
        pitch = thread_profile_creator.pitch
        major_diameter = thread_profile_creator.major_diameter
        top_thread_lead_creator = NoneInternalThreadLeadCreator(pitch, major_diameter)
        bottom_thread_lead_creator = NoneInternalThreadLeadCreator(pitch, major_diameter)

        thread = InternalThread(length=15.0,
                                thread_profile_creator=thread_profile_creator,
                                top_thread_lead_creator=top_thread_lead_creator,
                                bottom_thread_lead_creator=bottom_thread_lead_creator,
                                direction=ThreadDirection.RIGHT,
                                outer_diameter=-1.0)

        self.assertAlmostEqual(1.0, thread_profile_creator.pitch)
        self.assertAlmostEqual(6.0, thread_profile_creator.major_diameter)
        self.assertAlmostEqual(4.917468245269451, thread_profile_creator.minor_diameter)

        self.assertFalse(thread.center)
        self.assertAlmostEqual(15.0, thread.length)
        self.assertEqual(ThreadDirection.RIGHT, thread.direction)
        self.assertAlmostEqual(3.0, thread.outer_radius)
        self.assertAlmostEqual(6.0, thread.outer_diameter)

        scad.run_super_scad(thread, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainRightThread(self):
        """
        Plain right-handed and not centered thread.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())

        thread_profile_creator = TestThreadProfileCreator(nominal_diameter=6.0, pitch=1.0)
        pitch = thread_profile_creator.pitch
        minor_diameter = thread_profile_creator.minor_diameter
        major_diameter = thread_profile_creator.major_diameter
        top_thread_lead_creator = ScaleInInternalThreadLeadCreator(pitch, minor_diameter, major_diameter)
        bottom_thread_lead_creator = ScaleInInternalThreadLeadCreator(pitch, minor_diameter, major_diameter)

        thread = InternalThread(length=15.0,
                                thread_profile_creator=thread_profile_creator,
                                top_thread_lead_creator=top_thread_lead_creator,
                                bottom_thread_lead_creator=bottom_thread_lead_creator,
                                direction=ThreadDirection.RIGHT,
                                outer_diameter=-1.0)

        self.assertAlmostEqual(1.0, thread_profile_creator.pitch)
        self.assertAlmostEqual(6.0, thread_profile_creator.major_diameter)
        self.assertAlmostEqual(4.917468245269451, thread_profile_creator.minor_diameter)

        self.assertFalse(thread.center)
        self.assertAlmostEqual(15.0, thread.length)
        self.assertEqual(ThreadDirection.RIGHT, thread.direction)
        self.assertAlmostEqual(3.0, thread.outer_radius)
        self.assertAlmostEqual(6.0, thread.outer_diameter)

        scad.run_super_scad(thread, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainLeftThread(self):
        """
        Plain right-handed, not centered thread, and explicit external radius.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())

        thread_profile_creator = TestThreadProfileCreator(nominal_diameter=6.0, pitch=1.0)
        pitch = thread_profile_creator.pitch
        minor_diameter = thread_profile_creator.minor_diameter
        major_diameter = thread_profile_creator.major_diameter
        top_thread_lead_creator = ScaleInInternalThreadLeadCreator(pitch, minor_diameter, major_diameter)
        bottom_thread_lead_creator = ScaleInInternalThreadLeadCreator(pitch, minor_diameter, major_diameter)

        thread = InternalThread(length=15.0,
                                thread_profile_creator=thread_profile_creator,
                                top_thread_lead_creator=top_thread_lead_creator,
                                bottom_thread_lead_creator=bottom_thread_lead_creator,
                                direction=ThreadDirection.RIGHT,
                                center=True,
                                outer_diameter=6.02)

        self.assertAlmostEqual(1.0, thread_profile_creator.pitch)
        self.assertAlmostEqual(6.0, thread_profile_creator.major_diameter)
        self.assertAlmostEqual(4.917468245269451, thread_profile_creator.minor_diameter)

        self.assertTrue(thread.center)
        self.assertAlmostEqual(15.0, thread.length)
        self.assertEqual(ThreadDirection.RIGHT, thread.direction)
        self.assertAlmostEqual(3.01, thread.outer_radius)
        self.assertAlmostEqual(6.02, thread.outer_diameter)

        scad.run_super_scad(thread, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
