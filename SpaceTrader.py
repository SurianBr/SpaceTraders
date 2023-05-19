import requests
import json

class SpaceTrader:
    '''
    Api Calls do jogo SpaceTraders
    '''


    def __init__(self, caminho_secrets):
        '''
        Construtor

        Parâmetros
        ----------
            caminho_secrets : str
                Caminho para o arquivos screts.json que contem o tokem do agente
        '''

        self.url = 'https://api.spacetraders.io/v2/'

        leitura_secrets = open(caminho_secrets, 'r')
        string_secrets = leitura_secrets.read()
        self.secrets = json.loads(string_secrets)

        # busca token
        self.token = self.secrets['token']

    
    def post(self, url, headers=None, data=None):

        if headers is not None and data is not None:
            r = requests.post(url, headers=headers, json=data)
        elif headers is not None:
            r = requests.post(url, headers=headers)
        else:
            r = requests.post(url)

        return r.json()
    

    def get(self, url, headers=None):

        if headers is not None:
            r = requests.get(url, headers=headers)
        else:
            r = requests.post(url)

        return r.json()
    

    def register(self, callsign, faction):
        '''
        Registra um novo agente

        Parâmetros
        ----------
            callsign : str
                Callsign do novo agente
            faction : str
                Facção do novo agente

        Retorno
        -------
            resposta : dict
                Resposta chamada da API
        '''

        url = self.url + 'register'

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'symbol': callsign,
            'faction': faction
        }

        data = {
            'symbol': callsign,
            'faction': faction
        }

        return self.post(url, headers, data)
    

    def agent(self):
        '''
        Busca informações de agente cadastrado. Precisa do Token configurado.

        Retorno
        -------
            resposta : dict
                Resposta chamada da API
        '''
        
        url = self.url + 'my/agent'

        print(url)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.token)
        }

        return self.get(url, headers)
    

    def systems(self, system_symbol, waypoint_symbol=None, waypoint_type=None):
        '''
        Retorna dados de um sistema ou parada

        Parâmetros
        ----------
            system_symbol : str
                Simbolo do sistema

            waypoint_symbol : str (Opcional)
                Simbolo da parada

            waypoint_symbol : str (Opcional)
                Tipo da parada

        Retorno
        -------
            resposta : dict
                Sem waypoint_symbol e waypoint_type
                    Retorna dict com os dados do sistema

                Com waypoint_symbol e sem waypoint_type
                    Retorna dict com os dados da parada

                Com waypoint_symbol e waypoint_type
                    Retorna dict com os dados especifico do typo da parada
        '''

        if waypoint_symbol is not None and waypoint_type is not None:
            url = self.url + 'systems/{0}/waypoints/{1}/{2}'.format(
                system_symbol,
                waypoint_symbol,
                waypoint_type
            )
        else:
            url = self.url + 'systems/{0}'.format(
                system_symbol
            )

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.token)
        }

        return self.get(url, headers)
    

    def contracts(self, contracId=None, accept=False):
        '''
        Operações com contratos

        Parâmetros
        ----------
            contracId : str (Opcional)
                Id do contrato

            accept : Bool (Opcional)
                Flag para aceitar contrato. Precisa do contracId preencido. Default False.

        Retorno
        -------
            resposta : dict
                Sem contracId e accept=False
                    Retorna dict com todos os contratos disponiveis

                Enviado contracId e accept=False
                    Retorna dict com os dados do contrato

                Enviado contracId e accept=True
                    Retorna dict com os dados do contrato aceito

        '''

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.token)
        }

        if contracId is not None:
            url = self.url + 'my/contracts/{0}'.format(contracId)

            if accept is True:
                url = url + '/accept'

                return self.post(url, headers)
            
            return self.get(url, headers)
        
        else:
            url = self.url + 'my/contracts'

            return self.get(url, headers)
        

    def ships(
        self,
        ship_type=None,
        waypoint_symbol=None,
        ship_symbol=None,
        comando=None
    ):
        '''
        Operações com naves

        Parâmetros
        ----------
            contracId : str (Opcional)
                Id do contrato

        Retorno
        -------
            resposta : dict
                Sem contracId e accept=False
                    Retorna dict com todos os contratos disponiveis

                Enviado contracId e accept=False
                    Retorna dict com os dados do contrato

                Enviado contracId e accept=True
                    Retorna dict com os dados do contrato aceito

        '''

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.token)
        }

        if ship_type is not None and waypoint_symbol is not None:
            url = self.url + 'my/ships/'

            dados = {
                'shipType': ship_type,
                'waypointSymbol': waypoint_symbol
            }

            return self.post(url, headers, dados)
        
        elif ship_symbol is not None and comando is not None:
            if comando == 'navigate':
                url = self.url + 'my/ships/{0}/navigate'.format(
                    ship_symbol
                )

                dados = {
                    'waypointSymbol': waypoint_symbol
                }

                return self.post(url, headers, dados)
            
            else:
                url = self.url + 'my/ships/{0}/{1}'.format(
                    ship_symbol,
                    comando
                )
                return self.post(url, headers)

        else:
            url = self.url + 'my/ships/'

            return self.get(url, headers)