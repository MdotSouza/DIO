function calcRank(win,loss){
    let balance = win - loss;
    let level = "";
    
    if (balance <= 10){
        level = "Ferro";
    } else if (balance < 21){
        level = "Bronze";  
    } else if (balance < 51){
        level = "Prata";  
    } else if (balance < 81){
        level = "Ouro";  
    } else if (balance < 91){
        level = "Diamante";  
    } else if (balance <= 100){
        level = "Lendário";  
    } else {
        level = "Imortal";  
    }
    return `O Herói tem de saldo de ${balance} está no nível de ${level}!`
}

console.log(calcRank(100,101));
console.log(calcRank(100,100));
console.log(calcRank(107,100));
console.log(calcRank(120,100));
console.log(calcRank(150,100));
console.log(calcRank(180,100));
console.log(calcRank(190,100));
console.log(calcRank(200,100));
console.log(calcRank(111,10));