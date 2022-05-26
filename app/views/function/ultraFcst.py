import requests
from datetime import datetime, timedelta

def ultra_fcst(nx, ny):

    """좌표를 입력받아 초단기 실황 날씨를 제공하는 함수"""

    current_time = datetime.now()

    # 데이터 업데이트 시간 10분 고려
    time_ = current_time - timedelta(minutes=10)
    base_date = time_.strftime('%Y%m%d')
    base_time = time_.strftime('%H00')

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params ={'serviceKey' : 'KBfMS4fXfvc1Tn7/8xZpHQ9v97LoOTVTCaQCbNEVdCqGobQ0J7QFjp9JhpgiPCAu1jPDf9v4DlvPU+4y74sb0A==', 
            'pageNo' : '1', 'numOfRows' : '30', 'dataType' : 'json', 
            'base_date' : base_date, 'base_time' : base_time, 'nx' : nx, 'ny' : ny }


    res = requests.get(url, params=params)
    res = res.json()
    
    data = {'baseDate' : base_date, 'baseTime' : base_time,
            'nx' : nx, 'ny' : ny}

    for val in res['response']['body']['items']['item']:
        data[val['category']] = val['obsrValue']

    return data

