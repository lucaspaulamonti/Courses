// Utilização de variáveis e constantes em escopo global e local.
const uRose = 8, uLily = 10, uTulip = 2;
let nRose = 70, nLily = 50, nTulip = 120;
function tCalc(){
    let tRose, tLily, tTulip, total;
    tRose = uRose * nRose;
    tLily = uLily * nLily;
    tTulip = uTulip * nTulip;
    total = tRose + tLily + tTulip;
    console.log(total)
}
tCalc()
nRose -= 20, nLily -= 30;
tCalc()