# tirameLosVencimientosPapa
Un script en python para a partir de una lista, obtener los vencimientos de unas url. Si me da fiaca ir a nic.ar y consultarlo por ahi. Jaja


El archivo dominios.txt-ejemplo tiene que tener la lista de dominios y cuando este completo se tiene que llamar dominios.txt. 
Creas el entorno virtual 

#	Clonamos el repositorio
git clone https://github.com/PabloCarrai/tirameLosVencimientosPapa.git
#	Ingresamos a la carpeta
cd tirameLosVencimientosPapa
#	Creamos el entorno
python3.13 -m venv .venv
#	Activamos el entorno virtual
source  .venv/bin/activate
#	Instalamos los requerimientos
pip install -r requirements.txt
#	Corremos el programa
python3.13 main.py
