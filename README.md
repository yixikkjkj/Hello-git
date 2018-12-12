# Hello-git
git pull <远程主机名> <远程分支名>:<本地分支名>
	
1. 冒号后面的本地分支名，如果是当前分支，则可以省略

git push <远程主机名> <本地分支名>:<远程分支名>
	
1. 如果仅省略远程分支名，则认为远程分支名和本地分支名相同，或者默认为master
2. 如果仅省略本地分支名，则表示删除远程分支，表示为推一个空的分支上去
3. 如果
	
追踪关系

1. git clone时，对远程和本地同名的分支建立追踪关系
2. 手动通过设置upstream去建立追踪关系
	
git reset 的问题

1. 当你不小心push了一个错误的提交，这个错误包括但不限于

	- 写错了代码，就是需要reset回来
	- 应该写在前一个commit中，但是却独立了另一个commit

2. 这时候如果你reset了上一个版本的代码，本地的修改不会消失的，为了能把远端的提交也干掉，这时候你需要：

	- 手动把所有的代码都还原成上一个版本的状态，即对应上一个版本无修改
	- git stash 暂存这个修改，这时也是对应上个版本无修改的状态


3. 然后强行刷掉远端的提交，即 git push <远端主机名> <本地分支名>:<远端分支名> --force
4. 这时候tig再去查看的时候，远端已经是前一个版本的状态了
5. 这时候再去搞新的提交吧