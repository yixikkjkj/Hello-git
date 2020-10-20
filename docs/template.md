# 模版发送接口

## 接口信息

此接口用于以一个已申请并审核过的模版进行发送，发送时不再需要审核，相较于单条发送接口更快

## 请求信息

URL: https://www.meixinduanxin.com/api/sender/template_batch_send

访问方式: POST

HTTP 协议: HTTPS

编码格式: UTF-8

## 请求参数

| 参数名称 | 类型 | 必传 | 描述 | 示例 |
| ------- | ----- | -------- | ---- | ---- |
| api_key | 字符串 | 是 | 子账户的唯一标识 | '5daedb8d061173241101e734' |
| mobiles | 字符串 | 是 | 带发送号码，多个号码用```,```分割，最多 1000 个号码 | '137578111234,137578111235' |
| template_id | 字符串 | 是 | 模版的唯一标识的ID，目前可在web端上管理用户的模版： https://www.meixinduanxin.com/c/template | '5dbbc5879344f5ca7429dea3' |
| params | JSON字符串 | 是 | 模版参数字符串，json 对象的字符串，模版中参数为 key，待发送的值为 value | '{"code": 123456}' |
| ts | 整型 | 是 | 当前时间戳，单位：秒 | 1572836853 |
| sign | 字符串 | 是 | 校验字符串，利用请求参数生成的 md5 值，生成规则请查看 https://www.meixinduanxin.com/doc/request | 145658932393484 |

## 返回参数

| 参数名称 | 类型 | 描述 | 示例 |
| -------- | ---- | -------- | ---- |
| code | 整型 | 请求状态，code 为 0 表示成功 | 0 |
| accepted | 整型 | 接收的短信数量 | 999 |
| skipped | 整型 | 被拒绝的短信数量 | 1 |
| details | 数组 | 发送的详情，每一条短信发送情况的列表。单条短信详情包含的字段：mobile 手机号，sid 单个短信记录唯一标识，detail_code 单个短信记录发送情况，为 0 表示正常发送，detail_msg 异常信息的解释 |  |
| msg | 字符串 | 请求出错的信息，对 code 不为 0 时的解释信息 |  |

### 返回示例

```json
{
  'code': 0,
  'accepted': 1,
  'skipped': 0,
  'details': [{
    'mobile': '137578111234',
    'sid': '5dae6bdd1ffef59e70d1f08a',
    'detail_code': 0,
    'detail_msg': ''
  }],
  'msg': '',
}

```

## 代码示例

### Python 版本

```python
import hashlib
import json
import time

import requests

def gen_sign(data):
    v = '|'.join(["{}={}".format(k, v) for k, v in sorted(data.items())])
    str_to_sign = "{}_{}".format(v, SECRET_KEY)  # 子账号的 secret_key
    sign = hashlib.md5(str_to_sign.encode()).hexdigest()
    return sign


def batch_send_by_template(mobiles, template_id, params):
    """
        mobiles: 手机号码列表，如 ['15972096311', '15972096312']
        template_id: 模版id，如 '5dbfbc9c940bb98484125783'
        params: 模版参数，如 {'code': 123456}
    """
    data = {
        'api_key': API_KEY,  # 子账号的 api_key
        'template_id': template_id,
        'mobiles': ','.join(mobiles),
        'params': json.dumps(params),
    }
    data['ts'] = int(time.time())
    data['sign'] = gen_sign(data)
    rlt = requests.post('https://www.meixinduanxin.com/api/sender/template_batch_send', json=data)
    handle_send_result(rlt)
```

### Java 版本

```java
public class template {

  public static String genSign(TreeMap<String, Object> d) throws Exception {
    String rawStr = "";
    boolean isFirst = true;
    for (Map.Entry<String, Object> entry : d.entrySet()) {
      if (!isFirst) {
        rawStr += '|';
      }
      rawStr += entry.getKey().toString() + '=' + entry.getValue().toString();
      isFirst = false;
    }
    rawStr += "_" + SECRET_KEY;  // 子账号的 secret_key
    System.out.println(rawStr);

    StringBuffer res = new StringBuffer();
    MessageDigest md5 = MessageDigest.getInstance("md5");
    md5.update(rawStr.getBytes());
    for (byte temp : md5.digest()) {
      res.append(String.format("%02x", temp));
    }
    return res.toString();
  }

  public static void batchSendByTemplate(ArrayList<String> mobiles, String templateId, TreeMap<String, Object> params)
      throws Exception {
    /*
      @param mobiles 手机号码列表，如 ['15972096311', '15972096312']
      @param template_id: 模版id，如 '5dbfbc9c940bb98484125783'
      @param params: 模版参数，如 {'code': 123456}
    */
    TreeMap<String, Object> data = new TreeMap<String, Object>();
    data.put("api_key", API_KEY);  // 子账号的 api_key
    data.put("template_id", templateId);
    data.put("mobiles", String.join(",", mobiles));
    data.put("params", new Gson().toJson(params));
    data.put("ts", System.currentTimeMillis() / 1000);
    data.put("sign", genSign(data));

    // 将 Map 数据转化为 json 数据
    Gson gson = new Gson();
    String jsonStr = gson.toJson(data);
    // 发出 post 请求
    sendPost("https://www.meixinduanxin.com/api/sender/template_batch_send", jsonStr);
  }
}
```
