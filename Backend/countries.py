class country:
    def __init__(self, name, capital, latitude, longitude, windspeed, wind_direction, tectonic_plate):
        self.name = name
        self.cap = capital
        self.lat = latitude
        self.long = longitude
        self.coords = (round(self.lat,2), round(self.long,2))
        self.wind = (windspeed, int(wind_direction))
        self.plate = tectonic_plate

    def __str__(self):
<<<<<<< HEAD
        return f"Country: {self.name}\nCaptial: {self.cap}\nLongitude: {self.long}\nLatitude: {self.lat}\nWindspeed: {self.wind[0]}\nWind Direction: {self.wind[1]}\nTectonic Plate: {self.plate}"


# Countries
# eg = country("", "", , , 0, 0, "")
=======
        return f"Country: {self.name}\nCapital: {self.cap}\nLatitude: {self.lat}\nLongitude: {self.long}\nWindspeed: {self.wind[0]}\nWind Direction: {self.wind[1]}\nTectonic Plate: {self.plate}"


# Countries
eg = country("Egypt", "Cairo", 26.820553, 30.802498, 0, 0, "Arabian")
us = country("United States", "Washington", 37.09024, -95.712891, 0, 0, "North American")
>>>>>>> 3ab4be66f23a0734ae766e0af8b03512c3c40eb7

AD = country('Andora','Andorra la Vella',42.546245,1.601554,0,0,'African')
AE = country('United Arab Emirates','Abu Dhabi',23.424076,53.847818,0,0,'Arabian')
AF = country("Afghanistan", "Cairo", 33.93911,67.709953, 0, 0, "African")
AG = country("Antigua and Barbuda", "Saint John's", 17.060816, -61.796428, 0, 0, "North American")
AI = country("Anguilla", "The Valley", 18.220554, -63.068615, 0, 0, "Caribbean")
AL = country("Albania", "Tirana",41.153332 , 20.168331, 0, 0, "Eurasian")
AM = country("Armenia", "",40.069099 ,45.038189 , 0, 0, "Eurasian")
AN = country("Netherlands Antilles", "Willemstad", 12.226079,-69.060087 , 0, 0, "Caribbean")
AO = country("Angola", "Luanda", -11.202692, 17.873887, 0, 0, "African")
AQ = country("Antarctica", "NAN",-75.250973 , -0.071389, 0, 0, "Antarctic")
AR = country("Argentina", "Buenos Aires",-38.416097 ,-63.616672 , 0, 0, "South American")
AS = country("American Samoa", "Pago Pago", -14.270972, -170.132217, 0, 0, "Pacific")
AT = country("Austria", "Vienna",47.516231 ,14.550072 , 0, 0, "Eurasian")
AU = country("Australia", "Canberra",-25.274398 , 133.775136, 0, 0, "Australian")
AW = country("Aruba", "Oranjestad",12.52111 , -69.968338, 0, 0, "Caribbean")
AZ = country("Azerbaijan", "Baku", 40.143105, 47.576927, 0, 0, "Eurasian")
BA = country("Bosnia and Herzegovina", "Sarajevo",43.915886 , 17.679076, 0, 0, "Eurasian")
BB = country("Barbados", "Bridgetown",13.193887 ,-59.543198 , 0, 0, "Caribbean")
BD = country("Bangladesh", "Dhaka", 23.684994,90.356331 , 0, 0, "Indian")
BE = country("Belgium", "Brussels", 50.503887, 4.469936, 0, 0, "Eurasian")
BF = country("Burkina Faso", "Ouagadougou",12.238333 , -1.561593, 0, 0, "African")
BG = country("Bulgaria", "Sofia", 42.733883,25.48583 , 0, 0, "Eurasian")
BH = country("Bahrain", "Manama",25.930414 , 50.637772, 0, 0, "Arabian")
BI = country("Burundi", "Bujumbura", -3.373056, 29.918886, 0, 0, "African")
BJ = country("Benin", "Porto-Novo", 9.30769,2.315834 , 0, 0, "African")
BM = country("Bermuda", "Hamilton", 32.321384, -64.75737, 0, 0, "NAN")
BN = country("Brunei", "Bandar Seri Begawan",4.535277 ,114.727669 , 0, 0, "Philippine Sea")
BO = country("Bolivia", "Sucre",-16.290154 ,-63.588653 , 0, 0, "South American")
BR = country("Brazil", "Brasília",-14.235004 ,-51.92528 , 0, 0, "South American")
BS = country("Bahamas", "Bahamas", 25.03428,-77.39628 , 0, 0, "North American")
BT = country("Bhutan", "Bhutan",27.514162 , 90.433601, 0, 0, "Indian")
BV = country("Bouvet Island", "NAN",-54.423199 ,3.413194 , 0, 0, "NAN")
BW = country("Botswana", "Gaborone",-22.328474 ,24.684866 , 0, 0, "African")
BY = country("Belarus", "Belarus",53.709807 ,27.953389 , 0, 0, "Eurasian")
BZ = country("Belize", "Belize", 17.189877, -88.49765, 0, 0, "Caribbean")
CA = country("Canada", "Ottawa", 56.130366, -106.346771, 0, 0, "North American")
CC = country("Cocos [Keeling] Islands", "West Island", -12.164165, 96.870956, 0, 0, "Indian")
CD = country("Congo [DRC]", "Congo [DRC]",-4.038333 , 21.758664, 0, 0, "African")
CF = country("Central African Republic", "Bangui", 6.611111, 20.939444, 0, 0, "African")
CG = country("Congo [Republic]", "Brazzaville",-0.228021 , 15.827659, 0, 0, "Brazzaville")
CH = country("Switzerland", "Bern",46.818188 , 8.227512, 0, 0, "Eurasian")
CI = country("Côte d'Ivoire", "Yamoussoukro",7.539989 , -5.54708, 0, 0, "African")
CK = country("Cook Islands", "NAN", -21.236736,-159.777671 , 0, 0, "NAN")
CL = country("Chile", "Santiago",-35.675147 , -71.542969, 0, 0, "South American")
CM = country("Cameroon", "Yaoundé", 7.369722,12.354722 , 0, 0, "African")
CN = country("China", "China", 35.86166, 104.195397, 0, 0, "Eurasian")
CO = country("Colombia", "Bogotá", 4.570868,-74.297333 , 0, 0, "South American")
CR = country("Costa Rica", "San José", 9.748917,-83.753428 , 0, 0, "South American")
CU = country("Cuba", "Havana",21.521757 ,-77.781167 , 0, 0, "North American")
CV = country("Cape Verde", "Praia",16.002082 , -24.013197, 0, 0, "African")
CX = country("Christmas Island", "Flying Fish Cove",-10.447525 ,105.690449, 0, 0, "NAN")
CY = country("Cyprus", "Nicosia", 35.126413, 33.429859, 0, 0, "Eurasian")
CZ = country("Czech Republic", "Prague", 49.817492, 15.472962, 0, 0, "Eurasian")
DE = country("Germany", "Berlin",51.165691 , 10.451526, 0, 0, "Eurasian")
DJ = country("Djibouti", "Djibouti City",11.825138 , 42.590275, 0, 0, "African")
DK = country("Denmark", "Copenhagen",56.26392 ,9.501785 , 0, 0, "Eurasian")
DM = country("Dominica", "Roseau", 15.414999, -61.370976, 0, 0, "Caribbean")
DO = country("Dominican Republic", "Santo Domingo",18.735693 , -70.162651, 0, 0, "Caribbean")
DZ = country("Algeria", "Algiers", 28.033886,1.659626 , 0, 0, "African")
EC = country("Ecuador", "Quito",-1.831239 , -78.183406, 0, 0, "South American")
EE = country("Estonia", "Tallinn", 58.595272,25.013607 , 0, 0, "Eurasian")
EG = country("Egypt", "Cairo", 26.820553, 30.802498, 0, 0, "Arabian")
EH = country("Western Sahara", "Laayoune", 24.215527, -12.885834, 0, 0, "African")
ER = country("Eritrea", "Asmara", 15.179384,39.782334 , 0, 0, "African")
ES = country("Spain", "Madrid",40.463667 , -3.74922, 0, 0, "Eurasian")
ET = country("Ethiopia", "Addis Ababa",9.145 ,40.489673 , 0, 0, "African")
FI = country("Finland", "Finland", 61.92411,25.748151 , 0, 0, "Eurasian")
FJ = country("Fiji", "Suva",-16.578193 , 179.414413, 0, 0, "Australian")
FK = country("Falkland Islands", "Stanley",-51.796253 ,-59.523613 , 0, 0, "NAN")
FM = country("Micronesia", "NAN", 7.425554,150.550812 , 0, 0, "Pacific")
FO = country("Faroe Islands", "Tórshavn",61.892635 ,-6.911806 , 0, 0, "Eurasian")
FR = country("France", "Paris",46.227638 , 2.213749, 0, 0, "Eurasian")
GA = country("Gabon", "Libreville", -0.803689, 11.609444, 0, 0, "African")
GB = country("United Kingdom", "London", 55.378051, -3.435973, 0, 0, "Eurasian")
GD = country("Grenada", "St. George",12.262776 ,-61.604171 , 0, 0, "Caribbean")
GE = country("Georgia", "Tbilisi", 42.315407,43.356892 , 0, 0, "Eurasian")
GF = country("French Guiana", "Cayenne", 3.933889, -53.125782, 0, 0, "South American")
GG = country("Guernsey", "NAN",49.465691 , -2.585278, 0, 0, "Eurasian")
GH = country("Ghana", "Accra", 7.946527, -1.023194, 0, 0, "African")
GI = country("Gibraltar", "Gibraltar",36.137741 , -5.345374, 0, 0, "Eurasian")
GL = country("Greenland", "Nuuk", 71.706936, -42.604303, 0, 0, "North American")
GM = country("Gambia", "Banjul",13.443182 , -15.310139, 0, 0, "African")
GN = country("Guinea", "Conakry",9.945587 , -9.696645, 0, 0, "African")
GP = country("Guadeloupe", "Basse-Terre",16.995971 , -62.067641, 0, 0, "Caribbean")
GQ = country("Equatorial Guinea", "Malabo", 1.650801, 10.267895, 0, 0, "African")
GR = country("Greece", "Athens",39.074208 ,21.824312 , 0, 0, "Eurasian")
GS = country("South Georgia and the South Sandwich Islands", "NAN", -54.429579, -36.587909, 0, 0, "Scotia")
GT = country("Guatemala", "Guatemala City", 15.783471, -90.230759, 0, 0, "Caribbean")
GU = country("Guam", "Agana",13.444304 , 144.793731, 0, 0, "Pacific")
GW = country("Guinea-Bissau", "Bissau", 11.803749,-15.180413 , 0, 0, "African")
GY = country("Guyana", "Georgetown", 4.860416,-58.93018 , 0, 0, "South American")
GZ = country("Gaza Strip", "NAN",31.354676 ,34.308825 , 0, 0, "Arabian")
HK = country("Hong Kong", "Hong Kong", 22.396428, 114.109497, 0, 0, "Eurasian")
HM = country("Heard Island and McDonald Islands", "NAN",-53.08181 ,73.504158 , 0, 0, "Indian")
HN = country("Honduras", "Tegucigalpa", 15.199999,-86.241905 , 0, 0, "Caribbean")
HR = country("Croatia", "Zagreb", 45.1, 15.2, 0, 0, "Eurasian")
HT = country("Haiti", "Port-au-Prince", 18.971187, -72.285215, 0, 0, "Caribbean")
HU = country("Hungary", "Budapest",47.162494 , 19.503304, 0, 0, "Eurasian")

ID = country("Indonesia", "Jakarta",-0.789275 ,113.921327 , 0, 0, "Eurasian")
IE = country("Ireland", "Dublin",53.41291 , -8.24389, 0, 0, "Eurasian")
IL = country("Palestine", "Jerusalem",31.046051 , 34.851612, 0, 0, "Arabian")
IN = country("India", "New Delhi",20.593684, 78.96288, 0, 0, "Indian")
IO = country("British Indian Ocean Territory", "NAN", -6.343194,71.876519 , 0, 0, "Indian")
IQ = country("Iraq", "Baghdad", 33.223191, 43.679291, 0, 0, "Arabian")
IR = country("Iran", "Tehran",32.427908 , 53.688046, 0, 0, "Eurasian")
IS = country("Iceland", "Reykjavik",64.963051 ,-19.020835 , 0, 0, "North American")
IT = country("Italy", "Rome",41.87194 ,12.56738 , 0, 0, "Eurasian")
JE = country("Jersey", "NAN", 49.214439,-2.13125 , 0, 0, "Eurasian")
JM = country("Jamaica", "Kingston",18.109581 ,-77.297508 , 0, 0, "North American")
JO = country("Jordan", "Amman", 30.585164,36.238414 , 0, 0, "Arabian")
JP = country("Japan", "Japan", 36.204824,138.252924 , 0, 0, "North American")
KE = country("Kenya", "Nairobi",-0.023559 ,37.906193 , 0, 0, "African")
KG = country("Kyrgyzstan", "Bishkek",41.20438 ,74.766098 , 0, 0, "Eurasian")
KH = country("Cambodia", "Phnom Penh",12.565679 ,104.990963 , 0, 0, "Eurasian")
KM = country("Comoros", "Moroni",-11.875001 , 43.872219, 0, 0, "African")
KN = country("Saint Kitts and Nevis", "Basseterre",17.357822 , -62.782998, 0, 0, "Caribbean")
KP = country("North Korea", "Pyongyang",40.339852 ,127.510093 , 0, 0, "Eurasian")
KR = country("South Korea", "Seoul",35.907757 , 127.766922, 0, 0, "Eurasian")
KW = country("Kuwait", "Kuwait City",29.31166 ,47.481766 , 0, 0, "Arabian")
KY = country("Cayman Islands", "George Town", 19.513469,-80.566956 , 0, 0, "Caribbean")
KZ = country("Kazakhstan", "Astana",48.019573 ,66.923684 , 0, 0, "Eurasian")
LA = country("Laos", "Vientiane",19.85627 ,102.495496 , 0, 0, "Eurasian")
LB = country("Lebanon", "Beirut",33.854721 ,35.862285 , 0, 0, "Arabian")
LC = country("Saint Lucia", "Castries",13.909444 ,-60.978893 , 0, 0, "Caribbean")
LI = country("Liechtenstein", "Vaduz",47.166 ,9.555373 , 0, 0, "Eurasian")
LK = country("Sri Lanka", "Colombo",7.873054 ,80.771797 , 0, 0, "Indian")
LR = country("Liberia", "Monrovia",6.428055 ,-9.429499 , 0, 0, "African")
LS = country("Lesotho", "Maseru", -29.609988, 28.233608, 0, 0, "African")
LT = country("Lithuania", "Vilnius",55.169438 ,23.881275 , 0, 0, "Eurasian")
LU = country("Luxembourg", "Luxembourg City",49.815273 ,6.129583 , 0, 0, "Eurasian")
LV = country("Latvia", "Riga",56.879635 ,24.603189 , 0, 0, "Eurasian")
LY = country("Libya", "Tripoli", 26.3351,17.228331 , 0, 0, "African")
MA = country("Morocco", "Rabat", 31.791702,-7.09262 , 0, 0, "African")
MC = country("Monaco", "Monaco-Ville",43.750298 ,7.412841 , 0, 0, "Eurasian")
MD = country("Moldova", "Chișinău",47.411631 , 28.369885, 0, 0, "Eurasian")
ME = country("Montenegro", "Podgorica",42.708678 ,19.37439 , 0, 0, "Eurasian")
MG = country("Madagascar", "Madagascar", -18.766947,46.869107 , 0, 0, "Somali")
MH = country("Marshall Islands", "Majuro",7.131474 ,171.184478 , 0, 0, "Pacific")
MK = country("Macedonia", "Skopje",41.608635 ,21.745275 , 0, 0, "Eurasian")
ML = country("Mali", "Bamako", 17.570692,-3.996166 , 0, 0, "African")
MM = country("Myanmar", "Naypyidaw", 21.913965,95.956223 , 0, 0, "Indian")
MN = country("Mongolia", "Mongolia",46.862496 ,103.846656 , 0, 0, "Eurasian")
MO = country("Macau", "Macau",22.198745 , 113.543873, 0, 0, "Eurasian")
MP = country("Northern Mariana Islands", "Saipan",17.33083 , 145.38469, 0, 0, "Pacific")
MQ = country("Martinique", "Fort-de-France",14.641528 ,-61.024174 , 0, 0, "Caribbean")
MR = country("Mauritania", "Nouakchott",21.00789 ,-10.940835 , 0, 0, "African")
MS = country("Montserrat", "Plymouth",16.742498 , -62.187366, 0, 0, "Caribbean")
MT = country("Malta", "Valletta",35.937496 ,14.375416 , 0, 0, "African")
MU = country("Mauritius", "Port Louis",-20.348404 ,57.552152 , 0, 0, "African")
MV = country("Maldives", "Malé", 3.202778, 73.22068, 0, 0, "Indian")
MW = country("Malawi", "Lilongwe",-13.254308 ,34.301525 , 0, 0, "African")
MX = country("Mexico", "Mexico City",23.634501 ,-102.552784 , 0, 0, "Cocos")
MY = country("Malaysia", "Kuala Lumpur",4.210484 ,101.975766 , 0, 0, "Eurasian")
MZ = country("Mozambique", "Maputo",-18.665695 ,35.529562 , 0, 0, "African")
NA = country("Namibia", "Windhoek",-22.95764 ,18.49041 , 0, 0, "African")
NC = country("New Caledonia", "Nouméa",-20.904305 ,165.618042 , 0, 0, "Pacific")
NE = country("Niger", "Niamey",17.607789 ,8.081666 , 0, 0, "African")
NG = country("Nigeria", "Abuja",9.081999 ,8.675277 , 0, 0, "African")
NI = country("Nicaragua", "Managua",12.865416 ,-85.207229 , 0, 0, "Cocos")
NL = country("Netherlands", "Amsterdam", 52.132633, 5.291266, 0, 0, "Eurasian")
NO = country("Norway", "Oslo",60.472024 ,8.468946 , 0, 0, "Eurasian")
NP = country("Nepal", "Kathmandu",28.394857 ,84.124008 , 0, 0, "Indian")
NR = country("Nauru", "Yaren",-0.522778 ,166.931503 , 0, 0, "Pacific")
NU = country("Niue", "Alofi",-19.054445 ,-169.867233 , 0, 0, "Pacific")
NZ = country("New Zealand", "Wellington", -40.900557, 174.885971, 0, 0, "Pacific")
OM = country("Oman", "Muscat",21.512583 ,55.923255 , 0, 0, "Arabian")
PA = country("Panama", "Panama City",8.537981 , -80.782127, 0, 0, "South America")
PE = country("Peru", "Lima",-9.189967 ,-75.015152 , 0, 0, "Nazca")
PF = country("French Polynesia", "NAN",-17.679742 ,-149.406843 , 0, 0, "Pacific")
PG = country("Papua New Guinea", "Port Moresby", -6.314993,143.95555 , 0, 0, "Australian")
PH = country("Philippines", "Manila",12.879721 ,121.774017 , 0, 0, "Philippine Sea")
PK = country("Pakistan", "Islamabad",30.375321 ,69.345116 , 0, 0, "Indian")
PL = country("Poland", "Warsaw",51.919438 ,19.145136 , 0, 0, "Eurasian")
PM = country("Saint Pierre and Miquelon", "Saint-Pierre",46.941936 ,-56.27111 , 0, 0, "North American")
PN = country("Pitcairn Islands", "Adamstown", -24.703615, -127.439308, 0, 0, "Pacific")
PR = country("Puerto Rico", "San Juan", 18.220833, -66.590149 , 0, 0, "Caribbean")
PS = country("Palestinian", "Jerusalem", 31.952162, 35.233154 , 0, 0, "Arabian")
PT = country("Portugal", "Lisbon",39.399872 ,-8.224454 , 0, 0, "Eurasian")
PW = country("Palau", "Ngerulmud",7.51498 , 134.58252, 0, 0, "Philippine Sea")
PY = country("Paraguay", "Asunción", -23.442503, -58.443832, 0, 0, "South American")
QA = country("Qatar", "Doha", 25.354826, 51.183884, 0, 0, "Arabian")
RE = country("Réunion", "Saint-Denis", -21.115141, 55.536384, 0, 0, "African")
RO = country("Romania", "Bucharest",45.943161 ,24.96676 , 0, 0, "Eurasian")
RS = country("Serbia", "Belgrade",44.016521 ,21.005859 , 0, 0, "Eurasian")
RU = country("Russia", "Russia",61.52401 ,105.318756 , 0, 0, "Eurasian")
RW = country("Rwanda", "Kigali",-1.940278 ,29.873888 , 0, 0, "African")
SA = country("Saudi Arabia", "Riyad",23.885942 ,45.079162 , 0, 0, "Arabian")
SB = country("Solomon Islands", "Honiara",-9.64571 , 160.156194, 0, 0, "Pacific")
SC = country("Seychelles", "Victoria", -4.679574, 55.491977, 0, 0, "Somali")
SD = country("Sudan", "Khartoum",12.862807 , 30.217636, 0, 0, "African")
SE = country("Sweden", "Stockholm",60.128161 ,18.643501 , 0, 0, "Eurasian")
SG = country("Singapore", "Singapore",1.352083 ,103.819836 , 0, 0, "Singapore")
SH = country("Saint Helena", "Jamestown",-24.143474 , -10.030696, 0, 0, "African")
SI = country("Slovenia", "Ljubljana",46.151241 ,14.995463 , 0, 0, "Eurasian")
SJ = country("Svalbard and Jan Mayen", "NAN", 77.553604,23.670272 , 0, 0, "Eurasian")
SK = country("Slovakia", "Bratislava",48.669026 ,19.699024 , 0, 0, "Eurasian")
SL = country("Sierra Leone", "Freetown", 8.460555, -11.779889, 0, 0, "African")
SM = country("San Marino", "San Marino",43.94236 ,12.457777 , 0, 0, "Eurasian")
SN = country("Senegal", "Dakar", 14.497401, -14.452362, 0, 0, "African")

SO = country("Somalia", "Mogadishu",5.152149 , 46.199616, 0, 0, "Somali")
SR = country("Suriname", "Paramaribo",3.919305 ,-56.027783, 0, 0, "South American")
ST = country("São Tomé and Príncipe", "São Tomé",0.18636 , 6.613081, 0, 0, "African")
SV = country("El Salvador", " San Salvado",13.794185 ,-88.89653 , 0, 0, "Cocos")
SY = country("Syria", "Damascus",34.802075 ,38.996815 , 0, 0, "Arabian")
SZ = country("Swaziland", "Mbabane",-26.522503 , 31.465866, 0, 0, "African")
TC = country("Turks and Caicos Islands", "Cockburn Town", 21.694025,-71.797928 , 0, 0, "North American")
TD = country("Chad", "N'Djamena",15.454166 , 18.732207, 0, 0, "African")
TF = country("French Southern Territories", "NAN",-49.280366 ,69.348557 , 0, 0, "NAN")
TG = country("Togo", "Lomé",8.619543 ,0.824782 , 0, 0, "African")
TH = country("Thailand", "Bangkok",15.870032 ,100.992541 , 0, 0, "Eurasian")
TJ = country("Tajikistan", "Dushanbe", 38.861034, 71.276093, 0, 0, "Indian")
TK = country("Tokelau", "NAN",-8.967363 ,-171.855881 , 0, 0, "Pacific")
TL = country("Timor-Leste", "Dili",-8.874217 , 125.727539, 0, 0, "Australian")
TM = country("Turkmenistan", "Ashgabat",38.969719 ,59.556278 , 0, 0, "Eurasian")
TN = country("Tunisia", "Tunis",33.886917 ,9.537499 , 0, 0, "African")
TO = country("Tonga", "Nuku'alofa",-21.178986 ,-175.198242 , 0, 0, "Pacific")
TR = country("Turkey", "Ankara", 38.963745,35.243322 , 0, 0, "Eurasian")
TT = country("Trinidad and Tobago", "Port of Spain",10.691803 ,-61.222503 , 0, 0, "Caribbean")
TV = country("Tuvalu", "Funafuti",-7.109535,177.64933 , 0, 0, "Pacific")
TW = country("Taiwan", "Taipei",23.69781 ,120.960515 , 0, 0, "Eurasian")
TZ = country("Tanzania", "Dodoma",-6.369028 ,34.888822 , 0, 0, "African")
UA = country("Ukraine", "Kyiv",48.379433 ,31.16558 , 0, 0, "Eurasian")
UG = country("Uganda", "Kampala",1.373333 ,32.290275 , 0, 0, "African")
US = country("United States", "Washington",37.09024 , -95.712891, 0, 0, "North American")
UY = country("Uruguay", "Montevideo",-32.522779 ,-55.765835 , 0, 0, "South American")
UZ = country("Uzbekistan", "Tashkent",41.377491 ,64.585262 , 0, 0, "Eurasian")
VA = country("Vatican City", "Vatican City",41.902916 ,12.453389 , 0, 0, "Eurasian")
VC = country("Saint Vincent and the Grenadines", "Kingstown",12.984305 ,-61.287228 , 0, 0, "Caribbean")
VE = country("Venezuela", "Caracas",6.42375 ,-66.58973 , 0, 0, "South American")
VG = country("British Virgin Islands", "Road Town",18.420695 ,-64.639968 , 0, 0, "Caribbean")
VI = country("U.S. Virgin Islands", "Charlotte Amalie", 18.335765,-64.896335 , 0, 0, "Caribbean")
VN = country("Vietnam", "Hanoi",14.058324 ,108.277199 , 0, 0, "Eurasian")
VU = country("Vanuatu", "Port Vila",-15.376706 ,166.959158, 0, 0, "Australian")
WF = country("Wallis and Futuna", "Mata-Utu", -13.768752,-177.156097 , 0, 0, "Pacific")
WS = country("Samoa", "Apia",-13.759029 ,-172.104629 , 0, 0, "Pacific")
XK = country("Kosovo", "Pristina",42.602636 , 20.902977, 0, 0, "Eurasian")
YE = country("Yemen", "Sana'a",15.552727 ,48.516388 , 0, 0, "Arabian")
YT = country("Mayotte", "Mamoudzou", -12.8275,45.166244 , 0, 0, "Somali")
ZA = country("South Africa", "Pretoria",-30.559482 , 22.937506, 0, 0, "African")
ZM = country("Zambia", "Lusaka", -13.133897,27.849332 , 0, 0, "African")
ZW = country("Zimbabwe", "Harare", -19.015438, 29.154857 , 0, 0, "African")

# List of countries
countriesList = [
<<<<<<< HEAD
    
    # Add more countries here...
   AD, AE, AF, AG, AI,
   AL, AM, AN, AT, AU, AW,
   AZ, BA, BB, BD, BE, BF,
   BG, BH, BI, BJ, BM, BN,
   BO, BR, BS, BT, BV, CL, 
   CM, CN, CO, CR, DE, DJ, 
   DK, DM, DO, DZ, EC, EE, 
   EG, EH, ER, ES, ET, FI, 
   FJ, FK, GD, GE, GF, GG, 
   GH, GI, GL, GM, GN, GP, 
   GQ, HN, HR, HT, HU, ID, 
   IE, IL, KW, KY, LR, LS, 
   LT, LU, LV, LY, MA, MC, 
   MD, ME, MG, MH, NG, NI, 
   NL, NO, NP, NR, NU, NZ, 
   OM, PA, PE, PF, SC, SD, 
   SE, SG, SH, SK, SL, SM, 
   SN, SO, SR, ST, SV, SY, 
   SZ, TC, TD, TF, TG, TH, 
   TJ, TK, TL, TM, TN, TO, 
   TR, TT, TV, TW, TZ, UA, 
   UG, US, UY, UZ, VA, VC, 
   VE, VG, VI, VN, VU, WF, 
   WS, XK, YE, YT, ZA, ZM, ZW

]
countriesList.sort()
=======
    eg,
    us
    # Add more countries here...
]
>>>>>>> 3ab4be66f23a0734ae766e0af8b03512c3c40eb7
