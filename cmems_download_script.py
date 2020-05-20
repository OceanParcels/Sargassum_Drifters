import os
import datetime

downloadtimes = [datetime.datetime(2019, 7, 20) + datetime.timedelta(days=d) for d in range(80)]

for d in downloadtimes:
    dstr = d.strftime("%Y-%m-%d")
    fstr = d.strftime("%Y%m%d")
    print(dstr)
    os.system('python -m motuclient --motu http://nrt.cmems-du.eu/motu-web/Motu --service-id GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS --product-id global-analysis-forecast-phy-001-024-hourly-merged-uv --longitude-min -99 --longitude-max -5 --latitude-min 0 --latitude-max 26 --date-min "%s 00:30:00" --date-max "%s 23:30:00" --depth-min 0.493 --depth-max 0.4942 --variable uo --variable utide --variable utotal --variable vo --variable vsdx --variable vsdy --variable vtide --variable vtotal --out-dir /Users/erik/Desktop/SargassumData --out-name TrAtlUV_%s.nc --user USER --pwd PASSWD' % (dstr, dstr, fstr))