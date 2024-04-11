import requests

def obter_dados_da_spacex(filtro_mission_name=None, filtro_launch_year=None):
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    if response.status_code == 200:
        dados_spacex = response.json()
        if filtro_mission_name:
            dados_spacex = [launch for launch in dados_spacex if launch['mission_name'] == filtro_mission_name]
        if filtro_launch_year:
            dados_spacex = [launch for launch in dados_spacex if str(launch.get('launch_year')) == filtro_launch_year]
        return dados_spacex
    else:
        return None

def obter_detalhes_do_lancamento(launch_id):
    url = f"https://api.spacexdata.com/v3/launches/{launch_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None