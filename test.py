from collections import Counter

x = {'wgomezr': 58949, 'TamaApoyo': 753, 'MosqueraCarlosB': 184, 'carlosfigueroa6': 2053, 'jcarlostuarez': 6219, 'ALANDMOLESTINAM': 14701, 'ChristianCruzLa': 554, 'davidroserow': 5252, 'PabloPonce': 1498, 'CPCCS2019': 2652, 'c_espinozaec': 14066, 'FranklinMorenoQ': 81, 'davalos2019': 45058, 'JamesMcpccs': 419, 'HernanUlloa': 18108, 'FaustoRLuperaM': 753, 'EDGallegosBayas': 446, 'carlospauta': 5, 'mrivadeneirac': 2155, 'monka78': 1282, 'jobafonfay2019': 1043, 'GinaAguilarEc': 203, 'VickyDesintonio': 59561, 'GracielaMoraEc': 27671, 'MarleMontesinos': 93, 'SofiaAlmeidaEc': 4911, 'ChugchilanJaime': 2088, 'BuendiaConcejal': 4, 'abenavidesgol1': 1939, 'LuisaMaldonadoM': 84050, 'PaolaVintimilla': 10922, 'EdgarJacomeT': 498, 'AndresPasquel': 419, 'SevilaCarlos': 186, 'victorhugoerazo': 341, 'OlivioSarzosa': 78, 'PacoMoncayo': 42959, 'mariasolcorral': 5252, 'PabloDavalos63': 6588, 'LoroHomero': 98732, 'juancaholguin': 32934, 'JCSolines': 6915, 'CesarMontufar51': 41410, 'PatoGYE': 3, 'JoseVasquezC71': 16, 'jimmyjairala': 45251, 'cedeno_marth': 378, 'jorgevillacrese': 330, 'CynthiaViteri6': 46612, 'GinoCornejoM': 470, 'cgcassanello': 79, 'inca_jose': 30, 'EduardoArgudoG': 1094, 'fcojimenez21': 3939, 'patobuendia23': 227, 'jaimelomas74': 264, 'Simon_BolivarEC': 682, 'edgarsalazar_51': 178}

k = Counter(x)

# Finding 3 highest values
high = k.most_common(10)



for i in high:
    print(i[0])


