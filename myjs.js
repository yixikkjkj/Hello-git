function printHello() {
  document.getElementById("jshello").innerHTML = "js说你好";
  console.log("well,hello chrome");
  window.alert("我说你好！");
}

function numPlusstring() {
  var num = 1;
  var str = "zheshistr";
  console.log(num + str);
  return num + str;
}

function ArrayTry() {
  var cars = new Array();
  cars[0] = new Array();
  cars[0][1] = "wheel front";
  cars[0][2] = "wheel back";
  cars[1] = "engine";
  cars[2] = "coat";
  for (x in cars) {
    console.log(cars[x]);
  }
}

function FuncWithArg(attention, name) {
  console.log(
    attention + attention + attention + "And His Name is " + name + "!!"
  );
}

function SwitchVar(num) {
  switch (num) {
    case 10:
      //this is 10 now
      console.log("this issss1 100");
      break;
    case 12:
      //this is 12 now
      console.log("this is 121212");
      break;
    default:
      console.log("asdfasdfasdf");
      break;
  }
}

function Person(name, greeting) {
  this.name = name;
  this.greeting = function greeting() {
    console.log(greeting + "im" + this.name);
  };
}

function TestData() {
  data = [
    {
      num: 1598888888,
      time: Date()
    },
    {
      num: 222888888,
      time: Date()
    }
  ];
  InputTable(data);
}

function selectAll() {
  checklist = document.getElementsByName("rowinfo");
  for (idx in checklist) {
    checklist[idx].checked = !checklist[idx].checked;
  }
}

function DeleteSelected(index) {
  console.log("没有实现的删除方法");
}

function InputTable(data) {
  head = '<input type="checkbox" name="allcheckbox" onclick="selectAll()">';
  body = "<table>";
  for (info in data) {
    body += RowInfo(data[info]);
  }
  body += "</table>";
  console.log(head);
  document.getElementById("inputtable").innerHTML += head + body;
}

function RowInfo(info) {
  num = info["num"];
  time = info["time"];
  body =
    "<tr>" +
    "<td>" +
    '<input type="checkbox" name="rowinfo" value=' +
    num +
    ">" +
    "</td>" +
    "<td>" +
    num.toString() +
    "</td>" +
    "<td>" +
    time +
    "</td>" +
    "<td>" +
    '<button onclick="DeleteSelected()">删除</button>' +
    "</td>" +
    "</tr>";
  return body;
}

function constletvar() {
  const a = 1;
  let b = 1;
  var c = 1;
  console.log("asdfasdfasdf");
}

function test_for_select(e, v, d) {
  console.log("daolezheli");
  console.log(e);
  console.log(v);
  console.log(d);
}
