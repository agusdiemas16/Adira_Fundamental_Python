from package01.customer import Customer

PRIA, WANITA = range(2)
NON_FIX, FIX = range(2)

customer1 = Customer('Agus', PRIA, 3000000, True, FIX, {
    'Line 1': 'Cluster Edison Summarecon Serpong',
    'Kelurahan': 'Tanggerang Selatan',
    'City': 'Gading Serpong',
    'Province': 'Banten',
    'Zipcode': '15310',
    'Country': 'Indonesia'
})