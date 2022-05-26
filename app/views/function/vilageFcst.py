import requests
from datetime import datetime, timedelta

def vilage_fcst(nx, ny):

    """좌표를 입력받아 단기예보를 제공하는 함수"""

    current_time = datetime.now()

    # 데이터 업데이트 시간 10분정도 고려
    time_ = current_time - timedelta(hours=5, minutes=11)
    base_date = time_.strftime('%Y%m%d')

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    params ={'serviceKey' : 'KBfMS4fXfvc1Tn7/8xZpHQ9v97LoOTVTCaQCbNEVdCqGobQ0J7QFjp9JhpgiPCAu1jPDf9v4DlvPU+4y74sb0A==', 
            'pageNo' : '1', 'numOfRows' : '30', 'dataType' : 'JSON', 
            'base_date' : base_date, 'base_time' : '0500', 'nx' : nx, 'ny' : ny }


    res = requests.get(url, params=params)
    res = res.json()
    
    # json 형식 데이터 생성
    data = {'baseDate' : base_date, 'baseTime' : '0500',
            'nx' : nx, 'ny' : ny}

    for val in res['response']['body']['items']['item']:
        data[val['category']] = val['fcstValue']
    
    return data


   

