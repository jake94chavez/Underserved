with open('/Users/jakechavez/development/Projects/Underserved/Underserved/sql-crap/steam_filters.csv') as f:
	reader = csv.reader(f, delimiter = ',')
	next(reader, None)
	for row in reader:
		_, created = Filter.objects.get_or_create(
			kind=row[0],
			name=row[1],
			label=row[2],
		)

with open('/Users/jakechavez/development/Projects/Underserved/Underserved/sql-crap/steam_index.csv') as f:
	reader = csv.reader(f, delimiter = ',')
	next(reader, None)
	for row in reader:
		_, created = Index.objects.get_or_create(
			kind=row[0],
			name=row[1],
			app_id=row[2],
		)

with open('/Users/jakechavez/development/Projects/Underserved/Underserved/sql-crap/steam_games.csv') as f:
	reader = csv.reader(f, delimiter = '<')
	next(reader, None)
	for row in reader:
		if row[2]=='':
			_, created = Game.objects.get_or_create(
			app_id=row[0],
			app_name=row[1],
			metascore=0,
		)
		else:
			_, created = Game.objects.get_or_create(
			app_id=row[0],
			app_name=row[1],
			metascore=row[2],
		)