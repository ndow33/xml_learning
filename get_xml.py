from zeep import Client

aneroid = '302:OR:SNTL'
brighton = '366:UT:SNTL'

client = Client(wsdl='https://wcc.sc.egov.usda.gov/awdbWebService/services?WSDL')
# service areYouThere takes no parameters
print(client.service.areYouThere())
# service getAllForecastsForStation returns an ns0:forecastFull[] list...whatever that means
print(len(client.service.getAllForecastsForStation(brighton, '1980-10-01 00:00:00', '2100-01-01 00:00:00')))

def get_metadata(triplet):
    metadata = client.service.getStationMetadata(triplet)
    return metadata

print(get_metadata(brighton))
print(get_metadata(aneroid))

