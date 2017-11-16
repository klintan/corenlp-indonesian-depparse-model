# clean conll files

with open('id-ud-train.conllu') as f: 
	content = f.readlines()

content = [x for x in content if not x.startswith('#')]

with open('indonesian-train.conllu', 'w') as p:
	p.write("".join(content))