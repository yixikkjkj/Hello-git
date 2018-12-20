function printHello() {
  document.getElementById("jshello").innerHTML = "js说你好"
  console.log("well,hello chrome")
  window.alert("我说你好！")
}

function numPlusstring() {
  var num = 1
  var str = "zheshistr"
  console.log(num + str)
  return num + str
}

function ArrayTry() {
  var cars = new Array()
  cars[0] = new Array()
  cars[0][1] = "wheel front"
  cars[0][2] = "wheel back"
  cars[1] = "engine"
  cars[2] = "coat"
  for (x in cars) {
    console.log(cars[x])
  }
}

function FuncWithArg(attention, name) {
  console.log(attention + attention + attention + "And His Name is " + name + "!!")
}

function SwitchVar(num) {
  switch (num) {
    case 10:
      //this is 10 now
      console.log("this issss1 100")
      break
    case 12:
      //this is 12 now
      console.log("this is 121212")
      break
    default:
      console.log("asdfasdfasdf")
      break
  }
}

function Person(name, greeting) {
  this.name = name
  this.greeting = function greeting() {
    console.log(greeting + "im" + this.name)
  }
}
