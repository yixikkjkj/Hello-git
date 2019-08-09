import * as React from "react";

import { BEM } from "../../../common/util";
import { Icon } from "mz-react-components";

const styles = require("./index.scss");
const bem = BEM(styles, "promotion");

const click_href = {
  去群发: "/sms/create?create_type=order",
  订单催付: "/sms/notice?type=33",
  订单关怀: "/sms/notice?type=49",
  发货提醒: "/sms/notice?type=65",
  评价提醒: "/sms/notice?type=113",
  "群发记录/效果": "/sms/list",
  催付效果: "/sms/notice?type=33#page=stats_33"
};

const all_step_text = {
  1: [
    {
      time: "5.25-5.28",
      title: "预售",
      content: ["预售利益点通知，支付定金", "老客激活，收藏/加购提升"]
    },
    {
      time: "5.29-5.30",
      title: "预热",
      content: ["活动新品预告，优惠券发放", "618活动预告，利益点透出"]
    },
    {
      time: "5.31",
      title: "预热",
      no_multi_send: true,
      content: [
        "开启订单催付，提升下单转化",
        "开启付款关怀、发货提醒等，提升购物体验"
      ],
      href: [["订单催付"], ["付款关怀", "发货提醒"]]
    }
  ],
  2: [
    {
      time: "6.1-6.2",
      title: "开门红",
      content: ["预售尾款支付通知", "618第一波开门红活动通知"]
    },
    {
      time: "6.3-6.12",
      title: "品类日",
      content: ["618品类活动通知，突出利益点", "618品类活动倒计时"]
    },
    {
      time: "6.13-6.15",
      title: "狂欢预热",
      content: ["618狂欢活动利益点预告", "活动优惠券发放，提升加购/收藏"]
    },
    {
      time: "6.16-6.18",
      title: "狂欢日",
      content: ["第二件半价/前N件XX元活动通知", "618活动倒计时，最后冲刺"]
    }
  ],
  3: [
    {
      time: "6.19",
      title: "返场开始",
      content: ["返场活动通知，突出返场利益点", "图层开启评价提醒，提升DSR"],
      href: [[], ["评价提醒"]]
    },
    {
      time: "6.20",
      title: "返场结束",
      content: ["返场活动倒计时，最后冲量", "618结束客户关怀，表示感谢"]
    },
    {
      time: "6.21",
      title: "数据复盘",
      content: ["群发短信效果分析，群发记录/效果", "催付效果分析，催付效果"],
      href: [["群发记录/效果"], ["催付效果"]]
    }
  ]
};

const replaceHref = (msg, href_list) => {
  let result = [msg];
  for (const href_name of href_list) {
    let temp = [];
    for (const temp_str of result) {
      if (typeof temp_str !== "string") {
        temp.push(temp_str);
        continue;
      }
      let last_index = temp_str.lastIndexOf(href_name);
      if (last_index == -1) {
        temp.push(temp_str);
        continue;
      }
      temp.push(temp_str.slice(last_index + href_name.length, temp_str.length));
      temp.push(
        <a
          data-event-action={href_name}
          href={click_href[href_name]}
          key={href_name}
        >
          {href_name}
        </a>
      );
      temp.push(temp_str.slice(0, last_index));
    }
    result = temp;
  }
  result.reverse();
  return result;
};

export default class SmsPromoGuide extends React.PureComponent {
  constructor(props) {
    super(props);
    this.default_step = this.getStep(moment());
    this.state = { step: this.default_step };
  }

  getStep = now => {
    return 1;
    const m_525 = moment("2019-05-25");
    const m_601 = moment("2019-06-01");
    const m_619 = moment("2019-06-19");
    const m_621 = moment("2019-06-21");
    if (now.isBefore(m_525)) {
      return -1;
    } else if (now.isBefore(m_601)) {
      return 1;
    } else if (now.isBefore(m_619)) {
      return 2;
    } else if (now.isBefore(m_621)) {
      return 3;
    } else {
      return -1;
    }
  };

  renderTitle = (time, title) => {
    return (
      <div className={bem("verticalAlign")}>
        <div className={bem("title")}>
          <p>{time}</p>
          <p>{title}</p>
        </div>
      </div>
    );
  };

  renderContent = (content, href, is_active) => {
    return (
      <div className={bem("verticalAlign")}>
        <ul className={bem("content")}>
          {content.map((doc, idx) => {
            return (
              <li key={idx}>
                <span>
                  {is_active && href ? replaceHref(doc, href[idx]) : doc}
                </span>
              </li>
            );
          })}
        </ul>
      </div>
    );
  };

  renderStep = step => {
    let is_active = false;
    let block_css_name = "negativeBlock";
    if (step == this.state.step) {
      is_active = true;
      block_css_name = "activeBlock";
    }
    const step_text = all_step_text[step];
    return (
      <div
        onMouseEnter={() => {
          this.setState({ step });
        }}
        className={bem(block_css_name, step.toString())}
      >
        <div className={bem("actionContainer")}>
          {step_text.map((text, index) => {
            const content_block_css_name =
              text.no_multi_send && is_active
                ? "contentBlockNoMulti"
                : "contentBlock";
            return (
              <div
                key={index}
                className={bem("actionLine", step_text.length.toString())}
                data-ga-options={"actionPrefix: +" + text.title + "_"}
              >
                <div className={bem(block_css_name, "titleBlock")}>
                  {this.renderTitle(text.time, text.title)}
                </div>
                <div className={bem(block_css_name, content_block_css_name)}>
                  {this.renderContent(text.content, text.href, is_active)}
                </div>
                {!is_active || text.no_multi_send ? (
                  ""
                ) : (
                  <div className={bem("multiSendBlock")}>
                    <a data-event-action="去群发" href={click_href["去群发"]}>
                      去群发 <Icon name="xiayiye" />
                    </a>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  render() {
    if (this.state.step < 0) {
      return "";
    }

    return (
      <div
        data-ga-options="category: 短信工作台, actionPrefix: 618引导_"
        className={bem("")}
        onMouseLeave={() => {
          this.setState({ step: this.default_step });
        }}
      >
        {this.renderStep(1)}
        {this.renderStep(2)}
        {this.renderStep(3)}
      </div>
    );
  }
}
