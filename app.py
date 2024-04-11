from flask import Flask, render_template, request, jsonify
from model import obter_dados_da_spacex, obter_detalhes_do_lancamento

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Obter os parâmetros de filtro do formulário
    filtro_mission_name = request.args.get('filtro_mission_name')
    filtro_launch_year = request.args.get('filtro_launch_year')
    # Obter os dados da SpaceX com base nos filtros
    dados = obter_dados_da_spacex(filtro_mission_name, filtro_launch_year)
    return render_template('index.html', dados=dados)

@app.route('/detalhes/<int:launch_id>')
def detalhes(launch_id):
    # Obter os detalhes completos do lançamento
    detalhes = obter_detalhes_do_lancamento(launch_id)
    print(detalhes)
    return jsonify(detalhes)

if __name__ == '__main__':
    app.run(debug=True)