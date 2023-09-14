"""
@Author SunYL
@Time 2023/9/12 16:13
"""

import yaml
from common.tools import get_project_path, sep


class GetConf:

    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(type(self.env))  # output: <class 'dict'>
            # print(type(self.env["mysql"]), self.env["mysql"])
            # print(self.env["mysql"]["db"])

    def get_username_password(self):
        return self.env["username"], self.env["password"]

    def get_mysql(self):
        return self.env["mysql"]


if __name__ == '__main__':
    print(GetConf().get_username_password())
    print(GetConf().get_mysql())
