import os
from configparser import ConfigParser

from flask import Flask


class BACnetSetting:

    def __init__(self):
        self.enabled: bool = True
        self.ip = '192.168.0.100'
        self.port = 47808
        self.device_id = 123
        self.local_obj_name = 'Nube-IO'
        self.model_name = 'rubix-bac-stack-RC4'
        self.vendor_id = 1173
        self.vendor_name = 'Nube iO Operations Pty Ltd'
        self.attempt_reconnect_secs = 5

    def reload(self, setting: dict):
        if setting is not None:
            self.__dict__ = {k: setting[k] or v for k, v in self.__dict__.items()}
        return self


class MqttSetting:

    def __init__(self):
        self.enabled = True
        self.name = 'bacnet-server-mqtt'
        self.host = '0.0.0.0'
        self.port = 1883
        self.keepalive = 60
        self.qos = 1
        self.retain = False
        self.attempt_reconnect_on_unavailable = True
        self.attempt_reconnect_secs = 5
        self.publish_value = True
        self.topic = 'rubix/points'

    def reload(self, setting: dict):
        if setting is not None:
            self.__dict__ = {k: setting[k] or v for k, v in self.__dict__.items()}
        return self


class AppSetting:
    DATA_DIR_ENV = 'RUBIX_BACNET_DATA'
    KEY: str = 'APP_SETTING'
    default_data_dir: str = 'out'

    def __init__(self, **kwargs):
        self.__data_dir = self.__compute_dir(kwargs['data_dir'], AppSetting.default_data_dir)
        self.__prod = kwargs['prod'] or False
        self.__mqtt_setting = MqttSetting()
        self.__bacnet_setting = BACnetSetting()

    @property
    def data_dir(self):
        return self.__data_dir

    @property
    def prod(self) -> bool:
        return self.__prod

    @property
    def mqtt(self) -> MqttSetting:
        return self.__mqtt_setting

    @property
    def bacnet(self) -> BACnetSetting:
        return self.__bacnet_setting

    def reload(self, setting_file: str, logging_file: str):
        parser = self.__read_file(setting_file, self.__data_dir)
        self.__mqtt_setting = self.__mqtt_setting.reload(self.__load_setting('mqtt', parser))
        self.__bacnet_setting = self.__bacnet_setting.reload(self.__load_setting('bacnet', parser))
        return self

    def init_app(self, app: Flask):
        app.config[AppSetting.KEY] = self
        return self

    @staticmethod
    def __compute_dir(_dir: str, _def: str, mode=0o744) -> str:
        d = os.path.join(os.getcwd(), _def) if _dir is None or _dir.strip() == '' else _dir
        d = d if os.path.isabs(d) else os.path.join(os.getcwd(), d)
        os.makedirs(d, mode, True)
        return d

    @staticmethod
    def __read_file(setting_file: str, _dir: str):
        if setting_file is None or setting_file.strip() == '':
            return None
        s = setting_file if os.path.isabs(setting_file) else os.path.join(_dir, setting_file)
        if not os.path.isfile(s) or not os.path.exists(s):
            return None
        parser = ConfigParser()
        parser.read(setting_file)
        return parser

    @staticmethod
    def __load_setting(section: str, parser: ConfigParser):
        if parser is None:
            return None
        return dict(parser.items(section)) if parser.has_section(section) else None