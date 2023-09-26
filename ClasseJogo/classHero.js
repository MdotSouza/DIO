class Hero {
    constructor(name, age, heroType) {
        this.name  = name; 
        this.age = age;
        this.heroType = heroType;
    }

    attack(){
        let attackType = "";
        switch (this.heroType) {
            case "mago":
                attackType = "magia";   
                break;
            case "guerreiro":
                attackType = "a espada";   
                break;
            case "monge":
                attackType = "artes marciais";   
                break;
            case "ninja":
                attackType =  "shuriken";   
                break;
        }
        return `O ${this.heroType} atacou usando ${attackType}`
    }
}

let magoMerlin = new Hero("Merlin",130,"mago")
let guerreiroArthur = new Hero("Arthur",15,"guerreiro")
let mongeShaolin = new Hero("Shaolin",30,"monge")
let ninjaDonatello = new Hero("Donatello",20,"ninja")

console.log(magoMerlin.attack())
console.log(guerreiroArthur.attack())
console.log(mongeShaolin.attack())
console.log(ninjaDonatello.attack())
