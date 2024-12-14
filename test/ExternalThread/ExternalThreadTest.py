from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_thread.enum.ThreadDirection import ThreadDirection
from super_scad_thread.ExternalThread import ExternalThread
from super_scad_thread.lead_thread.external.NoneExternalThreadLeadCreator import NoneExternalThreadLeadCreator
from super_scad_thread.lead_thread.external.ScaleInExternalThreadLeadCreator import ScaleInExternalThreadLeadCreator
from test.ScadTestCase import ScadTestCase
from test.TestThreadProfileCreator import TestThreadProfileCreator


class ExternalThreadTest(ScadTestCase):
    """
    Testcases for external threads.
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
        minor_diameter = thread_profile_creator.minor_diameter
        top_thread_lead_creator = NoneExternalThreadLeadCreator(pitch, minor_diameter)
        bottom_thread_lead_creator = NoneExternalThreadLeadCreator(pitch, minor_diameter)

        thread = ExternalThread(length=15.0,
                                thread_profile_creator=thread_profile_creator,
                                top_thread_lead_creator=top_thread_lead_creator,
                                bottom_thread_lead_creator=bottom_thread_lead_creator,
                                direction=ThreadDirection.RIGHT)

        self.assertAlmostEqual(1.0, thread_profile_creator.pitch)
        self.assertAlmostEqual(6.0, thread_profile_creator.major_diameter)
        self.assertAlmostEqual(4.917468245269451, thread_profile_creator.minor_diameter)

        self.assertFalse(thread.center)
        self.assertAlmostEqual(15.0, thread.length)
        self.assertEqual(ThreadDirection.RIGHT, thread.direction)
        self.assertIsNone(thread.inner_diameter)
        self.assertIsNone(thread.inner_radius)
        self.assertEqual(2, thread.convexity)

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
        top_thread_lead_creator = ScaleInExternalThreadLeadCreator(pitch, minor_diameter, major_diameter)
        bottom_thread_lead_creator = ScaleInExternalThreadLeadCreator(pitch, minor_diameter, major_diameter)

        thread = ExternalThread(length=15.0,
                                thread_profile_creator=thread_profile_creator,
                                top_thread_lead_creator=top_thread_lead_creator,
                                bottom_thread_lead_creator=bottom_thread_lead_creator,
                                direction=ThreadDirection.RIGHT)

        self.assertAlmostEqual(1.0, thread_profile_creator.pitch)
        self.assertAlmostEqual(6.0, thread_profile_creator.major_diameter)
        self.assertAlmostEqual(4.917468245269451, thread_profile_creator.minor_diameter)

        self.assertFalse(thread.center)
        self.assertAlmostEqual(15.0, thread.length)
        self.assertEqual(ThreadDirection.RIGHT, thread.direction)
        self.assertIsNone(thread.inner_diameter)
        self.assertIsNone(thread.inner_radius)
        self.assertEqual(2, thread.convexity)

        scad.run_super_scad(thread, path_actual)
        actual = path_actual.read_text()

        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPlainLeftThread(self):
        """
        Plain right-handed, not centered thread, and hollow thread.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())

        thread_profile_creator = TestThreadProfileCreator(nominal_diameter=6.0, pitch=1.0)
        pitch = thread_profile_creator.pitch
        minor_diameter = thread_profile_creator.minor_diameter
        major_diameter = thread_profile_creator.major_diameter
        top_thread_lead_creator = ScaleInExternalThreadLeadCreator(pitch, minor_diameter, major_diameter)
        bottom_thread_lead_creator = ScaleInExternalThreadLeadCreator(pitch, minor_diameter, major_diameter)

        thread = ExternalThread(length=15.0,
                                thread_profile_creator=thread_profile_creator,
                                top_thread_lead_creator=top_thread_lead_creator,
                                bottom_thread_lead_creator=bottom_thread_lead_creator,
                                direction=ThreadDirection.RIGHT,
                                inner_radius=minor_diameter / 2.0,
                                center=True,
                                convexity=10)

        self.assertAlmostEqual(1.0, thread_profile_creator.pitch)
        self.assertAlmostEqual(6.0, thread_profile_creator.major_diameter)
        self.assertAlmostEqual(4.917468245269451, thread_profile_creator.minor_diameter)

        self.assertTrue(thread.center)
        self.assertAlmostEqual(15.0, thread.length)
        self.assertEqual(ThreadDirection.RIGHT, thread.direction)
        self.assertAlmostEqual(4.917468245269451, thread.inner_diameter)
        self.assertAlmostEqual(4.917468245269451 / 2.0, thread.inner_radius)
        self.assertEqual(10, thread.convexity)

        scad.run_super_scad(thread, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
