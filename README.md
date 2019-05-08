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
