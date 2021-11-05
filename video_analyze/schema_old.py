ai_camera_config_schema = {
    "usecase_name": "camera1_zac_vehicle",
    "usecase_type": "zac_vehicle",
    "camera_setup": {
        "camera_name": "camera_name1",
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
        "start_time": "5:30",
        "end_time": "16:30",
        "duration_type": "",

        "day_duration": {
            "start_day": "20210505",
            "end_day": "20220606"
        },
        "week_duration": {
            "weekday": ["monday, tuesday", "wednesday", "thursday", "friday", "saturday","sunday"],
            "start_day": "20210505",
            "end_day": "20220606"
        },
        "month_duration": {
            "monthday": [1, 2, 3, 4, 5, 6, 7, 8],
            "start_day": "20210505",
            "end_day": "20220606"
        }
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
