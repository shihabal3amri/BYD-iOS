# BYD iOS 多语言版 · 公开测试

中国版 BYD iPhone 应用现支持英语、阿拉伯语、俄语、西班牙语和简体中文。包含翻译更新、自定义底部标签栏、小组件和可选的靠近解锁功能。西班牙语翻译仍在审校中。选择简体中文会保留原文。

[下载 IPA · 351 MB](https://shihabal3amri.github.io/BYD-iOS/zh-Hans/) · [更新说明与校验值](https://github.com/shihabal3amri/BYD-iOS/releases/tag/v9.16.0-r6)

## 修订版 6 新增：语言与翻译更新

新增西班牙语和简体中文、签名翻译包下载，并修复设置项、对话框和主屏幕快捷操作标题的翻译。在**设置 → 翻译**中可手动更新，自动更新默认关闭。完全关闭并重新打开 BYD 后生效。

安装时选择 **Keep App Extensions**。更新后打开 BYD 约 30 秒，再从小组件库添加 BYD。小组件跟随所选语言，但翻译仍包含在 IPA 中。

BYD 包含四个小组件扩展，连同主应用共使用五个 App ID。可在 AltStore → My Apps → View App IDs 查看剩余额度。[了解 App ID 限制。](https://faq.altstore.io/altstore-classic/app-ids)

## 1. 设置 AltStore Classic

如果已安装 AltStore Classic，请继续下一步。否则，先在电脑上安装 **AltServer**，再通过它在 iPhone 上安装 **AltStore Classic**。使用您自己的 Apple 账户，无需付费开发者会员。iOS 16 及以上需开启开发者模式。

[macOS 指南](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) · [Windows 指南](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows)

## 2. 安装或更新 BYD

1. 点击上方的**添加至 AltStore Classic**，并确认添加软件源。
2. 在 AltStore 中找到 **BYD Localized**，查看权限并使用您自己的 Apple 账户安装。出现提示时选择 **Keep App Extensions**（保留应用扩展）。
3. 打开 BYD 并登录您自己的账户。在**我的 → 设置**中选择语言和底部标签。

**已经安装？**刷新 AltStore 软件源，在 **My Apps** 中选择 BYD 的 **Update**。版本应为 **9.16.0 · 修订版 6**。保留现有应用并使用同一 Apple 账户，以保留本地数据。

安装、更新或续签时，请保持 AltServer 运行，并通过同一 Wi-Fi 或 USB 连接。免费 Apple 账户需在七天签名有效期结束前为 AltStore 和 BYD 续签。下载约为 351 MB，速度取决于您与 GitHub 的连接。

如果按钮无法打开 AltStore，请在 **Browse → Sources → +** 中添加以下地址：

`https://raw.githubusercontent.com/shihabal3amri/BYD-iOS/main/source.json`

## 通过 Impactor 安装

将 IPA 导入 [Impactor](https://github.com/claration/Impactor)，应用名称保持为 **BYD**，并保留所有小组件扩展。使用您自己的 Apple 账户签名并安装。

若出现与 **appIdName** 有关的 **Developer API error 35**，请将名称设为 BYD，然后使用同一 IPA 重试。保留默认应用标识和应用组处理方式。仅下载 IPA 并不会完成安装。

## 靠近解锁 · 可选测试功能

打开**我的 → 设置 → 靠近解锁**。使用已激活的 BYD 蓝牙钥匙，在靠近时解锁，并可选择离开时上锁。新用户的自动操作、位置支持、运动提示和测试记录均**默认关闭**。已有测试用户保留保存的设置。

1. 先确认 BYD 原有蓝牙上锁和解锁正常。打开**选择距离**，按日常携带方式放置手机，在两个位置测量并保存。校准期间暂停自动操作。
2. 开启**靠近解锁**，按需开启**离开时上锁**。从远离车辆的位置开始，靠近再离开，检查车辆的实际响应。每部手机应单独校准。
3. 需要锁屏使用时，打开**后台检测 → 位置支持**，按照提示授权，并在系统提供时允许后台定位。**运动提示**为可选功能，需要运动与健身权限。重启手机或强制关闭应用后，请重新打开 BYD。

后台支持可能增加耗电，不能保证持续或整夜运行。此功能在手机本地处理位置，不保存或上传坐标。BYD 其他位置功能有各自的设置。

**已知 XS 问题：**一部 iPhone XS 的信号读数不稳定，早期测试中曾报告在室内意外解锁。更新至 iOS 18.7.10 后仍存在。原因尚未确定，不能认定为硬件故障。如果远近读数重叠或出现意外操作，请关闭此功能并反馈。

反馈前可开启测试记录、标记重要时刻，并在结束后导出。请注明手机及 iOS、车型、阈值、屏幕状态和车辆实际响应。公开分享前请检查日志。

## 公开测试 · 修订版 6

已在 iPhone X 和 Android 上验证签名翻译包更新。快捷操作适配器通过了 145 项真实 UIKit 对象检查，现有回归检查也已通过。当前生产安装包尚未在未越狱 iPhone 上完成安装验证。

需要 iOS 15 或更新版本。西班牙语仍在审校，部分动态内容和图片仍为中文。小组件翻译随应用包更新。已报告的 XS 靠近解锁问题仍未解决，个人资料页也可能为空白。

## 更新说明与校验值

`BYD-iOS_9.16.0_r6.ipa`

SHA-256: `9264280e225c61d1a115211433aa10e9b37aec5d4f94bc6fd7ae446aab36ec04`

## 接收版本更新通知

订阅 Telegram 频道并开启通知，及时了解新版本。

[订阅 Telegram](https://t.me/byd_localized)

本项目为非官方项目，与比亚迪无隶属关系，也未获得其认可。原版应用及资源属于各自所有者。不保证侧载版本支持受 Apple 限制的 Wallet 车钥匙、推送通知或 Siri 等功能。本软件源用于 AltStore Classic，并非 AltStore PAL。
