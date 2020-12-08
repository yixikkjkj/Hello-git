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

function draw_canvas() {
  var ca = document.getElementById('huabu');
  var ctx = ca.getContext('2d');
  ctx.fillRect(10, 10, 50, 50);
}


function send_request() {
  var formData = new FormData();
  formData.append('File', $('#file_input')[0].files[0], '签名自有证明.docx');
  formData.append('StoreFile', 'true');
  console.log($('#file_input')[0].files[0]);
  // $.ajax({
  //   url: 'https://team02.hackathon.ebincr.com/convert/docx/to/pdf?Secret=Y2qbHnYrTZj1aX8t',
  //   data: formData,
  //   processData: false,
  //   contentType: false,
  //   method: 'POST',
  //   success: function (data) {
  //     console.log(data);
  //   }
  // });
}

function upload_file() {
  $('#file_input').click();
}


// curl -i -X POST -d '{"apikey": "f23cfb0cb34a42ed8b9ab82bc4feba17","file": "a.docx", "filename":"a.docx", "outputformat":"pdf", "input": "raw"}' http://api.convertio.co/convert

// curl -i -X GET http://api.convertio.co/convert/afd58454e0731b0f2cdac3723b966647/dl
// curl -i -X POST -d '{"apikey": "f23cfb0cb34a42ed8b9ab82bc4feba17", "outputformat":"pdf", "input": "upload"}' http://api.convertio.co/convert

// 328d6b2a4078990366dfcc1210b4e94a

// curl -i -X PUT -d '{"step":"convert", "input": "upload"}' http://api.convertio.co/convert/328d6b2a4078990366dfcc1210b4e94a/a


  // var formData = new FormData();
  // formData.append('File', $('#file_input')[0].files[0], '签名自由证明.docx');
  // console.log($('#file_input')[0].files[0]);
  // var reader = new FileReader();
  // reader.readAsDataURL($('#file_input')[0].files[0]);
  // reader.onload = function (event) {
  //   console.log(this.result);
  //   console.log(this.result.indexOf(','));
  //   $.ajax({
  //     url: 'https://api.convertio.co/convert',
  //     data: {
  //       apikey: 'f23cfb0cb34a42ed8b9ab82bc4feba17',
  //       input: 'upload',
  //       outputformat: 'pdf',
  //     },
  //     method: 'POST',
  //     success: function (data) {
  //       console.log('succcccc');
  //       console.log(data);
  //       $.ajax({
  //         url: 'https://api.convertio.co/convert/' + data.id + '/' + $('#file_input')[0].files[0].name,
  //         data: $('#file_input')[0].files[0],
  //         method: 'PUT',
  //         success: function (data) {
  //           console.log('succccc');
  //           console.log(data);
  //         },
  //         error: function (data) {
  //           console.log('errrrorr');
  //           console.log(data);
  //         },
  //       });
  //     },
  //     error: function (data) {
  //       console.log('errrrorr');
  //       console.log(data);
  //     },
  //   });
  // }


function sumByType(array) {
  const temp = array.reduce((prev, curr) => {
    var now_val = prev[curr.type] ? prev[curr.type] : 0;
    prev[curr.type] = now_val + curr.value;
    return prev;
  }, Object.create(null));

  var rlt = [];
  for (const key in temp) {
    rlt.push({ type: key, value: temp[key] });
  }
  return rlt;
}

function resetSendGuide() {
  [0, 1, 2, 3].map(function (index) {
    [0, 1, 2, 3, 4].map(function (content_index) {
      $.ajax({
        url: '/common/sms/act/send_guide/set',
        type: "POST",
        data: {key: `act_${index}_${content_index}`, act_id: ''},
        dataType: "json",
        success: function (res) {
          if (res.success) {
            console.log('重置成功');
          } else {
            console.log('重置失败');
          }
        },
        error: function () {
          console.log("重置出错");
        }
      });
    });
  });
}

resetSendGuide()
