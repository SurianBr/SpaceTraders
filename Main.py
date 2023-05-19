import SpaceTrader

spaceTrader = SpaceTrader.SpaceTrader('secrets.json')

# Registra agente
#print(spaceTrader.register('RAVEN_1', 'COSMIC'))

# Busca agente
#print(spaceTrader.agent())

# Busca sistema
#print(spaceTrader.systems('X1-ZA40'))

# busca contratos
#print(spaceTrader.contracts())

# busca contrato em especifico
#print(spaceTrader.contracts('clhtodpoi29cps60dc65ljlk6'))

# aceita contrato
#print(spaceTrader.contracts('clhtodpoi29cps60dc65ljlk6', accept=True))

# Busca informações da parada
#print(spaceTrader.systems('X1-ZA40', 'X1-ZA40-68707C'))

# Busca naves disponivieis para compra
#print(spaceTrader.systems('X1-ZA40', 'X1-ZA40-68707C', 'SHIPYARD'))

# Busca impormações de naves possidas
#print(spaceTrader.ships())

# Compra nave
#print(spaceTrader.ships(ship_type='SHIP_MINING_DRONE', waypoint_symbol='X1-ZA40-68707C'))


# Ordena nave navegar para outra parada no sistema
#print(spaceTrader.ships(waypoint_symbol='X1-ZA40-99095A', ship_symbol='RAVEN_1-1', comando='navigate'))

# Ordena nave dockar
#print(spaceTrader.ships(ship_symbol='RAVEN_1-2', comando='dock'))

# Ordena nave abastecer
#print(spaceTrader.ships(ship_symbol='RAVEN_1-2', comando='refuel'))

# Ordena nave orbitar
#print(spaceTrader.ships(ship_symbol='RAVEN_1-2', comando='orbit'))

# Ordena nave minerar
#print(spaceTrader.ships(ship_symbol='RAVEN_1-2', comando='extract'))

# Ordena nave prospectar
print(spaceTrader.ships(ship_symbol='RAVEN_1-1', comando='survey'))