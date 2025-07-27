查看git版本 git -v
配置用户名及邮箱
git config --global user.name "username"
git config --global user.emali email_adress
保存配置信息 git config --global credential.helper store
查看配置信息 git config --global --list
创建仓库 git init
克隆仓库 git clone repo_url
查看仓库状态 git status
添加到暂存区 git add
提交到仓库 git commit -m 'message'
将当前目录全部添加至暂存区：git add .
查看提交信息：git log
查看简洁的提交信息：git log --oneline
回退版本 git reset mixed
- **--soft：** 回退到某一个版本，保留工作区、暂存区的修改内容
- **--hard：** 回退到某一个版本，丢弃工作区、暂存区的修改内容
- **--mixed：** 回退到某一个版本，保留工作区，丢弃暂存区的修改内容（默认参数）

查看操作的历史记录：git reflog
查看版本之间的差异：git diff
git diff --cache
git diff HEAD
git diff version01_id version02_id
git dirr HEAD HEAD~ （HEAD~：上一个版本）
查看暂存区的内容：git ls-files
删除工作区的文件：git rm file_name

工作区（Working Directory）
暂存区（Staging Area/Index）
本地仓库（Local Repository）

