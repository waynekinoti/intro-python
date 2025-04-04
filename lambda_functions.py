# lambda_functions
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))



add_two = lambda x, y: x + y

print(add_two(5, 15))

multiply_three = lambda a, b, c: a * b * c

print(multiply_three(2, 3, 4))

students = [{"id":1,"names":"Valene de Leon","gender":"Female","maths":78,"english":86,"kiswahili":57,"chemistry":71,"biology":63,"accounting":68,"history":45},
{"id":2,"names":"Rhodia Batterson","gender":"Female","maths":66,"english":80,"kiswahili":53,"chemistry":19,"biology":67,"accounting":28,"history":23},
{"id":3,"names":"Lillis Searston","gender":"Female","maths":52,"english":47,"kiswahili":57,"chemistry":35,"biology":72,"accounting":58,"history":58},
{"id":4,"names":"Selle Stobbie","gender":"Female","maths":30,"english":55,"kiswahili":24,"chemistry":69,"biology":79,"accounting":44,"history":46},
{"id":5,"names":"Hansiain Tackes","gender":"Male","maths":36,"english":13,"kiswahili":77,"chemistry":19,"biology":48,"accounting":43,"history":49},
{"id":6,"names":"Gaby Gierhard","gender":"Male","maths":21,"english":37,"kiswahili":63,"chemistry":30,"biology":65,"accounting":58,"history":61},
{"id":7,"names":"Chlo Garment","gender":"Female","maths":21,"english":21,"kiswahili":64,"chemistry":51,"biology":28,"accounting":39,"history":64},
{"id":8,"names":"Stavro McNally","gender":"Male","maths":13,"english":40,"kiswahili":73,"chemistry":36,"biology":72,"accounting":35,"history":70},
{"id":9,"names":"Ber Porteous","gender":"Male","maths":17,"english":22,"kiswahili":49,"chemistry":43,"biology":29,"accounting":65,"history":36},
{"id":10,"names":"Ilario Nation","gender":"Male","maths":57,"english":82,"kiswahili":86,"chemistry":43,"biology":25,"accounting":87,"history":56},
{"id":11,"names":"Kippie Woodroffe","gender":"Male","maths":12,"english":56,"kiswahili":36,"chemistry":19,"biology":66,"accounting":54,"history":56},
{"id":12,"names":"Monty Melato","gender":"Male","maths":62,"english":24,"kiswahili":14,"chemistry":22,"biology":28,"accounting":43,"history":69},
{"id":13,"names":"Alexandrina Rebbeck","gender":"Female","maths":66,"english":18,"kiswahili":75,"chemistry":53,"biology":41,"accounting":88,"history":50},
{"id":14,"names":"Tymothy Sarle","gender":"Male","maths":15,"english":31,"kiswahili":40,"chemistry":40,"biology":53,"accounting":41,"history":75},
{"id":15,"names":"Marti Eriksson","gender":"Female","maths":43,"english":32,"kiswahili":59,"chemistry":26,"biology":22,"accounting":31,"history":16},
{"id":16,"names":"Hoebart Ducroe","gender":"Male","maths":47,"english":19,"kiswahili":13,"chemistry":62,"biology":81,"accounting":62,"history":73},
{"id":17,"names":"Dela Bruckshaw","gender":"Female","maths":44,"english":30,"kiswahili":41,"chemistry":34,"biology":34,"accounting":82,"history":60},
{"id":18,"names":"Sylvan Mapstone","gender":"Male","maths":31,"english":43,"kiswahili":44,"chemistry":33,"biology":55,"accounting":19,"history":38},
{"id":19,"names":"Noelani Fleury","gender":"Female","maths":56,"english":25,"kiswahili":68,"chemistry":27,"biology":40,"accounting":32,"history":32},
{"id":20,"names":"Gillie Roma","gender":"Female","maths":70,"english":67,"kiswahili":60,"chemistry":13,"biology":44,"accounting":78,"history":32},
{"id":21,"names":"Maxy Abelson","gender":"Male","maths":75,"english":57,"kiswahili":21,"chemistry":20,"biology":65,"accounting":63,"history":18},
{"id":22,"names":"Eolande Rogez","gender":"Female","maths":82,"english":41,"kiswahili":49,"chemistry":19,"biology":90,"accounting":85,"history":59},
{"id":23,"names":"Gonzales Foch","gender":"Male","maths":54,"english":41,"kiswahili":28,"chemistry":10,"biology":75,"accounting":29,"history":32},
{"id":24,"names":"Gretna McGrouther","gender":"Female","maths":30,"english":17,"kiswahili":72,"chemistry":64,"biology":48,"accounting":50,"history":85},
{"id":25,"names":"Brad Sprowson","gender":"Male","maths":85,"english":42,"kiswahili":71,"chemistry":10,"biology":54,"accounting":42,"history":57},
{"id":26,"names":"Keir Tyght","gender":"Male","maths":25,"english":36,"kiswahili":37,"chemistry":34,"biology":85,"accounting":11,"history":39},
{"id":27,"names":"Shirline Garrattley","gender":"Female","maths":54,"english":51,"kiswahili":49,"chemistry":27,"biology":53,"accounting":28,"history":42},
{"id":28,"names":"Latrena Goskar","gender":"Female","maths":53,"english":13,"kiswahili":24,"chemistry":66,"biology":15,"accounting":54,"history":49},
{"id":29,"names":"Barby McGerraghty","gender":"Female","maths":19,"english":16,"kiswahili":37,"chemistry":32,"biology":56,"accounting":55,"history":54},
{"id":30,"names":"Frances Roughan","gender":"Female","maths":65,"english":46,"kiswahili":12,"chemistry":22,"biology":76,"accounting":43,"history":41},
{"id":31,"names":"Vergil Sturton","gender":"Male","maths":53,"english":40,"kiswahili":68,"chemistry":63,"biology":74,"accounting":37,"history":19},
{"id":32,"names":"Lucretia Yitzhakov","gender":"Female","maths":83,"english":44,"kiswahili":51,"chemistry":32,"biology":90,"accounting":15,"history":13},
{"id":33,"names":"Jorey Goward","gender":"Female","maths":62,"english":79,"kiswahili":20,"chemistry":50,"biology":35,"accounting":82,"history":25},
{"id":34,"names":"Isahella Leggan","gender":"Female","maths":28,"english":18,"kiswahili":27,"chemistry":18,"biology":87,"accounting":74,"history":74},
{"id":35,"names":"Barbra Mallinson","gender":"Female","maths":65,"english":36,"kiswahili":85,"chemistry":69,"biology":86,"accounting":71,"history":86},
{"id":36,"names":"Deborah Parnham","gender":"Female","maths":63,"english":34,"kiswahili":63,"chemistry":30,"biology":11,"accounting":24,"history":42},
{"id":37,"names":"Clint Tidey","gender":"Male","maths":79,"english":44,"kiswahili":11,"chemistry":49,"biology":60,"accounting":71,"history":81},
{"id":38,"names":"Jaimie Sinfield","gender":"Male","maths":82,"english":66,"kiswahili":17,"chemistry":42,"biology":31,"accounting":49,"history":51},
{"id":39,"names":"Cosetta Cundey","gender":"Female","maths":56,"english":77,"kiswahili":30,"chemistry":35,"biology":38,"accounting":63,"history":55},
{"id":40,"names":"Stuart Fishley","gender":"Male","maths":39,"english":24,"kiswahili":78,"chemistry":49,"biology":67,"accounting":12,"history":52},
{"id":41,"names":"Syd Goodfellowe","gender":"Male","maths":73,"english":38,"kiswahili":30,"chemistry":35,"biology":40,"accounting":51,"history":41},
{"id":42,"names":"Udall Critten","gender":"Male","maths":21,"english":52,"kiswahili":50,"chemistry":61,"biology":84,"accounting":35,"history":82},
{"id":43,"names":"Cati Doley","gender":"Female","maths":21,"english":48,"kiswahili":82,"chemistry":65,"biology":73,"accounting":29,"history":76},
{"id":44,"names":"Marietta Kubin","gender":"Female","maths":41,"english":12,"kiswahili":40,"chemistry":52,"biology":56,"accounting":71,"history":51},
{"id":45,"names":"Ulrich Portinari","gender":"Male","maths":15,"english":23,"kiswahili":57,"chemistry":37,"biology":16,"accounting":45,"history":83},
{"id":46,"names":"Lula Iczokvitz","gender":"Female","maths":59,"english":17,"kiswahili":81,"chemistry":42,"biology":38,"accounting":55,"history":63},
{"id":47,"names":"Farra Oldham","gender":"Female","maths":49,"english":52,"kiswahili":45,"chemistry":28,"biology":54,"accounting":46,"history":24},
{"id":48,"names":"Phoebe Bloxham","gender":"Female","maths":14,"english":38,"kiswahili":46,"chemistry":10,"biology":44,"accounting":79,"history":38},
{"id":49,"names":"Leela Hames","gender":"Female","maths":46,"english":84,"kiswahili":20,"chemistry":44,"biology":15,"accounting":90,"history":32},
{"id":50,"names":"Craggy Etienne","gender":"Male","maths":45,"english":24,"kiswahili":22,"chemistry":11,"biology":33,"accounting":16,"history":53},
{"id":51,"names":"Carlyn Millimoe","gender":"Female","maths":62,"english":51,"kiswahili":60,"chemistry":52,"biology":64,"accounting":55,"history":59},
{"id":52,"names":"Morie Dalglish","gender":"Male","maths":85,"english":16,"kiswahili":73,"chemistry":53,"biology":52,"accounting":71,"history":81},
{"id":53,"names":"Bearnard MacAlaster","gender":"Male","maths":74,"english":72,"kiswahili":31,"chemistry":63,"biology":79,"accounting":64,"history":82},
{"id":54,"names":"Wait Flohard","gender":"Male","maths":74,"english":48,"kiswahili":25,"chemistry":63,"biology":21,"accounting":53,"history":63},
{"id":55,"names":"Birdie Sive","gender":"Female","maths":50,"english":47,"kiswahili":30,"chemistry":19,"biology":66,"accounting":56,"history":57},
{"id":56,"names":"Gill Castane","gender":"Female","maths":70,"english":20,"kiswahili":44,"chemistry":53,"biology":88,"accounting":60,"history":51},
{"id":57,"names":"Phillis Lumsden","gender":"Female","maths":13,"english":33,"kiswahili":70,"chemistry":54,"biology":35,"accounting":31,"history":89},
{"id":58,"names":"Abner Donizeau","gender":"Male","maths":25,"english":31,"kiswahili":47,"chemistry":21,"biology":16,"accounting":13,"history":28},
{"id":59,"names":"Gladi Shermar","gender":"Female","maths":71,"english":59,"kiswahili":32,"chemistry":51,"biology":67,"accounting":86,"history":81},
{"id":60,"names":"Morlee Cotgrove","gender":"Male","maths":23,"english":65,"kiswahili":38,"chemistry":10,"biology":74,"accounting":37,"history":47},
{"id":61,"names":"Janaye Phython","gender":"Female","maths":45,"english":60,"kiswahili":63,"chemistry":42,"biology":12,"accounting":23,"history":72},
{"id":62,"names":"Annabel Hardey","gender":"Female","maths":77,"english":32,"kiswahili":70,"chemistry":63,"biology":34,"accounting":45,"history":87},
{"id":63,"names":"Kingsly Weyman","gender":"Male","maths":70,"english":83,"kiswahili":75,"chemistry":16,"biology":50,"accounting":30,"history":51},
{"id":64,"names":"Zelda Baunton","gender":"Female","maths":18,"english":29,"kiswahili":26,"chemistry":37,"biology":50,"accounting":22,"history":35},
{"id":65,"names":"Karin Tredgold","gender":"Female","maths":45,"english":13,"kiswahili":35,"chemistry":14,"biology":47,"accounting":26,"history":42},
{"id":66,"names":"Felicia Crosswaite","gender":"Female","maths":65,"english":40,"kiswahili":48,"chemistry":29,"biology":73,"accounting":45,"history":73},
{"id":67,"names":"Silas Emm","gender":"Male","maths":26,"english":24,"kiswahili":16,"chemistry":62,"biology":28,"accounting":40,"history":85},
{"id":68,"names":"Dallas Renac","gender":"Male","maths":69,"english":37,"kiswahili":60,"chemistry":36,"biology":87,"accounting":15,"history":65},
{"id":69,"names":"Gilberta Dabell","gender":"Female","maths":41,"english":65,"kiswahili":71,"chemistry":49,"biology":28,"accounting":78,"history":48},
{"id":70,"names":"Langsdon Husbands","gender":"Male","maths":29,"english":40,"kiswahili":56,"chemistry":52,"biology":19,"accounting":59,"history":82},
{"id":71,"names":"Myra Statefield","gender":"Female","maths":18,"english":72,"kiswahili":40,"chemistry":28,"biology":17,"accounting":67,"history":25},
{"id":72,"names":"Tallie Dupree","gender":"Female","maths":50,"english":85,"kiswahili":55,"chemistry":12,"biology":58,"accounting":44,"history":41},
{"id":73,"names":"Sonny Lamp","gender":"Male","maths":34,"english":20,"kiswahili":81,"chemistry":24,"biology":55,"accounting":76,"history":53},
{"id":74,"names":"Austin Hunnisett","gender":"Female","maths":25,"english":44,"kiswahili":63,"chemistry":11,"biology":59,"accounting":53,"history":14},
{"id":75,"names":"Bryce Cooling","gender":"Male","maths":75,"english":60,"kiswahili":66,"chemistry":15,"biology":58,"accounting":53,"history":38},
{"id":76,"names":"Jeremy Wickersham","gender":"Male","maths":86,"english":12,"kiswahili":72,"chemistry":53,"biology":68,"accounting":68,"history":87},
{"id":77,"names":"Josy Clowney","gender":"Female","maths":79,"english":54,"kiswahili":86,"chemistry":15,"biology":17,"accounting":49,"history":38},
{"id":78,"names":"Dmitri McGougan","gender":"Male","maths":70,"english":75,"kiswahili":68,"chemistry":24,"biology":86,"accounting":85,"history":20},
{"id":79,"names":"Joleen Coogan","gender":"Female","maths":11,"english":44,"kiswahili":27,"chemistry":48,"biology":68,"accounting":58,"history":31},
{"id":80,"names":"Saxe Mayo","gender":"Male","maths":28,"english":68,"kiswahili":31,"chemistry":67,"biology":22,"accounting":50,"history":65},
{"id":81,"names":"Bram Ellif","gender":"Male","maths":38,"english":50,"kiswahili":19,"chemistry":47,"biology":53,"accounting":67,"history":28},
{"id":82,"names":"Talya Candy","gender":"Female","maths":80,"english":64,"kiswahili":22,"chemistry":26,"biology":16,"accounting":73,"history":31},
{"id":83,"names":"Karita Shore","gender":"Female","maths":14,"english":69,"kiswahili":44,"chemistry":56,"biology":45,"accounting":47,"history":23},
{"id":84,"names":"Rochelle O'Scollee","gender":"Female","maths":79,"english":46,"kiswahili":83,"chemistry":58,"biology":12,"accounting":41,"history":82},
{"id":85,"names":"Leoine Camplejohn","gender":"Female","maths":43,"english":63,"kiswahili":25,"chemistry":38,"biology":27,"accounting":62,"history":18},
{"id":86,"names":"Rowan Seadon","gender":"Male","maths":20,"english":15,"kiswahili":54,"chemistry":26,"biology":39,"accounting":26,"history":63},
{"id":87,"names":"Skylar Giacomoni","gender":"Male","maths":27,"english":83,"kiswahili":70,"chemistry":55,"biology":21,"accounting":35,"history":57},
{"id":88,"names":"Yuri Gorhardt","gender":"Male","maths":11,"english":45,"kiswahili":17,"chemistry":57,"biology":32,"accounting":30,"history":84},
{"id":89,"names":"Wyn Layman","gender":"Male","maths":19,"english":76,"kiswahili":74,"chemistry":22,"biology":14,"accounting":69,"history":53},
{"id":90,"names":"Rolph Thraves","gender":"Male","maths":27,"english":25,"kiswahili":52,"chemistry":30,"biology":84,"accounting":28,"history":34},
{"id":91,"names":"Jaynell Hakey","gender":"Female","maths":84,"english":83,"kiswahili":12,"chemistry":26,"biology":66,"accounting":23,"history":85},
{"id":92,"names":"Salem Marcinkus","gender":"Male","maths":54,"english":54,"kiswahili":48,"chemistry":36,"biology":52,"accounting":87,"history":55},
{"id":93,"names":"Xavier Gregor","gender":"Male","maths":51,"english":73,"kiswahili":74,"chemistry":10,"biology":85,"accounting":80,"history":60},
{"id":94,"names":"Talyah Ellsom","gender":"Female","maths":74,"english":11,"kiswahili":39,"chemistry":42,"biology":52,"accounting":87,"history":63},
{"id":95,"names":"Anitra Straffon","gender":"Female","maths":64,"english":33,"kiswahili":18,"chemistry":14,"biology":60,"accounting":26,"history":56},
{"id":96,"names":"Wainwright Jakubovits","gender":"Male","maths":45,"english":67,"kiswahili":53,"chemistry":67,"biology":12,"accounting":41,"history":16},
{"id":97,"names":"Aileen Ludron","gender":"Female","maths":35,"english":73,"kiswahili":34,"chemistry":42,"biology":12,"accounting":54,"history":55},
{"id":98,"names":"Anne Hawkings","gender":"Female","maths":50,"english":75,"kiswahili":84,"chemistry":29,"biology":28,"accounting":25,"history":39},
{"id":99,"names":"Dion Castelluzzi","gender":"Male","maths":21,"english":56,"kiswahili":15,"chemistry":25,"biology":70,"accounting":58,"history":78},
{"id":100,"names":"Kalindi Wilkes","gender":"Female","maths":72,"english":22,"kiswahili":33,"chemistry":47,"biology":87,"accounting":66,"history":40},
{"id":101,"names":"Corbie Gregson","gender":"Male","maths":13,"english":31,"kiswahili":18,"chemistry":70,"biology":66,"accounting":60,"history":90},
{"id":102,"names":"Caitrin Slateford","gender":"Female","maths":45,"english":35,"kiswahili":69,"chemistry":70,"biology":64,"accounting":23,"history":79},
{"id":103,"names":"Kalila Pallas","gender":"Female","maths":31,"english":55,"kiswahili":57,"chemistry":15,"biology":27,"accounting":56,"history":45},
{"id":104,"names":"Doti Petto","gender":"Female","maths":45,"english":33,"kiswahili":60,"chemistry":27,"biology":15,"accounting":85,"history":77},
{"id":105,"names":"Anny Lightbourn","gender":"Female","maths":66,"english":75,"kiswahili":32,"chemistry":54,"biology":52,"accounting":63,"history":48},
{"id":106,"names":"Aubine Biggadike","gender":"Female","maths":85,"english":35,"kiswahili":70,"chemistry":17,"biology":36,"accounting":31,"history":25},
{"id":107,"names":"Audry Silvermann","gender":"Female","maths":72,"english":69,"kiswahili":46,"chemistry":40,"biology":72,"accounting":13,"history":88},
{"id":108,"names":"Gena Pierce","gender":"Female","maths":57,"english":52,"kiswahili":30,"chemistry":13,"biology":22,"accounting":40,"history":16},
{"id":109,"names":"Vlad Guttridge","gender":"Male","maths":19,"english":74,"kiswahili":23,"chemistry":11,"biology":11,"accounting":45,"history":56},
{"id":110,"names":"Grazia Kalkhoven","gender":"Female","maths":79,"english":84,"kiswahili":75,"chemistry":11,"biology":60,"accounting":86,"history":26},
{"id":111,"names":"Gerrard Borkin","gender":"Male","maths":52,"english":80,"kiswahili":33,"chemistry":29,"biology":39,"accounting":27,"history":20},
{"id":112,"names":"Cad Jacobsson","gender":"Male","maths":45,"english":71,"kiswahili":12,"chemistry":75,"biology":59,"accounting":30,"history":69},
{"id":113,"names":"Rafaellle Booker","gender":"Male","maths":38,"english":50,"kiswahili":74,"chemistry":23,"biology":25,"accounting":46,"history":22},
{"id":114,"names":"Florence Wreford","gender":"Female","maths":74,"english":52,"kiswahili":76,"chemistry":21,"biology":89,"accounting":71,"history":55},
{"id":115,"names":"Jimmie Gittoes","gender":"Male","maths":78,"english":40,"kiswahili":75,"chemistry":57,"biology":88,"accounting":22,"history":19},
{"id":116,"names":"Frans Stebles","gender":"Male","maths":41,"english":24,"kiswahili":33,"chemistry":50,"biology":39,"accounting":54,"history":38},
{"id":117,"names":"Kerr Pantling","gender":"Male","maths":60,"english":26,"kiswahili":64,"chemistry":22,"biology":31,"accounting":90,"history":88},
{"id":118,"names":"Garland Killelea","gender":"Female","maths":75,"english":58,"kiswahili":47,"chemistry":20,"biology":17,"accounting":62,"history":71},
{"id":119,"names":"Shelba Harm","gender":"Female","maths":80,"english":43,"kiswahili":85,"chemistry":44,"biology":15,"accounting":84,"history":81},
{"id":120,"names":"Jeff Verna","gender":"Male","maths":86,"english":55,"kiswahili":51,"chemistry":39,"biology":86,"accounting":74,"history":71},
{"id":121,"names":"Neil Elmore","gender":"Male","maths":31,"english":22,"kiswahili":57,"chemistry":45,"biology":65,"accounting":16,"history":52},
{"id":122,"names":"Maximo Jellybrand","gender":"Male","maths":12,"english":84,"kiswahili":52,"chemistry":30,"biology":70,"accounting":18,"history":49},
{"id":123,"names":"Hazel Vitte","gender":"Male","maths":74,"english":16,"kiswahili":40,"chemistry":67,"biology":89,"accounting":27,"history":61},
{"id":124,"names":"Tersina Mettetal","gender":"Female","maths":30,"english":15,"kiswahili":85,"chemistry":43,"biology":56,"accounting":46,"history":54},
{"id":125,"names":"Devon Goaley","gender":"Female","maths":24,"english":68,"kiswahili":43,"chemistry":34,"biology":51,"accounting":18,"history":89},
{"id":126,"names":"Christina Klimsch","gender":"Female","maths":21,"english":77,"kiswahili":33,"chemistry":55,"biology":81,"accounting":58,"history":33},
{"id":127,"names":"Nealy Jewise","gender":"Male","maths":66,"english":70,"kiswahili":50,"chemistry":69,"biology":11,"accounting":61,"history":29},
{"id":128,"names":"Lisabeth Budnik","gender":"Female","maths":28,"english":30,"kiswahili":54,"chemistry":10,"biology":46,"accounting":68,"history":52},
{"id":129,"names":"Abner Ludwikiewicz","gender":"Male","maths":75,"english":43,"kiswahili":33,"chemistry":11,"biology":74,"accounting":59,"history":40},
{"id":130,"names":"Shannah Surman-Wells","gender":"Female","maths":46,"english":73,"kiswahili":22,"chemistry":37,"biology":46,"accounting":61,"history":77},
{"id":131,"names":"Melany Dubique","gender":"Female","maths":26,"english":59,"kiswahili":16,"chemistry":28,"biology":74,"accounting":85,"history":84},
{"id":132,"names":"Deva Wenden","gender":"Female","maths":30,"english":12,"kiswahili":59,"chemistry":26,"biology":75,"accounting":56,"history":68},
{"id":133,"names":"Othelia Gooch","gender":"Female","maths":30,"english":54,"kiswahili":50,"chemistry":68,"biology":33,"accounting":28,"history":32},
{"id":134,"names":"Johann Scurlock","gender":"Male","maths":32,"english":66,"kiswahili":24,"chemistry":32,"biology":75,"accounting":41,"history":40},
{"id":135,"names":"Yulma Bloss","gender":"Male","maths":14,"english":23,"kiswahili":15,"chemistry":57,"biology":31,"accounting":23,"history":70},
{"id":136,"names":"Nester Dysert","gender":"Male","maths":29,"english":74,"kiswahili":86,"chemistry":59,"biology":45,"accounting":36,"history":66},
{"id":137,"names":"Linnell Frears","gender":"Female","maths":39,"english":20,"kiswahili":58,"chemistry":21,"biology":66,"accounting":41,"history":17},
{"id":138,"names":"Ninette Minucci","gender":"Female","maths":23,"english":20,"kiswahili":18,"chemistry":27,"biology":48,"accounting":67,"history":33},
{"id":139,"names":"Ginny Ferrario","gender":"Female","maths":57,"english":82,"kiswahili":14,"chemistry":27,"biology":81,"accounting":32,"history":27},
{"id":140,"names":"Bonnee Dearl","gender":"Female","maths":23,"english":23,"kiswahili":40,"chemistry":52,"biology":43,"accounting":72,"history":50},
{"id":141,"names":"Sib Begbie","gender":"Female","maths":54,"english":48,"kiswahili":72,"chemistry":41,"biology":53,"accounting":90,"history":44},
{"id":142,"names":"Hilton Crewther","gender":"Male","maths":53,"english":71,"kiswahili":15,"chemistry":26,"biology":32,"accounting":80,"history":61},
{"id":143,"names":"Jennie Schimke","gender":"Female","maths":68,"english":15,"kiswahili":23,"chemistry":31,"biology":86,"accounting":25,"history":22},
{"id":144,"names":"Ann-marie Hackworthy","gender":"Female","maths":10,"english":13,"kiswahili":46,"chemistry":44,"biology":64,"accounting":57,"history":33},
{"id":145,"names":"Worthington Fawdry","gender":"Male","maths":63,"english":11,"kiswahili":24,"chemistry":46,"biology":38,"accounting":13,"history":21},
{"id":146,"names":"Quintilla Credland","gender":"Female","maths":10,"english":34,"kiswahili":65,"chemistry":16,"biology":79,"accounting":66,"history":76},
{"id":147,"names":"Fraze Littrik","gender":"Male","maths":84,"english":73,"kiswahili":84,"chemistry":65,"biology":47,"accounting":22,"history":31},
{"id":148,"names":"Rafa Knotte","gender":"Female","maths":78,"english":71,"kiswahili":80,"chemistry":59,"biology":10,"accounting":14,"history":41},
{"id":149,"names":"Thornton Roskell","gender":"Male","maths":17,"english":60,"kiswahili":77,"chemistry":24,"biology":73,"accounting":65,"history":85},
{"id":150,"names":"Jackelyn Barkworth","gender":"Female","maths":20,"english":70,"kiswahili":76,"chemistry":51,"biology":54,"accounting":41,"history":57},
{"id":151,"names":"Hannah Bringloe","gender":"Female","maths":59,"english":16,"kiswahili":19,"chemistry":52,"biology":77,"accounting":51,"history":15},
{"id":152,"names":"Hew McIlvenny","gender":"Male","maths":16,"english":12,"kiswahili":47,"chemistry":55,"biology":71,"accounting":70,"history":30},
{"id":153,"names":"Daniella Scard","gender":"Female","maths":16,"english":19,"kiswahili":47,"chemistry":51,"biology":49,"accounting":27,"history":41},
{"id":154,"names":"Vito Cranke","gender":"Male","maths":78,"english":81,"kiswahili":59,"chemistry":12,"biology":19,"accounting":88,"history":13},
{"id":155,"names":"Manny Horsewood","gender":"Male","maths":39,"english":45,"kiswahili":35,"chemistry":66,"biology":49,"accounting":36,"history":89},
{"id":156,"names":"Hunter Penticoot","gender":"Male","maths":77,"english":55,"kiswahili":30,"chemistry":13,"biology":60,"accounting":61,"history":77},
{"id":157,"names":"Wat Angrave","gender":"Male","maths":31,"english":54,"kiswahili":31,"chemistry":14,"biology":38,"accounting":57,"history":32},
{"id":158,"names":"Florina Freak","gender":"Female","maths":46,"english":23,"kiswahili":61,"chemistry":67,"biology":23,"accounting":28,"history":78},
{"id":159,"names":"Garvey Hakonsen","gender":"Male","maths":25,"english":65,"kiswahili":40,"chemistry":64,"biology":39,"accounting":38,"history":13},
{"id":160,"names":"Yancy Bursnoll","gender":"Male","maths":32,"english":23,"kiswahili":70,"chemistry":59,"biology":61,"accounting":77,"history":53},
{"id":161,"names":"Ursula Camilleri","gender":"Female","maths":78,"english":21,"kiswahili":21,"chemistry":26,"biology":24,"accounting":56,"history":48},
{"id":162,"names":"Emlen McComas","gender":"Male","maths":32,"english":57,"kiswahili":16,"chemistry":47,"biology":23,"accounting":44,"history":41},
{"id":163,"names":"Adela Janeway","gender":"Female","maths":59,"english":54,"kiswahili":76,"chemistry":59,"biology":53,"accounting":25,"history":28},
{"id":164,"names":"Gradeigh Cranmor","gender":"Male","maths":30,"english":35,"kiswahili":33,"chemistry":43,"biology":79,"accounting":58,"history":43},
{"id":165,"names":"Alana Shallcross","gender":"Female","maths":80,"english":76,"kiswahili":31,"chemistry":53,"biology":59,"accounting":20,"history":83},
{"id":166,"names":"Kincaid Jaggs","gender":"Male","maths":51,"english":15,"kiswahili":86,"chemistry":32,"biology":90,"accounting":54,"history":61},
{"id":167,"names":"Naoma Blakey","gender":"Female","maths":44,"english":43,"kiswahili":33,"chemistry":20,"biology":86,"accounting":29,"history":58},
{"id":168,"names":"Alejandro Lenoir","gender":"Male","maths":53,"english":63,"kiswahili":56,"chemistry":69,"biology":73,"accounting":64,"history":53},
{"id":169,"names":"Chantal O'Glassane","gender":"Female","maths":65,"english":31,"kiswahili":19,"chemistry":44,"biology":15,"accounting":40,"history":54},
{"id":170,"names":"Adolphe Padgett","gender":"Male","maths":81,"english":82,"kiswahili":14,"chemistry":37,"biology":18,"accounting":37,"history":86},
{"id":171,"names":"Oby Gwyer","gender":"Male","maths":30,"english":16,"kiswahili":75,"chemistry":10,"biology":79,"accounting":90,"history":62},
{"id":172,"names":"Marj Fillis","gender":"Female","maths":41,"english":60,"kiswahili":73,"chemistry":15,"biology":81,"accounting":12,"history":18},
{"id":173,"names":"Reinhard Searle","gender":"Male","maths":83,"english":44,"kiswahili":64,"chemistry":38,"biology":73,"accounting":22,"history":75},
{"id":174,"names":"Inesita Inkster","gender":"Female","maths":15,"english":52,"kiswahili":21,"chemistry":51,"biology":56,"accounting":13,"history":48},
{"id":175,"names":"Jane Tortoise","gender":"Female","maths":49,"english":75,"kiswahili":16,"chemistry":37,"biology":17,"accounting":26,"history":38},
{"id":176,"names":"Nana Konert","gender":"Female","maths":84,"english":20,"kiswahili":75,"chemistry":18,"biology":19,"accounting":13,"history":34},
{"id":177,"names":"Dickie Jahner","gender":"Male","maths":24,"english":18,"kiswahili":47,"chemistry":44,"biology":36,"accounting":45,"history":56},
{"id":178,"names":"Carce Stiling","gender":"Male","maths":58,"english":79,"kiswahili":64,"chemistry":23,"biology":46,"accounting":38,"history":35},
{"id":179,"names":"Marcela Cockshoot","gender":"Female","maths":49,"english":57,"kiswahili":78,"chemistry":12,"biology":75,"accounting":42,"history":47},
{"id":180,"names":"Cyndi Gazzard","gender":"Female","maths":72,"english":38,"kiswahili":66,"chemistry":16,"biology":13,"accounting":15,"history":88},
{"id":181,"names":"Aube Duffitt","gender":"Male","maths":59,"english":25,"kiswahili":49,"chemistry":59,"biology":32,"accounting":33,"history":10},
{"id":182,"names":"Papageno Derges","gender":"Male","maths":34,"english":77,"kiswahili":12,"chemistry":54,"biology":16,"accounting":79,"history":77},
{"id":183,"names":"Nomi Rait","gender":"Female","maths":59,"english":55,"kiswahili":49,"chemistry":64,"biology":19,"accounting":53,"history":51},
{"id":184,"names":"Brent Purrington","gender":"Male","maths":17,"english":59,"kiswahili":27,"chemistry":70,"biology":63,"accounting":79,"history":73},
{"id":185,"names":"Carlie Mucci","gender":"Female","maths":71,"english":13,"kiswahili":43,"chemistry":48,"biology":63,"accounting":19,"history":78},
{"id":186,"names":"Sanders Jagielski","gender":"Male","maths":32,"english":24,"kiswahili":72,"chemistry":52,"biology":41,"accounting":35,"history":32}]

male_stidents = filter(lambda student: student['gender'] == 'Male', students)

sorted_by_chem = sorted(male_stidents, key=lambda s: s['chemistry'], reverse=True)

print(sorted_by_chem[0:5])

ages = [8, 17, 16, 19, 80, 76, 34, 20]

def increment_age(age):
    return age + 1

news_ages = map(increment_age, ages)

news_ages_2 = map(lambda a: a+1, ages)

print(list(news_ages))


