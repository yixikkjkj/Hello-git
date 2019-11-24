import java.security.MessageDigest;
import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;
import com.google.gson.Gson;

public class template {

  public static String API_KEY="5daeb6100d21bd6215da5e7d";  // 子账号的 api_key
  public static String SECRET_KEY = "PGG1sdgUCb";  // 子账号的 secret_key
  public static String POST_URL = "https://www.meixinduanxin.com";

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
    rawStr += "_" + SECRET_KEY; // 子账号的 secret_key
    System.out.println(rawStr);

    StringBuffer res = new StringBuffer();
    MessageDigest md5 = MessageDigest.getInstance("md5");
    md5.update(rawStr.getBytes());
    for (byte temp : md5.digest()) {
      res.append(String.format("%02x", temp));
    }
    return res.toString();
  }

  public static TreeMap<String, Object> batchSendByTemplate(ArrayList<String> mobiles, String templateId, TreeMap<String, Object> params)
      throws Exception {
    /*
      @param mobiles 手机号码列表，如 ['15972096311', '15972096312']
      @param template_id: 模版id，如 '5dbfbc9c940bb98484125783'
      @param params: 模版参数，如 {'code': 123456}
    */
    TreeMap<String, Object> data = new TreeMap<String, Object>();
    data.put("api_key", API_KEY);
    data.put("template_id", templateId);
    data.put("mobiles", String.join(",", mobiles));
    data.put("params", new Gson().toJson(params));
    data.put("ts", System.currentTimeMillis() / 1000);
    data.put("sign", genSign(data));
    post("https://www.meixinduanxin.com/api/sender/template_batch_send", data);
  }

  public static void main(String[] args) throws Exception {
    int a = 1;
    String b = "1";
    String c = a + b;
    System.out.println(c);
  }
}

