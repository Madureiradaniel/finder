from math import radians, cos, sin, asin, sqrt

class Services:
    #calcular km
    def haversine(self, a, b ):
        # Raio da Terra em Km
        r = 6371

        # Converte coordenadas de graus para radianos
        lon1, lat1, lon2, lat2 = map(radians, [ a['longitude'], a['latitude'], b['longitude'], b['latitude'] ] )

        # Formula de Haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        hav = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        km = 2 * r * asin( sqrt(hav) )

        return km

