#0-name
#1-element
#2-stage
#3-evolution index
#4- hp
#5- attack
#6- defense
#7- evolve Conditions


def setPokemonData():#some sample pokemons for testing
	#pokemon=type,stage,next pokemon to evolve into
	pokemons = dict()
	pokemons[1] = ("Bulbasaur", "grass",1,2,45,57,57,16)
	pokemons[2] = ("Ivysaur","grass",2,3,60,71,72,32)
	pokemons[3] = ("Venasaur","grass",3,None,80,91,92,None)
	pokemons[4] = ("Charmander","fire",1,5,39,56,47,16)
	pokemons[5] = ("Charmeleon","fire",2,6,58,72,62,36)
	pokemons[6] = ("Charizard",'fire',3,None,78,97,82,None)
	pokemons[7] = ("Squirtle","water",1,8,44,49,65,16)
	pokemons[8] = ("Watortle","water",2,9,59,64,80,36)
	pokemons[9] = ("Blastoise","water",3,None,79,84,103,None)
	pokemons[10] = ("Caterpie","bug",1,11,45,25,28,7)
	pokemons[11] = ("Metapod", "bug",2, 12,50,23,40,10)
	pokemons[12] = ("Butterfree","bug",3,None,60,68,65,None)
	pokemons[16] = ("Pidgey","flying",1,17,40,40,37,18)
	pokemons[17] = ("Pidgeotto","flying",2,18,63,55,53,36)
	pokemons[18] = ("Pidgeot","flying",3 ,None,83,75,73,None)
	pokemons[19] = ("Rattata", "normal",1,20,30,41,35,20)
	pokemons[20] = ("Raticate", "normal", 2 , None,55,66,65,None)
	pokemons[25] = ("Pikachu","electric",2,26,35,53,45,"Thunder Stone")
	pokemons[26]= ("Raichu","electric",3,None,60,90,68,None)
	pokemons[29] = ("Nidoran", "poison",1, 30,55,44,46,16)
	pokemons[30] = ("Nidorina", "poison",2,31,70,59,61,"Moon Stone")
	pokemons[31] = ("Nidoqueen","poison",3,None,90,84,86,None)
	pokemons[37] = ("Vulpix","fire",1,38,38,46,53,"Fire Stone")
	pokemons[38] = ("Ninetales","fire",3,None,73,79,88,None)
	pokemons[60] = ("Poliwag","water",1,61,40,45,45,25)
	pokemons[61] = ("Poliwhirl", "water",2,62,65,58,58,"Water Stone")
	pokemons[62] = ("Poliwrath", "water",3,None,90,83,93, None)
	pokemons[81] = ("Magnemite","electric",1,82,25,65,63,30)
	pokemons[82] = ("Magneton","electric",2, None,50,90,83,None)
	pokemons[92] = ("Gastly","ghost",1,93,30,68,33,25)
	pokemons[93] = ("Haunter","ghost",2,94,45,83,50,"Trade")
	pokemons[94] = ("Gengar","ghost",3,None,60,98,68,None)
	pokemons[129] = ("Magikarp","water",1,130,20,13,38,20)
	pokemons[130] = ("Gyarados", "water",2,None,95,93,90,None)
	pokemons[132] = ("Ditto","normal",1,None,48,48,48,None)
	pokemons[147] = ("Dratini","dragon",1,148,41,57,48,30)
	pokemons[148] = ("Dragonair",'dragon',2,149,61,77,68,55)
	pokemons[149] = ("Dragonite", 'dragon',3,None,91,117,98,None)
	return pokemons
#0 = description of item
#1 = type of item
#2 = price of item
def itemsData():
	items = dict()
	items["Thunder Stone"] = ("""\
A peculiar stone that makes certain species of Pokemon evolve. 
It has a thunderbolt pattern.""","evolution",
	2100)
	items["Fire Stone"] = ("""\
A peculiar stone that makes certain species of Pokemon evolve. 
It is colored orange.""","evolution",
	2100)
	items["Water Stone"] =("""\
A peculiar stone that makes certain species of Pokemon evolve. 
It is a clear, light blue.""","evolution",
	2100)
	items["Moon Stone"] =("""\
A peculiar stone that makes certain species of Pokemon evolve. 
It is as black as the night sky.""","evolution",
	2100)
	items["Rare Candy"] =("""\
A candy that is packed with energy. 
It raises the level of a Pokemon by one.""","consume",4000)
	items["Trade"] = ("""\
Allows evolution of Pokemon that evolve via trading""","evolution",2100)
	items["Pokeball"] = ("""\
A ball thrown to catch a wild Pokemon. 
It is designed in a capsule style.""","pokeball",200)
	items["Protein"] = ("""\
A nutritious drink for Pokemon. 
It raises the base Attack stat of one Pokemon.""","consume",9800)
	return items

# d[element] = 2dlist:not very effective,super effective,no effect
def elementsChart():
	d = dict()
	d["fire"] = [["fire","water","rock","dragon"],
		["grass","ice","bug","steel"],None]
	d["normal"] = [["rock","steel"],None,["ghost"]]
	d["water"] = [['water','grass','dragon'],['fire','ground','rock'],None]
	d['electric'] = [['electric','grass','dragon'],['water','flying'],
		['ground']]
	d['grass']=[['fire','grass','poison','flying','bug','dragon','steel'],
		['water','ground','rock'],None]
	d['poison']=[['poison','ground','rock','ghost'],['grass'],['steel']]
	d['flying']=[['electric','rock','steel'],['grass','fighting','bug'],None]
	d['bug']=[['fire','fighting','poison','flying','ghost','steel'],
		['grass','dark','psychic'],None]
	d['ghost']=[['dark'],['psychic','ghost'],['normal']]
	d['dragon']=[['steel'],['dragon'],None]
	return d