// 1.Направете for цикъл от 1 до n (включително) и задайте стъпка 3. Това означава, че при всяка итерация
//  на цикъла, променливата i ще увеличава стойността си с 3, вместо с 1:

function Nto1(input) {
    number = Number(input[0])
    for (let i = 1; i <= number; i+=3){
        console.log(i)
    }
}

// Nto1(["5"])