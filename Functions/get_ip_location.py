import geoip2.database
"""
Requirements:
    geoip2
    use this page to download the db:
      https://dev.maxmind.com/geoip/geolite2-free-geolocation-data?lang=en
"""
# This creates a Reader object. You should use the same object
# across multiple requests as creation of it is expensive.
with geoip2.database.Reader('/path/to/GeoLite2-City.mmdb') as reader:

    # Replace "city" with the method corresponding to the database
    # that you are using, e.g., "country".
    response = reader.city('203.0.113.0')
    print(
        response.country.iso_code +
        response.country.name +
        response.country.names['zh-CN'] +
        response.subdivisions.most_specific.name +
        response.subdivisions.most_specific.iso_code +
        response.city.name +
        response.postal.code +
        response.location.latitude +
        response.location.longitude +
        response.traits.network, sep="\n"
    )

""