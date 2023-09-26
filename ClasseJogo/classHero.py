class Hero():
    def __init__ (self, name, age, heroType): 
        self.name  = name 
        self.age = age
        self.heroType = heroType

    def attack(self):
        attackType = ""
        if self.heroType == "mago":
            attackType = "magia"   
        elif self.heroType == "guerreiro":
            attackType = "a espada"   
        elif self.heroType == "monge":
            attackType = "artes marciais"   
        elif self.heroType =="ninja":
            attackType =  "shuriken"
            
        return f"O {self.heroType} atacou usando {attackType}"
    
magoMerlin = Hero("Merlin",130,"mago")
guerreiroArthur = Hero("Arthur",15,"guerreiro")
mongeShaolin = Hero("Shaolin",30,"monge")
ninjaDonatello = Hero("Donatello",20,"ninja")

print(magoMerlin.attack())
print(guerreiroArthur.attack())
print(mongeShaolin.attack())
print(ninjaDonatello.attack())
