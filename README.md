# Hello-git

## git pull 和 push

git pull <远程主机名> <远程分支名>:<本地分支名>

1. 冒号后面的本地分支名，如果是当前分支，则可以省略

git push <远程主机名> <本地分支名>:<远程分支名>

1. 如果仅省略远程分支名，则认为远程分支名和本地分支名相同，或者默认为 master
2. 如果仅省略本地分支名，则表示删除远程分支，表示为推一个空的分支上去
3. 如果省略了本地和远程分支名，则认为当前本地分支推送到远端同样名字的分支

## 追踪关系

1. git clone 时，对远程和本地同名的分支建立追踪关系
2. 手动通过设置 upstream 去建立追踪关系

## git reset 的问题

1. 当你不小心 push 了一个错误的提交，这个错误包括但不限于

   - 写错了代码，就是需要 reset 回来
   - 应该写在前一个 commit 中，但是却独立了另一个 commit

2. 这时候如果你 reset 了上一个版本的代码，本地的修改不会消失的，为了能把远端的提交也干掉，这时候你需要：

   - 手动把所有的代码都还原成上一个版本的状态，即对应上一个版本无修改
   - git stash 暂存这个修改，这时也是对应上个版本无修改的状态

3) 然后强行刷掉远端的提交，即 git push <远端主机名> <本地分支名>:<远端分支名> --force
4) 这时候 tig 再去查看的时候，远端已经是前一个版本的状态了
5) 这时候再去搞新的提交吧

## git branch 合并问题

我们假定分支 A 需要合并到分支 B，合并可能遇到的问题是如果直接合并会导致 A 和 B 冲突，因此采取这样的策略

1. 先将 B 分支的代码合并或重演到 A 分支上 git pull origin B --rebase 或者 git pull origin B --merge
2. 此时冲突了，那我们解决冲突
3. 然后将冲突的文件 git add
4. 因为冲突，重演或者合并暂停了，既然解决了冲突，那我们继续 git rebase --continue 或者 git merge --continue
5. 全都解决完成之后我们就可以提交了
6. 然后进行合并，在分支 B 上执行 git merge A
7. 执行完成之后再提交，就把 A 的内容合并到 B 了，并且同步到了远端的 B 分支
8. 可能需要删除远端的 A 分支，可以使用 git push origin --delete A 来删除远端的 A 分支
9. 可能本地的 A 分支也不要了，用 git branch -d A 就可以了

# 凯恩斯主义

## 以前是怎么做的

1. 理想情况下，资本家付给雇员的工资应当被消费掉，即收入=支出
2. 雇员的生产能力足够强，创造的价值>收入，此时市场就会供大于求，于是降价，于是雇员的收入有结余
3. 结余的钱可以拿去做投资，这样依然能够保证收入=支出

## 出现了什么问题

1. 投资是不能一直投的，因为存在投资边际递减效应，当投资的收益还不如银行利率高的时候，那就不如不投资了
2. 为了继续投资，那可以把银行利率降低，就能使投资的量更多了，如果降到 0，那可以让所有钱都拿去投资。
3. 但是利率不能降到 0，因为如果降到 0 了，人们就会因为菜单成本和流动性陷阱，不如把钱放在家里


        天
      泽  风
    火      水
      雷  山
        地


模版：
时间：
表现：同样的也是三次请求，按顺序是通过、通过、拒绝，日志显示第二次和第三次请求间隔不到 100 毫秒

模版：5e376f9765b69f100559a03d
时间：2020-02-03 08:55:51 -> 200-02-03 08:58:15
表现：有三次审核请求，按顺序是通过、拒绝、通过，第一次和第二次的请求间隔很短

现在钉钉自动审核模版的表现是依次点了通过和拒绝，后面发现有这样情况的，可以让客服同学修改一下

## celery==4.4.0 和 redbeat==0.13.0 的问题

redbeat 在保存 task 执行时间到 redis 后，一直认为是 utc 时间，取出来的时候直接给加上了 utc 时区，redbeat 这样做是因为 celery.ScheduleEntry 使用了 utc 时间，并且还写了一句注释

> celery.ScheduleEntry sets last_run_at = utcnow(), which is confusing and wrong

celery 4.4.0 以前的版本没有校验 redbeat 取出来的时间和 celery 当前时间的时区不同，一直都相安无事，4.4.0 的时候给加上了，改动日志上说明是希望解决一个 bug（但是带来了新的 bug），这样校验之后 redbeat 总是得到 8 小时之后的时间，因此才会只有 beat: Waking up in 5.00 minutes 这样的 log

我觉得暂时还是先不要升级了


【美折到期提醒】
【美折】邓瑞大傻逼：您的美折订购即将到期，点击链接续订 tb.cn/4puZKPw 回T退订
含有敏感危险词，发送失败

{'app_id': '2018041202546849', 'method': 'alipay.trade.create', 'charset': 'utf-8', 'sign_type': 'RSA2', 'timestamp': '2020-02-11 12:54:45', 'version': '1.0', 'biz_content': '{"out_trade_no":"2020021112544557799","total_amount":50.0,"subject":"mini program recharge960(taovip)","timeout_express":"30m"}', 'notify_url': 'https://sms.meideng.net/hooks/alipay/recharge/750918ff7cafa3f747eca334bfdee1e3', 'sign': 'sWITBNvPfpIz7Ze4vfLjW9j6zuMYHjXUCbT82mAU1EgsJSD6dRdOVQ1+yPD4UlH2ozv/Cgwc0jsGD/2wVkm80U0GsX60PPeciraJs2itSoixrhTJWjZH1TtR8iWtJd1scse7dBtWCIYYOlpRoX4VzJjASD3JoUCVyohuo3z1Cxgiq7312CMfEkvIorAEQaggijsHB4yh3S1WHgnxTmZC2IdpRy0k/CKW+flWJTC5/3DINyHlTxlU1OhivxEHHgLAbFgYvmA6a77N+2LLl9ueYb+mXTzyg4F7rgixoOqRIHT3U+rMaVkC6OvP81xA2THa/0SINsfC7K9FV3plUPHgmA=='}

国家：我们新发布了外国人永久居留草案，另外这两天我们要清网
我们：为什么我看的论坛/我的账号又封了？
国家：我就知道大家对草案没有什么问题

我一开始总觉得，我挺自由的，我也认为自由就是我重要的追求，但是不知道什么时候，突然就像这样，钢筋穿胸而过，钉在原地，一点都动不了。现在想想，背上的重量确实很重，钢筋插着我也很疼，长久以来我也因为不自由而颓丧。但如果我的不自由能够保护你，避免这样的重量压到你身上，那我就不亏——你是更重要的追求。来，帮我拍张照片吧，我没有很多的时间了。
