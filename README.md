<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-arcaeabot

_✨ Arcaea查分插件 ✨_
</div>


## 功能 Resume

Arcaea 查分器。

使用 /arc help查看帮助信息

[更新日志](https://github.com/SEAFHMC/nonebot-plugin-arcaeabot/blob/v3.0.0/CHANGELOG.MD)

## 如何开始 Quick Start
### 有任何问题都可以前往QQ问题交流群[646089633](https://jq.qq.com/?_wv=1027&k=aB1dMnhe)

***请注意! 初次加载插件后会生成配置文件，您需要填写相关配置才能正常使用***

使用前请确保您的Python版本>=3.8

项目默认使用AUA (ArcaeaUnlimitedApi)，您需要申请相关apiurl与token(user-agent)并在机器人所在目录`data\arcaea\config.yml`中填写

<div align="center">

| 参数               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| aua_url | AUA的地址，如"https://www.example.com"</br>|
| aua_token | AUA的认证token，如"sb616" |

</div>

使该项目被您的 NoneBot2 (nonebot2 及 nonebot-adapter-onebot 版本不得低于 `2.0.0-beta4` ) 机器人作为插件加载, 至于如何做, 您应该懂的。

### 首次使用您需要更新资源文件(assets/song, assets/char)

- 向bot发送"/arc assets_update"以更新资源文件。
#### 如果更新失败（资源更新服务器炸了）
- 您可以使用[ArcaeaAssetsUpdater](https://github.com/SEAFHMC/ArcaeaAssetsUpdater)搭建自己的资源更新服务器，然后在 config.yml 中填写您的api地址)
- 还可以直接从[百度云](https://pan.baidu.com/s/1UWqU5S6tR7eG6s_fRK6Ksg?pwd=srhw)下载资源文件（更新至4.0.255c），并放置于bot目录/data/arcaea/assets中

## 指令 Command

<div align="center">


![image](nonebot_plugin_arcaeabot/resource/help.png)


</div>
  
## To Do
- 咕咕咕

## 感谢

- [Awbugl/Andreal](https://github.com/Awbugl/Andreal)
- [DiheChen/nonebot-plugin-arcaea](https://github.com/DiheChen/nonebot-plugin-arcaea)
- [iyume/nonebot-plugin-arcaea](https://github.com/iyume/nonebot-plugin-arcaea)
