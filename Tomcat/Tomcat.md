**Tomcat：** 相较于nginx来说tomcat更适合处理动态内容，它内置了一个http

**静态资源**
- html
- css
- jpg

**动态资源：** 动态资源被访问后需要先转为静态资源在返回给浏览器
- jsp
- asp
- php
- servlet

**网络通信的三要素**
- 传输协议协议：固定数据传输的规则
- ip：电子设备在网络中的唯一标识
- 端口号：0~65536

**server.xml**
```
<!-- 用于创建server实例 -->
<Server port="8005" shutdown="SHUTDOWN">
  <!-- 以日志形式输出服务器、操作系统、JVM版本信息 -->
  <Listener className="org.apache.catalina.startup.VersionLoggerListener" />
  <!-- 加载和销毁APR库，找不到该库会输出日志，不影响tomcat的启动 -->
  <Listener className="org.apache.catalina.core.AprLifecycleListener" />
  <!-- 避免jre内存泄漏 -->
  <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener" />
  <!-- 用户加载和销毁全局命名服务 -->
  <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener" />
  <!-- 在Context停止时重建Executor池中的线程，避免ThreadLocal相关的内存泄漏 -->
  <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener" />

  <!-- 全局命名服务 -->
  <GlobalNamingResources>
    <Resource name="UserDatabase" auth="Container"
              type="org.apache.catalina.UserDatabase"
              description="User database that can be updated and saved"
              factory="org.apache.catalina.users.MemoryUserDatabaseFactory"
              pathname="conf/tomcat-users.xml" />
  </GlobalNamingResources>

  <!-- 创建service实例 -->
  <Service name="Catalina">
    <Connector port="8080" protocol="HTTP/1.1"
               <!-- connector接收链接后的等待超时事件，单位毫秒 -->
               connectionTimeout="20000"
               <!-- 当接收到https协议的请求后将请求重定向到8443端口 -->
               redirectPort="8443"
               maxParameterCount="1000"
               />

    <!-- defaultHost:默认使用的主机名称 -->
    <Engine name="Catalina" defaultHost="localhost">

      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <!-- This Realm uses the UserDatabase configured in the global JNDI
             resources under the key "UserDatabase".  Any edits
             that are performed against this UserDatabase are immediately
             available for use by the Realm.  -->
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm"
               resourceName="UserDatabase"/>
      </Realm>

      <!-- unpackWARs：是否自动解压war包，false将会直接从war包启动而不解压
      autoDeploy：控制tomcat是否在运行时定期检测并自动部署新增或者变更的web应用 -->
      <Host name="localhost"  appBase="webapps"
            unpackWARs="true" autoDeploy="true">

        <!-- war包部署的路径 
          path：web应用的context路径
        -->
        <Context docBase="myApp" path="/myApp">
        </Context>

        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
                 prefix="localhost_access_log" suffix=".txt"
                 pattern="%h %l %u %t &quot;%r&quot; %s %b" />

      </Host>
    </Engine>
  </Service>
</Server>



<Executor name="tomcatThreadPool" 
          namePrefix="catalina-exec-"
          maxThreads="150" 
          minSpareThreads="4"/>








```



**tomcat-users.xml**