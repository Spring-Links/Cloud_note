准备工作：Python-3.12.1.tgz
    将文件上传至提前创建的software中进行解压，将解压后的文件移动至../server中
安装依赖库
    sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel wget make
进入../server/Python-3.12.1中
运行可执行文件configure
    ./configure --enable-optimizations
编译安装
    make -j $(nproc)
    sudo make altinstall
验证
    python3.12 --version