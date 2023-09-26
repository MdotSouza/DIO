function levelHero(name,xp){
    let level = "";
    
    if (xp <= 1000){
        level = "Ferro";
    } else if (xp < 2000){
        level = "Bronze";  
    } else if (xp < 5000){
        level = "Prata";  
    } else if (xp < 7000){
        level = "Ouro";  
    } else if (xp < 8000){
        level = "Platina";  
    } else if (xp < 9000){
        level = "Ascendente";
    } else if (xp <= 10000){
        level = "Imortal";  
    } else {
        level = "Radiante";  
    }
    return `O Herói de nome ${name} está no nível de ${level}!`;
}

const testes = [900,2100,3500,6000,7500,8300,9200,10000,10020];

let cont = 1;
for (xpTeste of testes){
    let nameHero = `Hero${cont}`;
    console.log(levelHero(nameHero,xpTeste));
    cont++;   
}
