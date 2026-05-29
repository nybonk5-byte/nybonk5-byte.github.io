const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question("数字を入力してください: ", (x) => {
if(x>5){
console.log("５以上です。")
}else{
    console.log("5以上出ないよ！")
}
readline.close
});