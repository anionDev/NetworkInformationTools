import unittest
from ..NetworkInformationTools.NetworkInformationToolsCore import NetworkInformationToolsCore


class NetworkInformationToolsCoreTests(unittest.TestCase):

    def test_loop_action_terminates_if_loop_is_disabled(self):
        # arrange
        pcuc = NetworkInformationToolsCore()

        # act
        pcuc.loop_action(False, lambda *args: None)
