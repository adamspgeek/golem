import unittest
from golem.appconfig import AppConfig, CommonConfig, NodeConfig
from golem.core.simpleenv import SimpleEnv


class TestWithAppConfig(unittest.TestCase):
    def clear_config(self):
        # This is to prevent test methods from picking up AppConfigs
        # created by previously run test methods:
        self.new_node()
        if hasattr(CommonConfig, "_properties"):
            del CommonConfig._properties
        if hasattr(CommonConfig, "properties"):
            del CommonConfig.properties
        if hasattr(NodeConfig, "_properties"):
            del NodeConfig._properties
        if hasattr(NodeConfig, "properties"):
            del NodeConfig.properties

    def new_node(self):
        AppConfig.CONFIG_LOADED = False

    def setUp(self):
        self.prev_simple_env = SimpleEnv.DATA_DIRECTORY
        self.clear_config()

    def tearDown(self):
        SimpleEnv.DATA_DIRECTORY = self.prev_simple_env
        self.clear_config()
