tcp报文格式：
    格式：-16位源端口号 16位目的端口号- -32为序号- -32位确认序号- -标志位（确认字符）- -其他-
    源端口号：tcp连接中发起连接的主机端口号
    目的端口号：tcp连接着接受连接的主机端口号
    序号：用来表示数据的序号
    确认序号：用来确认报文的顺序
    标志位
        ack：若为1则表示这个数据段中的确认序号是有效的
        rst：当客户端向服务器的一个端口发送tcp连接时，服务器的该端口不允许建立连接，服务器就会回送一个tcp报文，将rst设为1，以告诉客户端该端口无法连接
        syn：若为1则表示这是一条建立tcp连接的报文段
        fin：若为1则表示这是一条断开tcp连接的报文段

三次握手
第一步：客户端的tcp程序向服务器的tcp程序发送一个syn标志位为1的tcp报文段，该报文段也被称为syn报文段，客户端的tcp程序随机选择一个序号作为该报文段的初始序号（假设为client_isn）,这报文段由传输层传递到网络层后被封装在一个ip数据包中发往服务器
第二步：服务器接受到该数据包后，服务器的网络层将syn数据抽取出来并交给传输层，同时该服务器为tcp连接分配资源，并向客户端发送允许连接的tcp报文段，这个报文段的syn位置也为1，同时它的ack位置也为1，表示它是刚刚客户端发送的那个syn报文段的确认报文，所以它也被称为synack报文段，服务器同样随机选择一个序号作为synack报文段的初始序号（假设为server_isn），同时将确认序号设置为client_isn+1
第三步：当客户端收到这synack报文段后，客户端给tcp连接分配资源，同时生成一个synack的报文，并将这个报文发给服务器，经过以上两步tcp连接建立了，所以这一次的报文的syn位置为0，ack的位置仍为1，同时序号被设置为client_isn+1，与上两条的报文不同的是，这一条报文可以携带数据了，如http请求就是在tcp第三次握手时发送给服务器的

四次挥手
第一步：客户端的进程发出断开指令，此时客户端的tcp程序创建一个tcp报文段，这个报文段的fin位置被设为1，表示这是一个断开连接的报文
第二步：服务器收到这条断开连接的报文向客户端回送这个报文的确认报文，将ack字段设置为1，告诉客户端它已经收到fin报文，并同意断开
第三步：服务器在发送完确认报文后，服务器的tcp程序自己也创建一个fin报文，fin字段设置为1，然后发给客户端
第四步：客户端在收到服务器的fin报文后回送一个服务器的fin报文的确认报文，以告诉服务器允许断开连接，服务器在收到客户端的这个确认报文后就释放tcp连接相关的资源，客户端在等待半分钟或几分钟后也释放tcp资源