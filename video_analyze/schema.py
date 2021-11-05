ai_camera_config_schema = {
    "usecase_name": "camera1_zac_vehicle",
    "usecase_type": "zac_vehicle",
    "camera_setup": {
        "camera_name": "camera1",
        "rtsp": "rtsp://192.168.50.17:1594/va",
        "ROI": [
            [ 0.1, 0.2],
            [ 0.2, 0.3],
            [ 0.2, 0.3]
            ],
        "PR": [
            [[ 0.1, 0.2],
            [ 0.2, 0.3],
            [ 0.2, 0.3]],
            
            [[ 0.1, 0.2],
            [ 0.2, 0.3],
            [ 0.2, 0.3]]
        ]
    },

    "duration": {
        "monday":[["5:30", "8:30"],
                    ["10:00", "11:30"],
                    ["13:00", "15:30"]],

        "tuesday":[["5:30", "8:30"],
                    ["10:00", "11:30"],
                    ["13:00", "15:30"],
                    ["16:00", "19:30"]]        
    },

    "zac_human": {
        "zones": [{
            "zone": [
                [ 0.1, 0.2],
                [ 0.2, 0.3],
                [ 0.2, 0.3]
            ],
            "intersection_time_threshold": 0.0,
            "intersection_area_threshold": 0.0
        }],
        "lines": [{
            "line": [
                [ 0.1, 0.2],
                [ 0.2, 0.3]
            ],
            "direction": 0
        }]
    },

    "zac_vehicle": {
        "zones": [{
            "zone": [
                [ 0.1, 0.2 ],
                [ 0.2, 0.3 ],
                [ 0.2, 0.3 ]
            ],
            "intersection_time_threshold": 0.0,
            "intersection_area_threshold": 0.0
        }],
        "lines": [{
            "line": [
                [ 0.1, 0.2],
                [ 0.2, 0.3]
            ],
            "direction": 0
        }]
    }
}
