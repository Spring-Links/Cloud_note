**准备工作**
- Python-3.12.1.tgz
- CentOS 8

**上传tgz文件并解压**
`tar -zxf /export/softwares/Python-3.12.1.tgz -C /opt/python-3.12`

**安装依赖库**
```
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel wget make
# sudo dnf install -y gcc openssl-devel bzip2-devel libffi-devel wget make --allowerasing
```

**运行可执行文件并编译**
```
-- 进入../Python-3.12.1中运行可执行文件configure
./configure --enable-optimizations

-- 编译安装
make -j $(nproc)
sudo make altinstall

-- 验证
python3.12 --version
```