from typing import Tuple
from definition import DIRECTION_POOL, USECASE_POOLS, WEEKDAY


class CheckConfig:
    def __init__(self, config:dict) -> None:
        self.config = config
        self.usecase_type = ""
    
    @staticmethod
    def check_polygon(polygon:list) -> bool:
        if len(polygon) <3:
            return False
        return True
    
    @staticmethod
    def check_time_format(time:str) -> bool:
        splited_str = time.split(":")
        if len(splited_str) !=2 : return False

        hour = splited_str[0]
        minute = splited_str[1]

        if int(hour)<0 or int(hour)>24:
            return False
        
        if int(minute)<0 or int(minute)>59:
            return False

        return True

    def check_field(self, field:str)->bool:
        if field not in self.config.keys():
            return False
        return True

    def check_camera_setup(self) ->bool:
        if "camera_setup" not in self.config.keys():
            return False
        camera_setup = self.config["camera_setup"]

        if "camera_name" not in camera_setup.keys():
            return False
        if "rtsp" not in camera_setup.keys():
            return False
        if "ROI" not in camera_setup.keys():
            return False
        if "PR" not in camera_setup.keys():
            return False

        ROI = camera_setup["ROI"]
        PR = camera_setup["PR"]

        ROI_check = self.check_polygon(ROI)
        for region in PR:
            if self.check_polygon(region) == False:
                PR_check = False
                break
            else: PR_check = True

        if not ROI_check or not PR_check:
            return False
        
        return True
    
    def check_usecase_config_existed(self) -> bool:
        self.usecase_type = self.config["usecase_type"]
        if self.usecase_type !=USECASE_POOLS[0] and self.usecase_type not in self.config.keys():
            return False
        
        return True
    
    def check_duration(self)->bool:
        duration = self.config["duration"]
        for week_day in duration.keys():
            if week_day not in WEEKDAY:
                return False
            times = duration[week_day]
            for time in times:
                if len(time) !=2:
                    return False
                
                if self.check_time_format(time[0])==False or self.check_time_format(time[1])==False:
                    return False

        return True

    def check_zac_human(self):
        if "zac_human" not in self.config.keys():
            return False
        
        zac_human = self.config["zac_human"]
        
        if "zones" not in zac_human.keys():
            return False
        if "lines" not in zac_human.keys():
            return False
        zones = zac_human["zones"]
        for zone in zones:
            if "zone" not in zone.keys() or len(zone["zone"])<3:
                return False

        lines = zac_human["lines"]
        for line in lines:
            if "line" not in line.keys() or len(line["line"] !=2 ) or "direction" not in line.keys() or line["direction"] not in DIRECTION_POOL:
                return False
        
        return True
    
    def check_zac_vehicle(self):
        if "zac_vehicle" not in self.config.keys():
            return False
        zac_vehicle = self.config["zac_vehicle"]

        if "zones" not in zac_vehicle.keys():
            return False
        zones = zac_vehicle["zones"]
        for zone in zones:
            if "zone" not in zone.keys() or len(zone["zone"])<3:
                return False

        return True
    
    def check(self)->Tuple[bool, str]:        
        if self.check_field("usecase_type") == False:
            return False, "usecase_type is not found"
        elif self.config["usecase_type"] not in USECASE_POOLS:
            return False, "usecase_type is not in USECASE_POOLS"

        if self.check_camera_setup() == False:
            return False, "camera_setup is False"

        if self.check_usecase_config_existed() == False:
            return False, "config of {} is not found".format(self.usecase_type)
            
        if self.check_duration() == False:
            return False, "duration is false"
        
        if self.usecase_type == USECASE_POOLS[0]:
            return True
        
        elif self.usecase_type == USECASE_POOLS[1]:
            if self.check_zac_vehicle() == False:
                return False, "zac_vehicle is set false"

        elif self.usecase_type == USECASE_POOLS[2]:
            if self.check_zac_human() == False:
                return False, "zac_human is set false"
        
        return True, ""